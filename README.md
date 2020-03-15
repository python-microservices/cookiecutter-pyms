# Cookiecutter Python Microservice


[Cookiecutter](https://github.com/audreyr/cookiecutter) template for a Python microservice.

* GitHub repo: https://github.com/python-microservices/microservices-template

## Features
* Create a "ready to work" microservice project like our [Microservice Scaffold](https://github.com/python-microservices/microservices-scaffold)
* Deploy your microservice with [Microservice chassis pattern](https://microservices.io/patterns/microservice-chassis.html)
powered by [PyMS](https://github.com/python-microservices/pyms), [Flask](https://flask.palletsprojects.com/en/1.1.x/), [Connexion](https://github.com/zalando/connexion) 
and [Opentracing](https://opentracing.io/).
* Testing setup with ``py.test``
* [Travis-CI](http://travis-ci.org/): Ready for Travis Continuous Integration testing
* [Tox](http://testrun.org/tox/) testing: Setup to easily test for Python 3.6
* [Mkdocs](https://www.mkdocs.org/) docs: Documentation ready for generation with, for example


## Quick Start

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher):

```
  $ pip install --upgrade virtualenv
  $ virtualenv env
  $ source env/bin/activate
  $ pip install -U cookiecutter
```

Generate a Python Microservice project:


```
  (env) $ cookiecutter https://github.com/python-microservices/microservices-template.git
    project_repo_url [https://github.com/python-microservices/microservices-scaffold]: 
    project_name [Python Microservices Boilerplate]: prueba descarga
    project_folder [prueba_descarga]: 
    project_short_description [Python Boilerplate contains all the boilerplate you need to create a Python package.]: 
    create_model_class [y]: 
    microservice_with_swagger_and_connexion [y]: 
    microservice_with_traces [y]: 
    microservice_with_metrics [y]: 
    application_root [/prueba_descarga]: 
    Select open_source_license:
    1 - MIT license
    2 - BSD license
    3 - ISC license
    4 - Apache Software License 2.0
    5 - GNU General Public License v3
    6 - Not open source
    Choose from 1, 2, 3, 4, 5, 6 [1]: 
  
```
## Installation

### Install with virtualenv
```bash
virtualenv --python=python[3.6|3.7|3.8] venv
source venv/bin/activate
pip install -r requirements.txt
```

### Install with pipenv
```bash
pip install pipenv
pipenv install
```

#### Advantages over plain pip and requirements.txt
[Pipenv](https://pipenv.readthedocs.io/en/latest/) generates two files: a `Pipfile`and a `Pipfile.lock`.
* `Pipfile`: Is a high level declaration of the dependencies of your project. It can contain "dev" dependencies (usually test related stuff) and "standard" dependencies which are the ones you'll need for your project to function
* `Pipfile.lock`: Is the "list" of all the dependencies your Pipfile has installed, along with their version and their hashes. This prevents two things: Conflicts between dependencies and installing a malicious module.

For a more in-depth explanation please refer to  the [official documentation](https://pipenv.readthedocs.io/en/latest/).

## Run your python script
```bash
python manage.py runserver
```


## Check the result

Your default endpoints will be in this url:
```bash
http://127.0.0.1:5000/films/
http://127.0.0.1:5000/actors/
```

This URL is set in your `config.yml`:

```yaml
pyms:
  config:
    DEBUG: false
    TESTING: false
    APP_NAME: Template
    APPLICATION_ROOT : "" # <!---
```

You can acceded to a [swagger ui](https://swagger.io/tools/swagger-ui/) in the next url:
```bash
http://127.0.0.1:5000/ui/
```

This PATH is set in your `config.yml`:

```yaml
pyms:
  services:
    swagger:
      path: "swagger"
      file: "swagger.yaml"
      url: "/ui/" # <!---
```

Read more info in the documentation page: 
https://microservices-scaffold.readthedocs.io/en/latest/

# Docker
You can dockerize this microservice wit this steps:
* Create and push the image
  ```bash
  docker build -t films -f Dockerfile .
  ```
* Run the image:
  ```bash
  docker run -d -p 5000:5000 films
  ```
    