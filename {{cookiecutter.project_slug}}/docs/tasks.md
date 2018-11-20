# Tasks

A Makefile file has been created so that you can manage all the tasks that the microservice needs, from cleaning the project, passing a test or publishing a release.

## Makefile tasks
Below is a list of the tasks that make up the makefile with an example.
You need to install `requirements-dev.txt` in order to launch tasks.

### help
To use this Makefile to show hep about this Makefile: 

```
$ make help

clean                remove all build, test, coverage and Python artifacts
clean-build          remove build artifacts
clean-pyc            remove Python file artifacts
clean-test           remove test and coverage artifacts
lint                 check style with flake8 and pylint
test                 run tests with py.test
test-all             run tests on every Python version with tox
coverage             check code coverage quickly with the default Python
docs                 generate Mkdocs HTML documentation, including API docs
servedocs            compile the docs watching for changes
release              package and upload a release
dist                 builds source and wheel package
install              install the package to the active Python's site-packages

```

### clean
To use this Makefile to remove all build, test, coverage and Python artifacts.
```
$ make clean

rm -fr build/
rm -fr dist/
rm -fr .eggs/
rm -fr site/
find . -name '*.egg-info' -exec rm -fr {} +
find . -name '*.egg' -exec rm -f {} +
find . -name '*.pyc' -exec rm -f {} +
find . -name '*.pyo' -exec rm -f {} +
find . -name '*~' -exec rm -f {} +
find . -name '__pycache__' -exec rm -fr {} +
rm -fr .tox/
rm -f .coverage
rm -fr htmlcov/
rm -fr .pytest_cache

```

### clean-build
To use this Makefile to remove build artifacts.
```
$ make clean-build

rm -fr build/
rm -fr dist/
rm -fr .eggs/
rm -fr site/
find . -name '*.egg-info' -exec rm -fr {} +
find . -name '*.egg' -exec rm -f {} +

```

### clean-pyc
To use this Makefile to remove Python file artifacts.
```
$ make clean-pyc

find . -name '*.pyc' -exec rm -f {} +
find . -name '*.pyo' -exec rm -f {} +
find . -name '*~' -exec rm -f {} +
find . -name '__pycache__' -exec rm -fr {} +

```

### clean-test
To use this Makefile to remove test and coverage artifacts.
```
$ make clean-test

rm -fr .tox/
rm -f .coverage
rm -fr htmlcov/
rm -fr .pytest_cache

```

### lint
To use this Makefile to check style with pylint and generate pylintReport.txt
```
$ make lint

pylint avengers_api/*
************* Module avengers_api.__init__
avengers_api/__init__.py:18:0: C0301: Line too long (124/100) (line-too-long)
avengers_api/__init__.py:23:0: C0303: Trailing whitespace (trailing-whitespace)
************* Module avengers_api
avengers_api/__init__.py:1:0: C0111: Missing module docstring (missing-docstring)
avengers_api/__init__.py:10:0: C0111: Missing class docstring (missing-docstring)
avengers_api/__init__.py:22:4: C0103: Variable name "ms" doesn't conform to snake_case naming style (invalid-name)
************* Module avengers_api.models.init_db
avengers_api/models/init_db.py:4:0: C0304: Final newline missing (missing-final-newline)
avengers_api/models/init_db.py:1:0: C0111: Missing module docstring (missing-docstring)
avengers_api/models/init_db.py:4:0: C0103: Constant name "db" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module avengers_api.models.models
avengers_api/models/models.py:1:0: C0111: Missing module docstring (missing-docstring)
avengers_api/models/models.py:15:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module avengers_api.views
avengers_api/views/__init__.py:2:0: C0304: Final newline missing (missing-final-newline)
avengers_api/views/__init__.py:1:0: C0111: Missing module docstring (missing-docstring)
************* Module avengers_api.views.views
avengers_api/views/views.py:35:0: C0305: Trailing newlines (trailing-newlines)
avengers_api/views/views.py:1:0: C0111: Missing module docstring (missing-docstring)
avengers_api/views/views.py:30:8: E1101: Instance of 'scoped_session' has no 'add' member (no-member)
avengers_api/views/views.py:31:8: E1101: Instance of 'scoped_session' has no 'commit' member (no-member)

------------------------------------------------------------------
Your code has been rated at 4.89/10 (previous run: 3.83/10, +1.06)



```

