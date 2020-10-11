#!/usr/bin/env python

import os
import shutil


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(path: str) -> None:
    shutil.rmtree(path)


if __name__ == '__main__':

    if '{{ cookiecutter.microservice_with_swagger_and_connexion }}' != 'y':
        remove_dir('project/swagger')

    if '{{ cookiecutter.create_model_class }}' != 'y':
        remove_dir('project/models')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        if os.path.exists('LICENSE'):
            remove_file('LICENSE')
