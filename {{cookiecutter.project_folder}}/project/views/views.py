{%- if cookiecutter.microservice_with_swagger_and_connexion == 'y' -%}
import connexion
from flask import jsonify


def get():
    return jsonify({}), 200


def search():
    return get()


def post():
    if connexion.request.is_json:
        data = connexion.request.get_json()
        return jsonify(data)
    return jsonify({})
{%- elif cookiecutter.microservice_with_swagger_and_connexion != 'y' -%}
from flask import jsonify, Blueprint


app_bp = Blueprint('simple_page', __name__)


@app_bp.route('/', methods=["GET"])
def get():
    return jsonify({}), 200


@app_bp.route('/', methods=["POST"])
def post():
    return jsonify({})
{%- endif %}
