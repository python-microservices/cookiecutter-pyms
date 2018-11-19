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
  (env) $ full_name [Nick Fury]: Nicholas Joseph Fury
  (env) $ email [nick_fury@avengers.com]: 
  (env) $ project_repo_url [https://github.com/python-microservices/microservices-scaffold]: https://github.com/nickfury/my-ms
  (env) $ project_name [Python Microservices Boilerplate]: Avengers API
  (env) $ project_slug [avengers_api]: 
  (env) $ project_short_description [Python Boilerplate contains all the boilerplate you need to create a Python package.]: 
  (env) $ create_model_class [y]: y
  (env) $ model_name [Colors (ignore if you response 'n' in create_model_class)]: Avenger
  (env) $ table_name [colors (ignore if you response 'n' in create_model_class)]: avenger
  (env) $ version [0.1.0]: 0.0.1
  (env) $ pypi_server []: nexus3.avengers.com/my-pypi-server
  (env) $ create_author_file [y]: n
  (env) $ Select open_source_license:
  (env) $  1 - MIT license
  (env) $  2 - BSD license
  (env) $  3 - ISC license
  (env) $  4 - Apache Software License 2.0
  (env) $  5 - GNU General Public License v3
  (env) $  6 - Not open source
  (env) $ Choose from 1, 2, 3, 4, 5, 6 (1, 2, 3, 4, 5, 6) [1]: 6
  
```

Build and Run the microservice:

```
  (env) $ cd avengers_api
  (env) $ docker build -t ms_avenger_api -f Dockerfile .
  (env) $ docker run -p 5000:5000 --env CONFIGMAP_FILE=/microservice/config-docker.yml ms_avenger_api:latest

```
