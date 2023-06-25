# -*- coding: utf-8 -*-


import requests
from dotenv import load_dotenv
import os


load_dotenv()
SEARCH_API_URL = os.getenv('SEARCH_API_URL')
RESERVATION_API_URL = os.getenv('RESERVATION_API_URL')


def search(
        api_key,
        payload):

    headers = {
        "Api-Key": api_key
    }

    payload = payload
    return requests.post(SEARCH_API_URL, headers=headers, json=payload)


def search_poll(search_id, api_key):

    SEARCH_POLL_API_URL = 'https://api-testing.mozio.com/v2/search/%s/poll' % (
        search_id)

    headers = {
        "Api-Key": api_key
    }

    return requests.get(SEARCH_POLL_API_URL, headers=headers)


def reservation(
        api_key,
        payload):

    headers = {
        "Api-Key": api_key
    }

    # airline & flight_number required only when airport location included in
    # search request. Next statement change payload according to when airline
    # and flight_number provided.

    payload = payload

    return requests.post(RESERVATION_API_URL, headers=headers, json=payload)


def reservation_poll(search_id, api_key):

    RESERVATION_POLL_API_URL = 'https://api-testing.mozio.com/v2/reservations/%s/poll/' % (
        search_id)

    headers = {
        "Api-Key": api_key
    }

    return requests.get(RESERVATION_POLL_API_URL, headers=headers)


def delete_reservation(hashed_id, api_key):

    DELETE_RESERVATION_API_URL = 'https://api-testing.mozio.com/v2/reservations/%s/' % (
        hashed_id)

    headers = {
        "Api-Key": api_key
    }

    return requests.delete(DELETE_RESERVATION_API_URL, headers=headers)
