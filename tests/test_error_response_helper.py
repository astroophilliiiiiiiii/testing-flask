import pytest

from flask.helpers import format_error_response


def test_default_status_and_no_details():
    result = format_error_response('Bad request')
    assert result == {
        'error': 'Bad request',
        'status': 400,
        'details': None,
    }


def test_custom_status_codes():
    result_404 = format_error_response('Not found', status_code=404)
    assert result_404['status'] == 404
    assert result_404['error'] == 'Not found'

    result_500 = format_error_response('Server error', status_code=500)
    assert result_500['status'] == 500
    assert result_500['error'] == 'Server error'


def test_details_parameter():
    details = {'field': 'username', 'message': 'required'}
    result = format_error_response('Validation error', details=details)
    assert result['details'] == details
    assert result['error'] == 'Validation error'
    assert result['status'] == 400
