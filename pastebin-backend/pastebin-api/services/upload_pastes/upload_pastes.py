# simple linux service to upload files to spaces 
# after request comes to server, files are saved in /root/pastes
# this script will be run every 5 seconds
# any new files will be uploaded to spaces

import boto3
from datetime import datetime
import os
import glob
import time
import shutil
from datetime import datetime
  
SPACES_URL="https://digitalspaces.nyc3.digitaloceanspaces.com"
SPACES_KEY="S5FHP2J6FFJ3UQKVX6HW"
SPACES_SECRET="6TyMkyAkuLzvQOfKjkXTKxqp1JalLQ8kDQYKIs1V3Wk"

import logging
from logging.handlers import RotatingFileHandler

def upload_files_task():
    logger.info("running upload files task at {}".format(datetime.now()))

    # copy pastes from docker container to local drive
    session = boto3.session.Session()
    client = session.client('s3', region_name='nyc3', endpoint_url=SPACES_URL, aws_access_key_id=SPACES_KEY, aws_secret_access_key=SPACES_SECRET)

    for path in glob.glob("/root/pastes/*"):
        fname = path.split('/')[-1]
        client.upload_file(path, 'pastes', fname)
        os.remove(path)

"""
def download_files_task():
    session = boto3.session.Session(aws_access_key_id=SPACES_KEY, aws_secret_access_key=SPACES_SECRET)
    client = session.client('s3', region_name='nyc3', endpoint_url=SPACES_URL, aws_access_key_id=SPACES_KEY, aws_secret_access_key=SPACES_SECRET)

    # download files as necessary
    #client.download_file('pastes', '2WQDyDn.txt', 'out_test.txt')
"""

# create logger
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

# create file handler and set level to debug
fh = RotatingFileHandler('/var/log/upload_pastes.log', maxBytes=2000, backupCount=1)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

while True: # run task forever
    upload_files_task()
    time.sleep(5)
