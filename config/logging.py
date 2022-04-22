import os


def get_logging_config(app):
    BASE_DIR = app.root_path
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '[%(asctime)s.%(msecs)03d] [%(name)s] [%(levelname)s] [%(request_id)s] %(message)s',
                'datefmt': '%d/%m/%Y %H:%M:%S',
            },
        },
        'handlers': {
            'debug': {
                'level': 'DEBUG',
                'formatter': 'default',
                'filters': ['request_id'],
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(BASE_DIR, 'logs', 'debug.log'),
                'maxBytes': 1024000
            },
        },
        'loggers': {
            'debug': {
                'level': 'DEBUG',
                'handlers': ['debug']
            },
        },
        'filters': {
            'request_id': {
                '()': 'utils.request_id.RequestIdFilter',
            },
        },
    }
