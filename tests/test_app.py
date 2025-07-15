from http import HTTPStatus

from fastapi.testclient import TestClient

from src.fast_zero.app import app


def test_read_root_ok_e_ola_mundo():
    client = TestClient(app)  # Arrenge/Organizacao do teste

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'Menssagem': 'Olá mundo!'}
