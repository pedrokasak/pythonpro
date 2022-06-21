from django.test import Client


def test_status_code(client: Client):
    response = client.get('/')
    response.status_code == 200
