#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(path):
    shutil.rmtree(path)


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        if os.path.exists('AUTHORS.rst'):
            remove_file('AUTHORS.rst')

    if '{{ cookiecutter.create_model_class }}' != 'y':
        remove_dir('{{ cookiecutter.project_slug }}/models')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        if os.path.exists('LICENSE'):
            remove_file('LICENSE')
