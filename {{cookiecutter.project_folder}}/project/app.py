import logging
import logging.config

from pyms.flask.app import Microservice
{% if cookiecutter.create_model_class == 'y' -%}
from project.models.init_db import db
{% endif -%}
{% if cookiecutter.microservice_with_swagger_and_connexion != 'y' -%}
from project.views.views import app_bp
{% endif %}

class MyMicroservice(Microservice):
    def init_libs(self) -> None:
{% if cookiecutter.create_model_class == 'y' %}
        db.init_app(self.application)
        with self.application.test_request_context():
            db.create_all()
{% endif -%}
{% if cookiecutter.microservice_with_swagger_and_connexion != 'y' %}
        self.application.register_blueprint(app_bp, url_prefix='{{ cookiecutter.application_root }}')
{% endif %}
    def init_logger(self) -> None:
        if not self.application.config["DEBUG"]:
            super().init_logger()
        else:
            level = "DEBUG"
            LOGGING = {
                'version': 1,
                'disable_existing_loggers': False,
                'handlers': {
                    'console': {
                        'level': level,
                        'class': 'logging.StreamHandler',
                    },
                },
                'loggers': {
                    '': {
                        'handlers': ['console'],
                        'level': level,
                        'propagate': True,
                    },
                    'anyconfig': {
                        'handlers': ['console'],
                        'level': "WARNING",
                        'propagate': True,
                    },
                    'pyms': {
                        'handlers': ['console'],
                        'level': "WARNING",
                        'propagate': True,
                    },
                    'root': {
                        'handlers': ['console'],
                        'level': level,
                        'propagate': True,
                    },
                }
            }

            logging.config.dictConfig(LOGGING)


def create_app() -> None:
    """Initialize the Flask app, register blueprints and intialize all libraries like Swagger, database, the trace system...
    return the app and the database objects.
    :return:
    """
    ms = MyMicroservice(path=__file__)
    return ms.create_app()