### flake8
To use this Makefile check style with flake8 and generate pyflake8tReport.txt
```
$ make flake8

flake8 avengers_api tests
avengers_api/__init__.py:18:80: E501 line too long (120 > 79 characters)
avengers_api/__init__.py:23:1: W293 blank line contains whitespace
avengers_api/models/init_db.py:4:18: W292 no newline at end of file
avengers_api/models/models.py:15:1: E302 expected 2 blank lines, found 1
avengers_api/views/__init__.py:2:80: E501 line too long (82 > 79 characters)
avengers_api/views/__init__.py:2:83: W292 no newline at end of file
avengers_api/views/views.py:6:1: E303 too many blank lines (3)
avengers_api/views/views.py:14:1: E303 too many blank lines (3)
avengers_api/views/views.py:33:24: F821 undefined name 'avenger'
avengers_api/views/views.py:35:1: W391 blank line at end of file
tests/test_views.py:21:80: E501 line too long (96 > 79 characters)
tests/test_views.py:22:80: E501 line too long (103 > 79 characters)
tests/test_views.py:23:80: E501 line too long (93 > 79 characters)
tests/test_views.py:29:13: E261 at least two spaces before inline comment
tests/test_views.py:40:80: E501 line too long (80 > 79 characters)


```

### test
To use this Makefile to run tests with py.test
```
$ make test

py.test
========================================================= test session starts =============================================================
platform linux -- Python 3.5.2, pytest-4.0.0, py-1.7.0, pluggy-0.8.0
rootdir: /home/nickfury/proyectos/microservicios/avengers_api, inifile:
collected 4 items                                                                                                                                                                                                                                                   

tests/test_views.py ....                                                             [100%]

========================================================== 4 passed in 0.76 seconds ========================================================
```

