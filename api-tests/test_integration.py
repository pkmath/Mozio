# -*- coding: utf-8 -*-


import requests
import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv()

BASE_URL = os.getenv('BASE_URL')
API_KEY = os.getenv('API_KEY')


class MozioApiTest:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            "Api-Key": API_KEY
        }

    def test_search_endpoint(self):
        search_payload = {
            "start_address": "44 Tehama Street, San Francisco, CA, USA",
            "end_address": "SFO",
            "mode": "one_way",
            "pickup_datetime": "2023-12-01 15:30",
            "num_passengers": 2,
            "currency": "USD",
            "campaign": "Panagiotis Karathymios"
        }

        search_response = requests.post(
            BASE_URL + '/v2/search/',
            headers=self.headers,
            json=search_payload)
        search_id = search_response.json()['search_id']
        return search_id

    def test_search_poll_endpoint(self, search_id):
        SEARCH_POLL_API_URL = BASE_URL + '/v2/search/%s/poll' % (search_id)

        search_poll_response = requests.get(
            SEARCH_POLL_API_URL, headers=self.headers)
        search_poll_data = search_poll_response.json()

        results = search_poll_data['results']
        results_data = pd.DataFrame(
            columns=[
                "provider_name",
                "price",
                "result_id"])

        for i in results:
            y = i['steps'][0]
            provider_name = y['details']['provider_name']
            price = float(y['details']['price']['price']['value'])
            result_id = i['result_id']
            results_data.loc[len(results_data.index)] = [
                provider_name, price, result_id]

        results_data = results_data[results_data['provider_name']
                                    == 'Dummy External Provider']
        results_data = results_data.reset_index(drop=True)
        result_id = results_data.loc[results_data['price'].idxmin(
        )]['result_id']

        return result_id

    def test_reservation_endpoint(self, search_id, result_id):
        # airline & flight_number added as the destination (SFO) is airport
        # and according to Mozio API Guide it is required
        reservation_payload = {
            'search_id': search_id,
            'result_id': result_id,
            'email': 'pkarathymios@gmail.com',
            'phone_number': '+306945047253',
            'first_name': 'Panagiotis',
            'last_name': 'Karathymios',
            'airline': 'AA',
            'flight_number': '123'
        }

        reservation_response = requests.post(
            BASE_URL + '/v2/reservations/',
            headers=self.headers,
            json=reservation_payload)
        reservation_results = reservation_response.json()

    def test_reservation_poll_endpoint(self, search_id):
        RESERVATION_POLL_API_URL = BASE_URL + \
            '/v2/reservations/%s/poll/' % (search_id)
        reservation_poll_response = requests.get(
            RESERVATION_POLL_API_URL, headers=self.headers)

        reservation_poll_resutls = reservation_poll_response.json()
        confirmation_number = reservation_poll_resutls['reservations'][0]['confirmation_number']
        hashed_id = reservation_poll_resutls['reservations'][0]['id']

        return hashed_id, confirmation_number

    def test_delete_endpoint(self, hashed_id):
        DELETE_RESERVATION_API_URL = BASE_URL + \
            '/v2/reservations/%s/' % (hashed_id)

        delete_response = requests.delete(
            DELETE_RESERVATION_API_URL, headers=self.headers)
        delete_resutls = delete_response.json()


# Instantiate the test class
test = MozioApiTest()

# Run the tests

# get the search id
search_id = test.test_search_endpoint()
# get result id according to assessment instructions
result_id = test.test_search_poll_endpoint(search_id)
# make the booking
test.test_reservation_endpoint(search_id, result_id)
# get the hashed id and confirmation number of booking
hashed_id, confirmation_number = test.test_reservation_poll_endpoint(search_id)
# cancel the booking
test.test_delete_endpoint(hashed_id)

# print the confirmation number
print('Confirmation number: ' + confirmation_number)
