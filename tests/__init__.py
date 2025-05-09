from http import HTTPStatus

from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_root_return_test(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'teste'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'discordid': '123456789012345678',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'discordid': '123456789012345678',
        'id': 1,
    }