### test-all
To use this Makefile to run tests on every Python version with tox.
```
$ make test-all

tox
GLOB sdist-make: /home/nickfury/proyectos/microservicios/avengers_api/setup.py
py36 create: /home/nickfury/proyectos/microservicios/avengers_api/.tox/py36
py36 installdeps: -r/home/nickfury/proyectos/microservicios/avengers_api/requirements-tests.txt
py36 inst: /home/nickfury/proyectos/microservicios/avengers_api/.tox/.tmp/package/1/MS-avengers_api-0.1.0.zip
py36 installed: anyconfig==0.9.7,astroid==2.0.4,atomicwrites==1.2.1,attrs==18.2.0,certifi==2018.10.15,chardet==3.0.4,Click==7.0,clickclick==1.2.2,connexion==2.0.2,coverage==4.5.2,coveralls==1.5.1,docopt==0.6.2,filelock==3.0.10,flake8==3.6.0,Flask==1.0.2,Flask-OpenTracing==0.2.0,Flask-Script==2.0.6,Flask-SQLAlchemy==2.3.2,idna==2.7,inflection==0.3.1,isort==4.3.4,itsdangerous==1.1.0,jaeger-client==3.12.0,Jinja2==2.10,jsonschema==2.6.0,lazy-object-proxy==1.3.1,livereload==2.5.2,Markdown==3.0.1,MarkupSafe==1.1.0,mccabe==0.6.1,mkdocs==0.17.5,more-itertools==4.3.0,MS-avengers_api==0.1.0,nose==1.3.7,openapi-spec-validator==0.2.4,opentracing==1.3.0,pluggy==0.8.0,py==1.7.0,py-ms==0.1.1,pycodestyle==2.4.0,pyflakes==2.0.0,pylint==2.1.1,pytest==4.0.0,python-json-logger==0.1.10,PyYAML==3.13,requests==2.20.1,six==1.11.0,SQLAlchemy==1.2.14,swagger-ui-bundle==0.0.2,threadloop==1.0.2,thrift==0.11.0,toml==0.10.0,tornado==4.5.3,tox==3.5.3,typed-ast==1.1.0,urllib3==1.24.1,virtualenv==16.1.0,Werkzeug==0.14.1,wrapt==1.10.11
py36 run-test-pre: PYTHONHASHSEED='432109883'
py36 runtests: commands[0] | coverage run /home/nickfury/proyectos/microservicios/avengers_api/.tox/py36/bin/nosetests
....
----------------------------------------------------------------------
Ran 4 tests in 1.303s

OK
py35 create: /home/nickfury/proyectos/microservicios/avengers_api/.tox/py35
py35 installdeps: -r/home/nickfury/proyectos/microservicios/avengers_api/requirements-tests.txt
py35 inst: /home/nickfury/proyectos/microservicios/avengers_api/.tox/.tmp/package/1/MS-avengers_api-0.1.0.zip
py35 installed: anyconfig==0.9.7,astroid==2.0.4,atomicwrites==1.2.1,attrs==18.2.0,certifi==2018.10.15,chardet==3.0.4,Click==7.0,clickclick==1.2.2,connexion==2.0.2,coverage==4.5.2,coveralls==1.5.1,docopt==0.6.2,filelock==3.0.10,flake8==3.6.0,Flask==1.0.2,Flask-OpenTracing==0.2.0,Flask-Script==2.0.6,Flask-SQLAlchemy==2.3.2,idna==2.7,inflection==0.3.1,isort==4.3.4,itsdangerous==1.1.0,jaeger-client==3.12.0,Jinja2==2.10,jsonschema==2.6.0,lazy-object-proxy==1.3.1,livereload==2.5.2,Markdown==3.0.1,MarkupSafe==1.1.0,mccabe==0.6.1,mkdocs==0.17.5,more-itertools==4.3.0,MS-avengers_api==0.1.0,nose==1.3.7,openapi-spec-validator==0.2.4,opentracing==1.3.0,pathlib2==2.3.2,pluggy==0.8.0,py==1.7.0,py-ms==0.1.1,pycodestyle==2.4.0,pyflakes==2.0.0,pylint==2.1.1,pytest==4.0.0,python-json-logger==0.1.10,PyYAML==3.13,requests==2.20.1,six==1.11.0,SQLAlchemy==1.2.14,swagger-ui-bundle==0.0.2,threadloop==1.0.2,thrift==0.11.0,toml==0.10.0,tornado==4.5.3,tox==3.5.3,typed-ast==1.1.0,typing==3.6.6,urllib3==1.24.1,virtualenv==16.1.0,Werkzeug==0.14.1,wrapt==1.10.11
py35 run-test-pre: PYTHONHASHSEED='432109883'
py35 runtests: commands[0] | coverage run /home/nickfury/proyectos/microservicios/avengers_api/.tox/py35/bin/nosetests
....
----------------------------------------------------------------------
Ran 4 tests in 1.347s

OK
______________________________________________________________________________________________________________________________ summary ______________________________________________________________________________________________________________________________
  py36: commands succeeded
  py35: commands succeeded
  congratulations :)

```

### coverage
To use this Makefile to check code coverage quickly with the default Python.
```
$ make coverage

coverage erase
coverage run --source avengers_api -m pytest
Coverage.py warning: --include is ignored because --source is set (include-ignored)
================================================================================================ test session starts ================================================================================================
platform linux -- Python 3.5.2, pytest-4.0.0, py-1.7.0, pluggy-0.8.0
rootdir: /home/nickfury/proyectos/microservicios/avengers_api, inifile:
collected 4 items                                                                                                                                                                                                   

tests/test_views.py ....                                                                                                                                                                                      [100%]

============================================================================================= 4 passed in 1.19 seconds ==============================================================================================
coverage report -m
Name                              Stmts   Miss  Cover   Missing
---------------------------------------------------------------
avengers_api/__init__.py             13      2    85%   22-24
avengers_api/models/__init__.py       0      0   100%
avengers_api/models/init_db.py        2      0   100%
avengers_api/models/models.py        14      0   100%
avengers_api/views/__init__.py        1      0   100%
avengers_api/views/views.py          18      1    94%   34
---------------------------------------------------------------
TOTAL                                48      3    94%
coverage html
python -c "$BROWSER_PYSCRIPT" htmlcov/index.html

```

