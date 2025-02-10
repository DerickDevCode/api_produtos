import pytest
from django.urls import reverse

from api.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('home'))
    return resp


def test_status_code_home(resp):
    assert resp.status_code == 200


def test_conteudo(resp):
    assert_contains(resp, '<h1>HOME PAGE</h1>')
