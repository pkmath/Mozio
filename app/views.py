# -*- coding: utf-8 -*-


from flask import jsonify, request
from app import app
from app.external_api import search, search_poll, reservation, reservation_poll, delete_reservation


@app.route('/v2/search/', methods=['POST'])
def search_endpoint():
    # search parameters
    api_key = request.headers['Api-Key']
    payload = request.json

    try:
        # Send api-key & search terms to external API to get search_id
        search_response = search(
            api_key,
            payload)

        if search_response.status_code == 403:
            return jsonify({'message': search_response.json()['user_message']})
        elif search_response.status_code == 400:
            return jsonify(search_response.json())
        else:
            search_id = search_response.json()  # ['search_id']

        return search_id

    except Exception as e:
        return jsonify(
            {'message': 'Error occurred during API communication', 'error': str(e)}), 500


@app.route('/v2/search/<search_id>/poll/', methods=['GET'])
def search_poll_endpoint(search_id):

    api_key = request.headers['Api-Key']

    try:

        search_poll_response = search_poll(search_id, api_key)

        if search_poll_response.status_code == 403:
            return jsonify(search_poll_response.json())
        elif search_poll_response.status_code == 400:
            return jsonify(search_poll_response.json())
        else:
            search_resutls = search_poll_response.json()

        return search_resutls

    except Exception as e:
        return jsonify(
            {'message': 'Error occurred during API communication', 'error': str(e)}), 500


@app.route('/v2/reservations/', methods=['POST'])
def reservation_endpoint():
    # reservation parameters
    api_key = request.headers['Api-Key']
    payload = request.json

    try:
        # Send api-key & reservation terms to external API
        reservation_response = reservation(
            api_key,
            payload)

        if reservation_response.status_code == 403:
            return jsonify(reservation_response.json())
        elif reservation_response.status_code == 400:
            return jsonify(reservation_response.json())
        else:
            reservation_results = reservation_response.json()

        return reservation_results

    except Exception as e:
        return jsonify(
            {'message': 'Error occurred during API communication', 'error': str(e)}), 500


@app.route('/v2/reservations/<search_id>/poll/', methods=['GET'])
def reservation_poll_endpoint(search_id):

    api_key = request.headers['Api-Key']

    try:

        reservation_poll_response = reservation_poll(search_id, api_key)

        if reservation_poll_response.status_code == 403:
            return jsonify(reservation_poll_response.json())
        elif reservation_poll_response.status_code == 400:
            return jsonify(reservation_poll_response.json())
        else:
            reservation_resutls = reservation_poll_response.json()

        return reservation_resutls

    except Exception as e:
        return jsonify(
            {'message': 'Error occurred during API communication', 'error': str(e)}), 500


@app.route('/v2/reservations/<hashed_id>/', methods=['DELETE'])
def delete_endpoint(hashed_id):

    api_key = request.headers['Api-Key']

    try:

        delete_response = delete_reservation(hashed_id, api_key)

        if delete_response.status_code == 403:
            return jsonify(delete_response.json())
        elif delete_response.status_code == 400:
            return jsonify(delete_response.json())
        else:
            delete_resutls = delete_response.json()

        return delete_resutls

    except Exception as e:
        return jsonify(
            {'message': 'Error occurred during API communication', 'error': str(e)}), 500
