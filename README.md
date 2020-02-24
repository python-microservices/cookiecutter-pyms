# Cookiecutter Python Microservice


[Cookiecutter](https://github.com/audreyr/cookiecutter) template for a Python microservice.

* GitHub repo: https://github.com/python-microservices/microservices-template

## Features

* Testing setup with ``py.test``
* [Travis-CI](http://travis-ci.org/) - The web framework usedTravis-CI_: Ready for Travis Continuous Integration testing
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

Build and Run the microservice:

```
  (env) $ cd avengers_api
  (env) $ docker build -t ms_avenger_api -f Dockerfile .
  (env) $ docker run -p 5000:5000 --env CONFIGMAP_FILE=/microservice/config-docker.yml ms_avenger_api:latest

```
