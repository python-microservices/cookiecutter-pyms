# -*- coding: utf-8 -*-
# Copyright (c) 2018 by Alberto Vara <a.vara.1986@gmail.com>
import codecs
import os

from setuptools import setup, find_packages

version = __import__('{{cookiecutter.project_slug}}').__version__
author = __import__('{{cookiecutter.project_slug}}').__author__
author_email = __import__('{{cookiecutter.project_slug}}').__email__

if os.path.exists('README.rst'):
    long_description = codecs.open('README.rst', 'r', 'utf-8').read()
else:
    long_description = '{{cookiecutter.project_short_description}}'

setup(
    name="MS-{{cookiecutter.project_slug}}",
    version=version,
    author=author,
    author_email=author_email,
    description="Python Miscroservice barebone",
    long_description=long_description,
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
    python_requires='>=3.5',
    license="GPLv3",
    platforms=["any"],
    keywords="python, microservices",
    url='{{cookiecutter.project_repo_url}}',
    test_suite='nose.collector',
    packages=find_packages(),
    include_package_data=True,
)