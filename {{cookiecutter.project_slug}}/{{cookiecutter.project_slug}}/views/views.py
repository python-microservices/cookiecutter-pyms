# encoding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

{% if cookiecutter.create_model_class == 'n' -%}
import json
{% endif %}

import connexion
from flask import jsonify, current_app

{% if cookiecutter.create_model_class == 'y' -%}
from {{cookiecutter.project_slug}}.models.init_db import db
from {{cookiecutter.project_slug}}.models.models import {{cookiecutter.model_name}}
{% endif %}


{% if cookiecutter.create_model_class == 'y' -%}
def list_view():
    """Example endpoint return a list of {{cookiecutter.table_name}} by palette
    """
    current_app.logger.info("Return all {{cookiecutter.table_name}} list")
    query = {{cookiecutter.model_name}}.query.all()

    return jsonify([i.serialize for i in query])


def create_view():
    """Example endpoint return create a {{cookiecutter.table_name}}
    """
    current_app.logger.info("Create {{cookiecutter.table_name}}")
    if connexion.request.is_json:
        data = connexion.request.get_json()
        my_obj = {{cookiecutter.model_name}}(name=data["name"])
        db.session.add(my_obj)
        db.session.commit()

        return jsonify({{cookiecutter.table_name}}.serialize)
    return jsonify({})
{% else %}
def dummy_view():
    """
    Example endpoint return a simple json
    """
    current_app.logger.info("Return a simple json")
    dummy_json = {'msg': "Hello "}
    return json.dumps(dummy_json)
{% endif %}
