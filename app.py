from logging.config import dictConfig

import flask

from config.logging import get_logging_config
from config.common import APP_CONFIG
from utils.flask import register_blueprints
from api.v1 import routes as api_v1_routes
from web import routes as web_routes

# Logging configuration
dictConfig(get_logging_config(flask.Flask(__name__)))

# Application configuration
app = flask.Flask(__name__,
                  static_url_path='',
                  static_folder='static',
                  template_folder='templates')

# Register blueprints
register_blueprints(app, api_v1_routes)
register_blueprints(app, web_routes)

# Run application
if __name__ == '__main__':
    app.run(
        host=APP_CONFIG.get('FLASK_HOST', '0.0.0.0'),
        port=APP_CONFIG.get('FLASK_PORT', 5000),
        debug=APP_CONFIG.get('FLASK_DEBUG', False)
    )