### dist
To use this Makefile to builds source and wheel package
```
$ make dist

rm -fr build/
rm -fr dist/
rm -fr .eggs/
rm -fr site/
find . -name '*.egg-info' -exec rm -fr {} +
find . -name '*.egg' -exec rm -f {} +
find . -name '*.pyc' -exec rm -f {} +
find . -name '*.pyo' -exec rm -f {} +
find . -name '*~' -exec rm -f {} +
find . -name '__pycache__' -exec rm -fr {} +
rm -fr .tox/
rm -f .coverage
rm -fr htmlcov/
rm -fr .pytest_cache
python setup.py sdist
running sdist
running egg_info
creating MS-avengers_api.egg-info
writing MS-avengers_api.egg-info/PKG-INFO
writing dependency_links to MS-avengers_api.egg-info/dependency_links.txt
writing top-level names to MS-avengers_api.egg-info/top_level.txt
writing manifest file 'MS-avengers_api.egg-info/SOURCES.txt'
reading manifest file 'MS-avengers_api.egg-info/SOURCES.txt'
writing manifest file 'MS-avengers_api.egg-info/SOURCES.txt'
running check
creating MS-avengers_api-0.1.0
creating MS-avengers_api-0.1.0/MS-avengers_api.egg-info
creating MS-avengers_api-0.1.0/avengers_api
creating MS-avengers_api-0.1.0/avengers_api/models
creating MS-avengers_api-0.1.0/avengers_api/views
creating MS-avengers_api-0.1.0/tests
copying files to MS-avengers_api-0.1.0...
copying README.md -> MS-avengers_api-0.1.0
copying setup.py -> MS-avengers_api-0.1.0
copying MS-avengers_api.egg-info/PKG-INFO -> MS-avengers_api-0.1.0/MS-avengers_api.egg-info
copying MS-avengers_api.egg-info/SOURCES.txt -> MS-avengers_api-0.1.0/MS-avengers_api.egg-info
copying MS-avengers_api.egg-info/dependency_links.txt -> MS-avengers_api-0.1.0/MS-avengers_api.egg-info
copying MS-avengers_api.egg-info/top_level.txt -> MS-avengers_api-0.1.0/MS-avengers_api.egg-info
copying avengers_api/__init__.py -> MS-avengers_api-0.1.0/avengers_api
copying avengers_api/models/__init__.py -> MS-avengers_api-0.1.0/avengers_api/models
copying avengers_api/models/init_db.py -> MS-avengers_api-0.1.0/avengers_api/models
copying avengers_api/models/models.py -> MS-avengers_api-0.1.0/avengers_api/models
copying avengers_api/views/__init__.py -> MS-avengers_api-0.1.0/avengers_api/views
copying avengers_api/views/views.py -> MS-avengers_api-0.1.0/avengers_api/views
copying tests/__init__.py -> MS-avengers_api-0.1.0/tests
copying tests/test_views.py -> MS-avengers_api-0.1.0/tests
Writing MS-avengers_api-0.1.0/setup.cfg
creating dist
Creating tar archive
removing 'MS-avengers_api-0.1.0' (and everything under it)
python setup.py bdist_wheel
running bdist_wheel
running build
running build_py
creating build
creating build/lib
creating build/lib/avengers_api
copying avengers_api/__init__.py -> build/lib/avengers_api
creating build/lib/tests
copying tests/__init__.py -> build/lib/tests
copying tests/test_views.py -> build/lib/tests
creating build/lib/avengers_api/models
copying avengers_api/models/__init__.py -> build/lib/avengers_api/models
copying avengers_api/models/init_db.py -> build/lib/avengers_api/models
copying avengers_api/models/models.py -> build/lib/avengers_api/models
creating build/lib/avengers_api/views
copying avengers_api/views/__init__.py -> build/lib/avengers_api/views
copying avengers_api/views/views.py -> build/lib/avengers_api/views
running egg_info
writing dependency_links to MS-avengers_api.egg-info/dependency_links.txt
writing MS-avengers_api.egg-info/PKG-INFO
writing top-level names to MS-avengers_api.egg-info/top_level.txt
reading manifest file 'MS-avengers_api.egg-info/SOURCES.txt'
writing manifest file 'MS-avengers_api.egg-info/SOURCES.txt'
installing to build/bdist.linux-x86_64/wheel
running install
running install_lib
creating build/bdist.linux-x86_64
creating build/bdist.linux-x86_64/wheel
creating build/bdist.linux-x86_64/wheel/avengers_api
creating build/bdist.linux-x86_64/wheel/avengers_api/models
copying build/lib/avengers_api/models/__init__.py -> build/bdist.linux-x86_64/wheel/avengers_api/models
copying build/lib/avengers_api/models/init_db.py -> build/bdist.linux-x86_64/wheel/avengers_api/models
copying build/lib/avengers_api/models/models.py -> build/bdist.linux-x86_64/wheel/avengers_api/models
copying build/lib/avengers_api/__init__.py -> build/bdist.linux-x86_64/wheel/avengers_api
creating build/bdist.linux-x86_64/wheel/avengers_api/views
copying build/lib/avengers_api/views/__init__.py -> build/bdist.linux-x86_64/wheel/avengers_api/views
copying build/lib/avengers_api/views/views.py -> build/bdist.linux-x86_64/wheel/avengers_api/views
creating build/bdist.linux-x86_64/wheel/tests
copying build/lib/tests/__init__.py -> build/bdist.linux-x86_64/wheel/tests
copying build/lib/tests/test_views.py -> build/bdist.linux-x86_64/wheel/tests
running install_egg_info
Copying MS-avengers_api.egg-info to build/bdist.linux-x86_64/wheel/MS-avengers_api-0.1.0-py3.5.egg-info
running install_scripts
adding license file "AUTHORS" (matched pattern "AUTHORS*")
creating build/bdist.linux-x86_64/wheel/MS-avengers_api-0.1.0.dist-info/WHEEL
creating 'dist/MS-avengers_api-0.1.0-py3-none-any.whl' and adding 'build/bdist.linux-x86_64/wheel' to it
adding 'avengers_api/__init__.py'
adding 'avengers_api/models/__init__.py'
adding 'avengers_api/models/init_db.py'
adding 'avengers_api/models/models.py'
adding 'avengers_api/views/__init__.py'
adding 'avengers_api/views/views.py'
adding 'tests/__init__.py'
adding 'tests/test_views.py'
adding 'MS-avengers_api-0.1.0.dist-info/AUTHORS'
adding 'MS-avengers_api-0.1.0.dist-info/METADATA'
adding 'MS-avengers_api-0.1.0.dist-info/WHEEL'
adding 'MS-avengers_api-0.1.0.dist-info/top_level.txt'
adding 'MS-avengers_api-0.1.0.dist-info/RECORD'
removing build/bdist.linux-x86_64/wheel
ls -l dist
total 12
-rw-rw-r-- 1 nickfury nickfury 4937 nov 20 11:31 MS-avengers_api-0.1.0-py3-none-any.whl
-rw-rw-r-- 1 nickfury nickfury 3462 nov 20 11:31 MS-avengers_api-0.1.0.tar.gz

```

