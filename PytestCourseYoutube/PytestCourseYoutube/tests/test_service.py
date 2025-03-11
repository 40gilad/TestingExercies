import pytest
import source.service as service
import unittest.mock as mock


@mock.patch("source.service.requests.get")
def test_get_users_from_endpoint(mocked_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": 1, "name": "Paul Mccartney"}]
    mocked_get.return_value = mock_response
    data = service.get_users_from_endpoint()
    assert data == [{"id kaki": 1, "name kaki": "Paul Mccartney"}]
