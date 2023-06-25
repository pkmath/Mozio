# -*- coding: utf-8 -*-
import sys
import os
from dotenv import load_dotenv
import unittest

load_dotenv()

API_KEY = os.getenv('API_KEY')
HOME_PATH = os.getenv('HOME_PATH')
sys.path.append(HOME_PATH)

import app

class ControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.payload = {
            "start_address": "44 Tehama Street, San Francisco, CA, USA",
            "end_address": "65 Tehama Street, San Francisco, CA, USA",
            "pickup_datetime": "2023-12-05 15:30",
            "mode": "one_way",
            "num_passengers": 2,
            "currency": "USD",
            "campaign": "pk"
        }
        self.headers = {
            "Api-Key": API_KEY
        }

        self.search_id = ''

        self.payload2 = {
            'search_id': "",
            'result_id': "",
            'email': "",
            'phone_number': "",
            'first_name': "",
            'last_name': ""
        }

    def test_search_endpoint(self):
        response = self.client.post(
            '/v2/search/',
            headers=self.headers,
            json=self.payload)
        self.assertEqual(response.status_code, 200)

    def test_search_poll_endpoint(self):
        response = self.client.get(
            '/v2/search/123456789/poll/',
            headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_reservation_endpoint(self):
        response = self.client.post(
            '/v2/reservations/',
            headers=self.headers,
            json=self.payload2)
        self.assertEqual(response.status_code, 200)

    def test_reservation_poll_endpoint(self):
        response = self.client.get(
            '/v2/reservations/65ab89cfcb6640f492766db721a82ed8/poll/',
            headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_delete_endpoint(self):
        response = self.client.delete(
            '/v2/reservations/9880cf9681da4c119da7dc4032307b66/',
            headers=self.headers)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
