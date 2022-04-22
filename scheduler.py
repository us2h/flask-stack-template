from logging.config import dictConfig

import flask
from celery import Celery
from celery.schedules import crontab

from config.common import APP_CONFIG
from config.logging import get_logging_config


# Logging configuration
dictConfig(get_logging_config(flask.Flask(__name__)))


# We use Redis for broker and backend
REDIS_URL = 'redis://{0}:{1}/{2}'.format(
    str(APP_CONFIG.get('CELERY_BROKER_REDIS_HOST', 'redis')),
    str(APP_CONFIG.get('CELERY_BROKER_REDIS_PORT', 6379)),
    str(APP_CONFIG.get('CELERY_BROKER_REDIS_DATABASE', 0))
)

# Configure celery app
app = Celery(
    'app',
    broker=REDIS_URL,
    backend=REDIS_URL,
)

app.conf.update(
    enable_utc=True,
    timezone=APP_CONFIG.get('TIMEZONE', 'UTC'),
    result_expires=120,
    imports=('tasks.hello_world',)
)


# Schedule
app.conf.beat_schedule = {
    'interval_task': {
        'task': 'tasks.hello_world.hello_world',
        'schedule': int(APP_CONFIG.get('TASK_INTERVAL_SECONDS', 10)),
    },
    'scheduled_task': {
        'task': 'tasks.hello_world.hello_world',
        'schedule': crontab(
            hour=int(APP_CONFIG.get('TASK_SCHEDULED_HOUR', 1)),
            minute=int(APP_CONFIG.get('TASK_SCHEDULED_MINUTES', 0)),
            day_of_week='*'
        ),
    }
}
