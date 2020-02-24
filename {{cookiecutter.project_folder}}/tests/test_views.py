import json
import os
import unittest
from project.app import MyMicroservice
from pyms.constants import CONFIGMAP_FILE_ENVIRONMENT
from typing import Dict, List, Union, Text


class ProjectTestCase(unittest.TestCase):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    def setUp(self):
        os.environ[CONFIGMAP_FILE_ENVIRONMENT] = os.path.join(self.BASE_DIR, "config-tests.yml")
        ms = MyMicroservice(path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "project", "test_views.py"))
        self.app = ms.create_app()
        self.base_url = self.app.config["APPLICATION_ROOT"]
        self.client = self.app.test_client()

    def tearDown(self):
        pass  # os.unlink(self.app.config['DATABASE'])

    {%- if cookiecutter.application_root != '/' %}
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(404, response.status_code)
    {% endif -%}
    
    def test_healthcheck(self):
        response = self.client.get('/healthcheck')
        self.assertEqual(200, response.status_code)

    def test_list_view(self):
        {%- if cookiecutter.application_root != '/' %}
        response = self.client.get('{{ cookiecutter.application_root }}/')
        {%- elif cookiecutter.application_root == '/' %}
        response = self.client.get('/')
        {% endif %}
        self.assertEqual(200, response.status_code)

    def test_create_view(self):
        name = "blue"
        {% if cookiecutter.application_root != '/' -%}
        response = self.client.post('{{ cookiecutter.application_root }}/',
        {%- elif cookiecutter.application_root == '/' %}
        response = self.client.post('/',
        {% endif %}
                                    data=json.dumps(dict(name=name)),
                                    content_type='application/json'
                                    )
        self.assertEqual(200, response.status_code)
