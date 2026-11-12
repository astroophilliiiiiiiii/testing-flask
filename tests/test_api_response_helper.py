import pytest

from flask.helpers import format_api_response


def test_default_response():
    payload = {'key': 'value'}
    resp = format_api_response(data=payload)
    assert resp == {'data': payload, 'status': 200, 'message': 'OK'}


def test_custom_status_and_message():
    payload = [1, 2, 3]
    resp = format_api_response(data=payload, status_code=404, message='Not Found')
    assert resp == {'data': payload, 'status': 404, 'message': 'Not Found'}


def test_none_data_defaults():
    resp = format_api_response()
    assert resp['data'] is None
    assert resp['status'] == 200
    assert resp['message'] == 'OK'
