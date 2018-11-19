# Configuration

The project is configured in `{{cookiecutter.project_slug}}/config.yml`. You must set the project name `APP_NAME` and the path prefix
of the project `APPLICATION_ROOT`. This constants is defined in the class Config:

```
class Config:
    DEBUG = False
    TESTING = False
    APP_NAME = "Template"
    APPLICATION_ROOT = "/template"
```

It's also important to check `setup.py`. 
