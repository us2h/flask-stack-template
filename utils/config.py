import os


def update_config_from_env(config: dict) -> dict:
    for key in config.keys():
        if key in os.environ:
            if isinstance(config[key], bool):
                if os.environ[key] in ['true', 'True']:
                    config[key] = True
                if os.environ[key] in ['false', 'False']:
                    config[key] = False
            else:
                config[key] = os.environ[key]
    return config