### release
To use this Makefile to package and upload a release to pypi repository.
```
$ make release

rm -fr build/
rm -fr dist/
rm -fr .eggs/
rm -fr site/
find . -name '*.egg-info' -exec rm -fr {} +
find . -name '*.egg' -exec rm -f {} +
find . -name '*.pyc' -exec rm -f {} +
find . -name '*.pyo' -exec rm -f {} +
find . -name '*~' -exec rm -f {} +
find . -name '__pycache__' -exec rm -fr {} +
rm -fr .tox/
rm -f .coverage
rm -fr htmlcov/
rm -fr .pytest_cache
python setup.py sdist
running sdist
running egg_info
creating MS-avengers_api.egg-info
writing dependency_links to MS-avengers_api.egg-info/dependency_links.txt
writing top-level names to MS-avengers_api.egg-info/top_level.txt
writing MS-avengers_api.egg-info/PKG-INFO
writing manifest file 'MS-avengers_api.egg-info/SOURCES.txt'
reading manifest file 'MS-avengers_api.egg-info/SOURCES.txt'
writing manifest file 'MS-avengers_api.egg-info/SOURCES.txt'
running check
creating MS-avengers_api-0.1.0
creating MS-avengers_api-0.1.0/MS-avengers_api.egg-info
creating MS-avengers_api-0.1.0/avengers_api
creating MS-avengers_api-0.1.0/avengers_api/models
creating MS-avengers_api-0.1.0/avengers_api/views
creating MS-avengers_api-0.1.0/tests
copying files to MS-avengers_api-0.1.0...
copying README.md -> MS-avengers_api-0.1.0
copying setup.py -> MS-avengers_api-0.1.0
copying MS-avengers_api.egg-info/PKG-INFO -> MS-avengers_api-0.1.0/MS-avengers_api.egg-info
copying MS-avengers_api.egg-info/SOURCES.txt -> MS-avengers_api-0.1.0/MS-avengers_api.egg-info
copying MS-avengers_api.egg-info/dependency_links.txt -> MS-avengers_api-0.1.0/MS-avengers_api.egg-info
copying MS-avengers_api.egg-info/top_level.txt -> MS-avengers_api-0.1.0/MS-avengers_api.egg-info
copying avengers_api/__init__.py -> MS-avengers_api-0.1.0/avengers_api
copying avengers_api/models/__init__.py -> MS-avengers_api-0.1.0/avengers_api/models
copying avengers_api/models/init_db.py -> MS-avengers_api-0.1.0/avengers_api/models
copying avengers_api/models/models.py -> MS-avengers_api-0.1.0/avengers_api/models
copying avengers_api/views/__init__.py -> MS-avengers_api-0.1.0/avengers_api/views
copying avengers_api/views/views.py -> MS-avengers_api-0.1.0/avengers_api/views
copying tests/__init__.py -> MS-avengers_api-0.1.0/tests
copying tests/test_views.py -> MS-avengers_api-0.1.0/tests
Writing MS-avengers_api-0.1.0/setup.cfg
creating dist
Creating tar archive
removing 'MS-avengers_api-0.1.0' (and everything under it)
python setup.py bdist_wheel
running bdist_wheel
running build
running build_py
creating build
creating build/lib
creating build/lib/avengers_api
copying avengers_api/__init__.py -> build/lib/avengers_api
creating build/lib/tests
copying tests/__init__.py -> build/lib/tests
copying tests/test_views.py -> build/lib/tests
creating build/lib/avengers_api/models
copying avengers_api/models/__init__.py -> build/lib/avengers_api/models
copying avengers_api/models/init_db.py -> build/lib/avengers_api/models
copying avengers_api/models/models.py -> build/lib/avengers_api/models
creating build/lib/avengers_api/views
copying avengers_api/views/__init__.py -> build/lib/avengers_api/views
copying avengers_api/views/views.py -> build/lib/avengers_api/views
running egg_info
writing top-level names to MS-avengers_api.egg-info/top_level.txt
writing MS-avengers_api.egg-info/PKG-INFO
writing dependency_links to MS-avengers_api.egg-info/dependency_links.txt
reading manifest file 'MS-avengers_api.egg-info/SOURCES.txt'
writing manifest file 'MS-avengers_api.egg-info/SOURCES.txt'
installing to build/bdist.linux-x86_64/wheel
running install
running install_lib
creating build/bdist.linux-x86_64
creating build/bdist.linux-x86_64/wheel
creating build/bdist.linux-x86_64/wheel/avengers_api
creating build/bdist.linux-x86_64/wheel/avengers_api/models
copying build/lib/avengers_api/models/__init__.py -> build/bdist.linux-x86_64/wheel/avengers_api/models
copying build/lib/avengers_api/models/init_db.py -> build/bdist.linux-x86_64/wheel/avengers_api/models
copying build/lib/avengers_api/models/models.py -> build/bdist.linux-x86_64/wheel/avengers_api/models
copying build/lib/avengers_api/__init__.py -> build/bdist.linux-x86_64/wheel/avengers_api
creating build/bdist.linux-x86_64/wheel/avengers_api/views
copying build/lib/avengers_api/views/__init__.py -> build/bdist.linux-x86_64/wheel/avengers_api/views
copying build/lib/avengers_api/views/views.py -> build/bdist.linux-x86_64/wheel/avengers_api/views
creating build/bdist.linux-x86_64/wheel/tests
copying build/lib/tests/__init__.py -> build/bdist.linux-x86_64/wheel/tests
copying build/lib/tests/test_views.py -> build/bdist.linux-x86_64/wheel/tests
running install_egg_info
Copying MS-avengers_api.egg-info to build/bdist.linux-x86_64/wheel/MS-avengers_api-0.1.0-py3.5.egg-info
running install_scripts
adding license file "AUTHORS" (matched pattern "AUTHORS*")
creating build/bdist.linux-x86_64/wheel/MS-avengers_api-0.1.0.dist-info/WHEEL
creating 'dist/MS-avengers_api-0.1.0-py3-none-any.whl' and adding 'build/bdist.linux-x86_64/wheel' to it
adding 'avengers_api/__init__.py'
adding 'avengers_api/models/__init__.py'
adding 'avengers_api/models/init_db.py'
adding 'avengers_api/models/models.py'
adding 'avengers_api/views/__init__.py'
adding 'avengers_api/views/views.py'
adding 'tests/__init__.py'
adding 'tests/test_views.py'
adding 'MS-avengers_api-0.1.0.dist-info/AUTHORS'
adding 'MS-avengers_api-0.1.0.dist-info/METADATA'
adding 'MS-avengers_api-0.1.0.dist-info/WHEEL'
adding 'MS-avengers_api-0.1.0.dist-info/top_level.txt'
adding 'MS-avengers_api-0.1.0.dist-info/RECORD'
removing build/bdist.linux-x86_64/wheel
ls -l dist
total 12
-rw-rw-r-- 1 nickfury nickfury 4937 nov 20 11:50 MS-avengers_api-0.1.0-py3-none-any.whl
-rw-rw-r-- 1 nickfury nickfury 3467 nov 20 11:50 MS-avengers_api-0.1.0.tar.gz
twine upload --repository-url http://nexus3.avengers.com/repository/pypi-internal/ dist/*
Enter your username: nickfury
Enter your password: **********************

```

