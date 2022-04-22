from utils.config import update_config_from_env

"""
Basic configuration
"""
APP_CONFIG = {
    # Flask config
    'FLASK_HOST': '0.0.0.0',
    'FLASK_PORT': 5000,
    'FLASK_DEBUG': False,
}

"""
If .env file exist and have keys also existing in this config then take values from .env file
"""
APP_CONFIG = update_config_from_env(APP_CONFIG)
