# Overview

{{cookiecutter.project_short_description}}

# Stack

* [connexion](<http://connexion.readthedocs.io>)
* [Flask](https://github.com/pallets/flask)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/)
* [Flask-Injector](https://github.com/alecthomas/flask_injector)
* [Flask-Script](https://flask-script.readthedocs.io/en/latest/)
* [Opentracing](https://github.com/opentracing-contrib/python-flask)

# API Documentation

The Microservice create a URL to inspect the Swagger documentation of the api in:

```
http://localhost:5000/[APPLICATION_ROOT]/ui/
```

Our API Rest work with `connexion <http://connexion.readthedocs.io>`_. You can see connexion docs or the official
`Swagger documentation <https://swagger.io/specification/>`_ to add the syntax to your APIS and create your Swagger docs.

The API definition is contained in `{{cookiecutter.project_slug}}/swagger/*.yml` and it is possible to convert to [RAML files](https://mulesoft.github.io/oas-raml-converter/) if necessary.
