from app import app, celery, db

from flask import request, abort, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin
from app.models import Pastes
from datetime import datetime, timedelta
from hashlib import md5
import os
import redis
import json
import shutil
import boto3

BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_character(digit):
    return BASE62[digit]


def base_encode(num, base=62):
    digits = []
    while num > 0:
        remainder = num % base
        digits.append(remainder)
        num = num // base
    digits = digits[::-1]
    return list(map(get_character, digits))


def generate_url(ip_addr, timestamp, url_length=7):
    key = str(ip_addr + timestamp).encode('utf-8')
    hexvalue = md5(key).hexdigest()
    decvalue = int(hexvalue, 16)
    url = base_encode(decvalue)
    return ''.join(url[:7])


@app.route('/api/v1/paste', methods=['POST'])
@cross_origin()
def write_paste():
    return write_paste_async(request)


@celery.task
def write_paste_async(request):
    if not request.json:
        abort(400)  # missing response body

    if not {"paste_contents", "expiration_length_in_minutes"} <= request.json.keys():
        abort(400)  # missing one or more required keys

    ip_addr = request.remote_addr
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")
    key = str(ip_addr + timestamp).encode('utf-8')
    shortlink = generate_url(ip_addr, timestamp)

    # write to cache folder
    paste_path = "{}/{}.txt".format(app.config['CACHE_FOLDER'], shortlink)
    os.makedirs(os.path.dirname(paste_path), exist_ok=True)
    f = open(paste_path, 'w')
    f.write(request.json["paste_contents"])
    f.close()

    # upload to S3
    path = "{}.txt".format(shortlink)
    session = boto3.session.Session()
    client = session.client('s3', region_name='nyc3', endpoint_url=app.config["SPACES_URL"],
        aws_access_key_id=app.config["SPACES_KEY"], aws_secret_access_key=app.config["SPACES_SECRET"])
    client.upload_file(paste_path, 'pastes', path)

    # add paste to database
    paste = Pastes(shortlink=shortlink,
                   expiration_length_in_minutes=request.json['expiration_length_in_minutes'],
                   created_at=datetime.now(),
                   paste_path=path)

    db.session.add(paste)
    db.session.commit()

    return jsonify({"shortlink": shortlink }), 200


@app.route('/api/v1/paste', methods=['GET'])
def get_paste():

    shortlink = request.args.get('shortlink')
    paste = Pastes.query.filter_by(shortlink=shortlink).first()

    if paste is None:  # bad request
        abort(400)

    # update redis cache with hit
    r = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'],
        db=0, password=app.config['REDIS_PASS'])
    period = datetime.now().strftime("%Y-%m")
    key = "{}-{}".format(period, shortlink)
    r.incrby(key, 1)
    r.close()

    # file destination
    path = paste.paste_path
    cache_path = "{}/{}.txt".format(app.config['CACHE_FOLDER'], shortlink)

    # download file from S3 if it is not at file destination
    if not os.path.exists(cache_path):
        session = boto3.session.Session()
        client = session.client('s3', region_name='nyc3', endpoint_url=app.config["SPACES_URL"],
            aws_access_key_id=app.config["SPACES_KEY"], aws_secret_access_key=app.config["SPACES_SECRET"])
        client.download_file('pastes', path, cache_path)

    # load paste_contents from cache
    f = open(cache_path, 'r')
    paste_contents = f.read()
    f.close()

    # return paste_contents
    body = {
        "paste_contents": paste_contents,
        "created_at": paste.created_at,
        "expires_at": paste.created_at + timedelta(minutes=paste.expiration_length_in_minutes)
    }

    return jsonify(body), 200


@app.route('/api/v1/stats/hits', methods=['GET'])
def get_hits():

    period = request.args.get('period')
    shortlink = request.args.get('shortlink')
    key = "{}-{}".format(period, shortlink)
    
    # read hits from redis cache
    r = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'],
        db = 0, password=app.config['REDIS_PASS'])
    value = r.get(key)
    r.close()

    if value:
        return jsonify({"hits": value.decode('UTF-8')}), 200
    
    return jsonify({"hits": 0}), 200


@app.before_request
def pre_request():
    app.logger.info("{ip} {date} {method} {url}".format(
        ip=request.remote_addr, date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        method=request.method, url=request.url
    ))
