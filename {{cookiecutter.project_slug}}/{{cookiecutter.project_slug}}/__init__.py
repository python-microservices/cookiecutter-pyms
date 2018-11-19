from pyms.flask.app import Microservice
{% if cookiecutter.create_model_class == 'y' -%}
from {{cookiecutter.project_slug}}.models.init_db import db
{% endif %}

__author__ = "{{cookiecutter.full_name}}"
__email__ = "{{cookiecutter.email}}"
__version__ = "{{cookiecutter.version}}"


{% if cookiecutter.create_model_class == 'y' -%}
class MyMicroservice(Microservice):
    def init_libs(self, app):
        db.init_app(app)
        with app.test_request_context():
            db.create_all()
{% endif %}

def create_app():
    """Initialize the Flask app, register blueprints and intialize all libraries like Swagger, database, the trace system...
    return the app and the database objects.
    :return:
    """
    {% if cookiecutter.create_model_class == 'y' -%}
    ms = MyMicroservice(service="ms", path=__file__)
    {% else %}
    ms = Microservice(service="ms", path=__file__)
    {% endif %}
    return ms.create_app()
