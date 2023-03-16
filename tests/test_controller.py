import pytest
import json
from app.controller import api


@pytest.fixture
def client():
    return api.test_client()


def test_crawl(client):
    response = client.post('/crawl')
    assert response.status_code == 200
    assert json.loads(response.data) == {"Status": "OK"}


def test_filter_more_than_five(client):
    response = client.get('/filter/more_than_five')
    assert response.status_code == 200


def test_filter_less_than_or_five(client):
    response = client.get('/filter/less_than_or_five')
    assert response.status_code == 200


def test_page_not_found(client):
    response = client.get('/wrong-url')
    assert response.status_code == 404
    assert json.loads(response.data) == {"Status": "The requested URL was not found on the server."}