from flask import Blueprint


series = Blueprint('series', __name__)


@series.route('/')
def all():
    return 'Hello World!'
