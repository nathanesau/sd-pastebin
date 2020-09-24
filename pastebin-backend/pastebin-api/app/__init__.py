from flask import Flask
from celery import Celery
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging
import logging.handlers
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@134.122.41.28/postgres'
app.config['PASTES_FOLDER'] = '/pastes'
app.config['CACHE_FOLDER'] = '/cache'
app.config['LOGS_FOLDER'] = '/logs'
app.config['REDIS_HOST'] = '134.122.41.28'
app.config['REDIS_PORT'] = 6379
app.config['CELERY_BROKER_URL'] = '134.122.41.28'
app.config['CELERY_RESULT_BACKEND'] = '134.122.41.28'
CORS(app)

db = SQLAlchemy(app)

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

os.makedirs(app.config['LOGS_FOLDER'], exist_ok=True)
handler = logging.handlers.RotatingFileHandler("{}/log.txt".format(app.config['LOGS_FOLDER']),
    maxBytes=1024 * 1024)
app.logger.addHandler(handler)

from app import routes, models
