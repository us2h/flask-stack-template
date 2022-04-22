import logging
import flask
from flask import render_template


debug_logger = logging.getLogger('debug')

routes = flask.Blueprint('index', __name__)


@routes.route('/')
def index():
    debug_logger.debug('test')
    return render_template('index.html')
