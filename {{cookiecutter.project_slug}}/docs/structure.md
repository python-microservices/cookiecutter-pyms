# Structure

You have a project with this structure:

```
    mkdocs.yml          # The configuration file.
    docs/
        index.md        # The documentation homepage.
        ...             # Other markdown pages, images and other files.
    README.md           # Basic information to display in CVS
    manage.py
    setup.py
    requirements.txt
    requirements-tests.txt
    requirements-docker.txt
    tests.sh
    tox.ini
    pyms                # utilities for database access, logging, tracing, etc
    {{cookiecutter.project_slug}}
        __init__.py
        config.py
        models          # database models
        swagger
            *.yaml      # API definition
        tests
        views
```

# Common

## manage.py

A Django style command line. Use this to start the application like:
```bash
python manage.py runserver
```

You can set the host and the port with:
```bash
python manage.py runserver -h 0.0.0.0 -p 8080
```

## pyms/healthcheck/healthcheck.py
This views is usually used by Kubernetes, Eureka and other systems to check if our application is up and running

## pyms/logger/logger.py
Print logger in JSON format to send to server like Elasticsearch. Inject span traces in logger

## pyms/models/__init__.py
Initizalize `flask_sqlalchemy.SQLAlchemy object`

## pyms/tracer/main.py
Create an injector `flask_opentracing.FlaskTracer` to use in our projects

# Specific

## {{cookiecutter.project_slug}}/__init__.py
This file init the project with the funcion `create_app`. Initialize the Flask app, register `blueprints <http://flask.pocoo.org/docs/0.12/blueprints/>`_
and intialize all libraries like Swagger, database, the trace system...

## {{cookiecutter.project_slug}}/config.py
See :doc:`configuration </configuration>` section

## {{cookiecutter.project_slug}}/views
use views.py or create your file.

## swagger/*.yaml
Use to define your rest behaviour, endpoints and routes. See `connexion <http://connexion.readthedocs.io>`_ docs to how add new views
