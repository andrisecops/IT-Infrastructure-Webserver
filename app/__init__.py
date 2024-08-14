from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes, dashboard, monitoring, analysis

# Inisialisasi logging
import logging
from logging.handlers import RotatingFileHandler
import os

if not os.path.exists(app.config['LOG_PATH']):
    os.makedirs(app.config['LOG_PATH'])

file_handler = RotatingFileHandler(os.path.join(app.config['LOG_PATH'], 'system.log'), maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
