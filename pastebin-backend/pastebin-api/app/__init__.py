from flask import Flask
from celery import Celery
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging
import logging.handlers
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["SQLALCHEMY_DATABASE_URI"]
app.config['CACHE_FOLDER'] = '/cache'
app.config['LOGS_FOLDER'] = '/logs'
app.config['REDIS_HOST'] = os.environ["REDIS_HOST"]
app.config['REDIS_PASS'] = os.environ["REDIS_PASS"]
app.config['REDIS_PORT'] = 6379
app.config['CELERY_BROKER_URL'] = os.environ["CELERY_BROKER_URL"]
app.config['CELERY_RESULT_BACKEND'] = os.environ["CELERY_RESULT_BACKEND"]
app.config['SPACES_URL'] = os.environ["SPACES_URL"]
app.config['SPACES_KEY'] = os.environ["SPACES_KEY"]
app.config['SPACES_SECRET'] = os.environ["SPACES_SECRET"]
CORS(app)

db = SQLAlchemy(app)

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

os.makedirs(app.config['LOGS_FOLDER'], exist_ok=True)
handler = logging.handlers.RotatingFileHandler("{}/log.txt".format(app.config['LOGS_FOLDER']),
    maxBytes=1024 * 1024)
app.logger.addHandler(handler)

from app import routes, models
