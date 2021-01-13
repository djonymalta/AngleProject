import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "harmo.settings")

import django
django.setup()

from django.core.management import call_command


import unittest
from django.test import Client


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_must_know_returns_status_code_equal_200(self):
        # Issue a GET request.
        response = self.client.get('http://localhost:8000/v1/rest/clock/9/0/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_must_return_result_of_calc_angle(self):
        # Issue a GET request.
        response = self.client.get('http://localhost:8000/v1/rest/clock/3/0/')

        # Expect Angle to equal angle_calc.
        self.assertEqual(response.json()['angle'], f'{90.0}')