### servedocs
To use this Makefile to compile the docs watching for changes.
```
$ make servedocs

mkdocs build
INFO    -  Cleaning site directory 
INFO    -  Building documentation to directory: /home/nickfury/proyectos/microservicios/avengers_api/site 
mkdocs serve
INFO    -  Building documentation... 
INFO    -  Cleaning site directory 
[I 181120 10:45:16 server:292] Serving on http://127.0.0.1:8000
[I 181120 10:45:16 handlers:59] Start watching changes
[I 181120 10:45:16 handlers:61] Start detecting changes

```

### docs
To use this Makefile to generate Mkdocs HTML documentation, including API docs.
```
$ make docs

mkdocs build
INFO    -  Cleaning site directory 
INFO    -  Building documentation to directory: /home/nickfury/proyectos/microservicios/avengers_api/site 

```

### install
To use this Makefile to install the package to the active Python's site-packages.
```
$ make install

rm -fr build/
rm -fr dist/
rm -fr .eggs/
rm -fr site/
find . -name '*.egg-info' -exec rm -fr {} +
find . -name '*.egg' -exec rm -f {} +
find . -name '*.pyc' -exec rm -f {} +
find . -name '*.pyo' -exec rm -f {} +
find . -name '*~' -exec rm -f {} +
find . -name '__pycache__' -exec rm -fr {} +
rm -fr .tox/
rm -f .coverage
rm -fr htmlcov/
rm -fr .pytest_cache
python setup.py install
running install
running bdist_egg
running egg_info
creating MS-avengers_api.egg-info
writing MS-avengers_api.egg-info/PKG-INFO
writing dependency_links to MS-avengers_api.egg-info/dependency_links.txt
writing top-level names to MS-avengers_api.egg-info/top_level.txt
writing manifest file 'MS-avengers_api.egg-info/SOURCES.txt'
reading manifest file 'MS-avengers_api.egg-info/SOURCES.txt'
writing manifest file 'MS-avengers_api.egg-info/SOURCES.txt'
installing library code to build/bdist.linux-x86_64/egg
running install_lib
running build_py
creating build
creating build/lib
creating build/lib/avengers_api
copying avengers_api/__init__.py -> build/lib/avengers_api
creating build/lib/tests
copying tests/__init__.py -> build/lib/tests
copying tests/test_views.py -> build/lib/tests
creating build/lib/avengers_api/models
copying avengers_api/models/__init__.py -> build/lib/avengers_api/models
copying avengers_api/models/init_db.py -> build/lib/avengers_api/models
copying avengers_api/models/models.py -> build/lib/avengers_api/models
creating build/lib/avengers_api/views
copying avengers_api/views/__init__.py -> build/lib/avengers_api/views
copying avengers_api/views/views.py -> build/lib/avengers_api/views
creating build/bdist.linux-x86_64
creating build/bdist.linux-x86_64/egg
creating build/bdist.linux-x86_64/egg/avengers_api
creating build/bdist.linux-x86_64/egg/avengers_api/models
copying build/lib/avengers_api/models/__init__.py -> build/bdist.linux-x86_64/egg/avengers_api/models
copying build/lib/avengers_api/models/init_db.py -> build/bdist.linux-x86_64/egg/avengers_api/models
copying build/lib/avengers_api/models/models.py -> build/bdist.linux-x86_64/egg/avengers_api/models
copying build/lib/avengers_api/__init__.py -> build/bdist.linux-x86_64/egg/avengers_api
creating build/bdist.linux-x86_64/egg/avengers_api/views
copying build/lib/avengers_api/views/__init__.py -> build/bdist.linux-x86_64/egg/avengers_api/views
copying build/lib/avengers_api/views/views.py -> build/bdist.linux-x86_64/egg/avengers_api/views
creating build/bdist.linux-x86_64/egg/tests
copying build/lib/tests/__init__.py -> build/bdist.linux-x86_64/egg/tests
copying build/lib/tests/test_views.py -> build/bdist.linux-x86_64/egg/tests
byte-compiling build/bdist.linux-x86_64/egg/avengers_api/models/__init__.py to __init__.cpython-35.pyc
byte-compiling build/bdist.linux-x86_64/egg/avengers_api/models/init_db.py to init_db.cpython-35.pyc
byte-compiling build/bdist.linux-x86_64/egg/avengers_api/models/models.py to models.cpython-35.pyc
byte-compiling build/bdist.linux-x86_64/egg/avengers_api/__init__.py to __init__.cpython-35.pyc
byte-compiling build/bdist.linux-x86_64/egg/avengers_api/views/__init__.py to __init__.cpython-35.pyc
byte-compiling build/bdist.linux-x86_64/egg/avengers_api/views/views.py to views.cpython-35.pyc
byte-compiling build/bdist.linux-x86_64/egg/tests/__init__.py to __init__.cpython-35.pyc
byte-compiling build/bdist.linux-x86_64/egg/tests/test_views.py to test_views.cpython-35.pyc
creating build/bdist.linux-x86_64/egg/EGG-INFO
copying MS-avengers_api.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
copying MS-avengers_api.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying MS-avengers_api.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying MS-avengers_api.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
zip_safe flag not set; analyzing archive contents...
avengers_api.__pycache__.__init__.cpython-35: module references __file__
tests.__pycache__.test_views.cpython-35: module references __file__
creating dist
creating 'dist/MS-avengers_api-0.1.0-py3.5.egg' and adding 'build/bdist.linux-x86_64/egg' to it
removing 'build/bdist.linux-x86_64/egg' (and everything under it)
Processing MS-avengers_api-0.1.0-py3.5.egg
creating /home/nickfury/.virtualenvs/tmp-20eb965128020af/lib/python3.5/site-packages/MS-avengers_api-0.1.0-py3.5.egg
Extracting MS-avengers_api-0.1.0-py3.5.egg to /home/nickfury/.virtualenvs/tmp-20eb965128020af/lib/python3.5/site-packages
Adding MS-avengers_api 0.1.0 to easy-install.pth file

Installed /home/nickfury/.virtualenvs/tmp-20eb965128020af/lib/python3.5/site-packages/MS-avengers_api-0.1.0-py3.5.egg
Processing dependencies for MS-avengers_api==0.1.0
Finished processing dependencies for MS-avengers_api==0.1.0


```

