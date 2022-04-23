# Flask bootstrap project
You could use this template to easy and fast start new project for API, Web, tasks, etc without configuration some basic things like logging, celery tasks, endpoints routing, web templates configuration etc.

## Features:

* Template for web pages with static
* Template for API endpoints
* Scheduled tasks with Celery
* Logging
* Configuration with ENV variables support


## Running:

### Docker
First you need to build the image:

```bash
$ docker build -t my_project .
```
After that you can run the container:
```bash
$ docker run -d \
  --name=clicker \
  --rm \
  -ti \
  -p 80:80 \
  -v /local/path:/app/logs \
  my_project
```
Change the port if you need and `/local/path` to your own path in host os where you want to store logs.

### Docker-compose
Run docker-compose configuration:

```bash
$ docker-compose up --build -d
```
It will use `docker-compose.yml` file from the current directory.
If you don't need periodic tasks you can remove `tasks` and `redis` services from `docker-compose.yml` file.
Redis is mandatory for periodic tasks. It used as celery broker and as cache for celery tasks.

## Configuration

### Web pages
To add new web page you need to add new template to `templates` directory.
Then you need to add python file to web directory and add necessary imports to `__init__.py` file. Or you can extend existing configuration.

### API endpoints
To add new API endpoint you need to add new python file to `api/v1` directory and add necessary imports to `__init__.py` file. Or you can extend existing configuration.
The main difference between API endpoints and web pages is that API endpoints are not able to serve static files.

### Scheduled tasks
To add new scheduled task you need to add new task file with to `tasks` directory.
Then extend imports section in celery app configuration in `scheduler.py` file.

```python
app.conf.update(
    ...
    imports=('tasks.hello_world', 'tasks.new_task')
)
```

And add new task to scheduler section in same file.

```python
app.conf.beat_schedule = {
    ...
    'new_task': {
        'task': 'tasks.new_task.new_task',
        'schedule': int(APP_CONFIG.get('TASK_INTERVAL_SECONDS', 10)),
    },
}
```
To start scheduler you need to run:
```bash
$ celery -A scheduler worker -B
```
or if you run it in production split it in two processes:
```bash
$ celery -A scheduler worker
```
and 
```bash
$ celery -A scheduler beat
```

### Logging
Logging configuration located in `config/logging.py` file.
You could add more loggers, formatters and handlers to it. Just use existing configuration as example.

Also, one filter already added to logging configuration, this is `RequestIdFilter`. It adds request id to all log records so you can track logs by request id from beggining of request to end.

To start logging anywhere in your code you need to initialize necessary logger. As parameter, you need to pass logger name as it defined in `loggers` section of your logging configuration.

```python
import logging
...
debug_logger = logging.getLogger('debug')
```
then you can use logger to log messages:
```python
debug_logger.debug('message')
```

### Overriding variables
If you need to override some config variable without changing it in `common.py` you could set necessary variable as environment variable on your system.

Or if you're using docker or docker-compose you could set them in `.env` file or pass as environment variables to docker container.
