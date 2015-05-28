# coding:utf-8
import os
import logging
import unittest

from pagarme.api import PagarmeApi
from pagarme.config import __endpoint__, __user_agent__
from pagarme.exceptions import NullAPIKeyError

# logging
logging.basicConfig(level=logging.INFO)


class ApiTest(unittest.TestCase):
    def setUp(self):
        self.api = PagarmeApi(endpoint=__endpoint__, api_key=os.environ['PAGARME_API_KEY'])

    def test_default_headers(self):
        self.assertIsInstance(self.api.default_headers, dict)
        self.assertIn('Content-Type', self.api.default_headers)
        self.assertIn('Accept', self.api.default_headers)
        self.assertIn('User-Agent', self.api.default_headers)

    def test_api_key_required(self):
        with self.assertRaises(NullAPIKeyError) as e:
            api = PagarmeApi(endpoint=__endpoint__)

    def test_default_endpoint(self):
        self.assertEqual(__endpoint__, self.api.default_endpoint)

    def test_default_user_agent(self):
        self.assertEqual(__user_agent__, self.api.default_user_agent)

    def test_api_get(self):
        response = self.api.get('/plans')
        self.assertGreater(len(response), 0)

    def test_api_post(self):
        plan = {
            'amount': '4990',
            'days': '30',
            'name': 'basic',
        }
        plan = self.api.post('/plans', data=plan)
        self.assertNotIn('errors', plan)

    def test_api_put(self):
        plan = {
            'amount': '4990',
            'days': '30',
            'name': 'intermediat',
        }
        plan = self.api.post('/plans', data=plan)
        name = {'name': 'intermediate'}
        plan = self.api.put('/plans/%s' % plan['id'], data=name)
        self.assertEqual('intermediate', name['name'])

    def test_api_bad_request(self):
        response = self.api.post('/plans')
        self.assertNotEqual(response.get('errors'), None)
