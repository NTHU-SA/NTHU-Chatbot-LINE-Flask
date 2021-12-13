from flask import Flask
import logging

app = Flask(__name__)

from app.views import base
from app.linebot import callback, followEvent, messageEvent, postbackEvent

# bind gunicon logger to flask_app logger
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)
