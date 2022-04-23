import logging
import flask
from flask import render_template

# Remove next line if you don't need logging here
debug_logger = logging.getLogger('debug')

routes = flask.Blueprint('index', __name__)


@routes.route('/')
def index():
    # Remove next line if you don't need logging here
    debug_logger.debug('test')
    return render_template('index.html')
