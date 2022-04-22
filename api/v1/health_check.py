import flask


routes = flask.Blueprint('health_check', __name__)


@routes.route('/ping', methods=['GET'])
def ping():
    return flask.Response('pong', status=200)
