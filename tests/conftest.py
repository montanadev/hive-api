import pytest
from rest_framework import status
from rest_framework.test import APIClient

from tests.helpers import reverse


@pytest.fixture(scope="package")
def client():
    return APIClient()


@pytest.fixture(scope="function")
def item(client):
    response = client.post(
        reverse("item-list-view"),
        {"name": "name", "description": "description"},
        format="json",
    )
    assert response.status_code == status.HTTP_201_CREATED

    return response.json()
