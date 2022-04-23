from utils.config import update_config_from_env

"""
Basic configuration
"""
APP_CONFIG = {
    # Common
    'TIMEZONE': 'UTC',

    # Flask config
    'FLASK_HOST': '0.0.0.0',
    'FLASK_PORT': 80,
    'FLASK_DEBUG': False,

    # Scheduler config
    'TASK_INTERVAL_SECONDS': 10,
    'TASK_SCHEDULED_HOUR': 1,
    'TASK_SCHEDULED_MINUTE': 0,

    # Celery config
    'CELERY_BROKER_REDIS_HOST': 'redis',
    'CELERY_BROKER_REDIS_PORT': 6379,
    'CELERY_BROKER_REDIS_DATABASE': 0,
}

"""
If .env file exist and have keys also existing in this config then take values from .env file
"""
APP_CONFIG = update_config_from_env(APP_CONFIG)
