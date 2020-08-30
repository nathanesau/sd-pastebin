from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging
import logging.handlers
import os

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
app.config['PASTES_FOLDER'] = 'pastes'
app.config['LOGS_FOLDER'] = 'logs'
app.config['REDIS_HOST'] = 'localhost'
app.config['REDIS_PORT'] = 6379
db = SQLAlchemy(app)

os.makedirs(app.config['LOGS_FOLDER'], exist_ok=True)
handler = logging.handlers.RotatingFileHandler("{}/log.txt".format(app.config['LOGS_FOLDER']),
    maxBytes=1024 * 1024)
app.logger.addHandler(handler)

from app import routes, models
