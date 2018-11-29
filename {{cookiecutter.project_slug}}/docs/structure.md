# Structure

You have a project with this structure:

```
    mkdocs.yml          # The configuration file.
    docs/
        index.md        # The documentation homepage.
        ...             # Other markdown pages, images and other files.
    README.md           # Basic information to display in CVS
    Dockerfile    
    manage.py
    setup.py
    requirements.txt
    requirements-tests.txt
    requirements-docker.txt
    tests.sh
    tox.ini
    {{cookiecutter.project_slug}}
        __init__.py
        config.py
        models          # database models
        swagger
            *.yaml      # API definition
        views
    tests/        
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

## py-ms
py-ms is a library that contains a set of common features for microservices.

# Specific
For project configuration see [configuration section](configuration.md).

## {{cookiecutter.project_slug}}/models/init_db.py
Initialize `flask_sqlalchemy.SQLAlchemy object`.

## {{cookiecutter.project_slug}}/models/models.py
Project specific models.

## {{cookiecutter.project_slug}}/swagger/swagger.yaml
Use to define your rest behaviour, endpoints and routes. See `connexion <http://connexion.readthedocs.io>`_ docs to how add new views

## {{cookiecutter.project_slug}}/views
Use views.py or create your file.

## {{cookiecutter.project_slug}}/__init__.py
This file init the project calling `create_app` method. Initialize the Flask app, register [blueprints](http://flask.pocoo.org/docs/0.12/blueprints/) and initialize all libraries like Swagger, database, trace system, custom logger format, etc.
