from unittest.mock import patch

import pytest
from rest_framework import status

from hive.api.models import ItemImage, Location
from tests.helpers import assert_dict_in, reverse

create_item_payloads = [
    ({"name": "item"}, {"name": "item"}),
    ({"name": "item", "description": "temp"}, {"name": "item", "description": "temp"}),
]


@pytest.mark.django_db
@pytest.mark.parametrize("create_payload,expected", create_item_payloads)
def test_item_create(create_payload, expected, client):
    response = client.post(reverse("item-list-view"), create_payload, format="json")
    assert_dict_in(expected, response.json())
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
@patch("hive.api.utils.check_call", lambda x: None)
def test_item_create_and_print(client):
    response = client.post(
        reverse("item-list-view"), {"name": "name", "print": True}, format="json"
    )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_create_item_and_image(client):
    response = client.post(
        reverse("item-list-view"),
        {"name": "item", "image": "sample_image"},
        format="json",
    )
    assert response.status_code == status.HTTP_201_CREATED

    assert_dict_in({"name": "item"}, response.json())
    image = ItemImage.objects.get(id=response.json()["image"])
    assert image.data == "sample_image"


@pytest.mark.django_db
def test_item_create_image(client):
    response = client.post(
        reverse("item-list-view"),
        {"name": "item", "image": "sample_image"},
        format="json",
    )
    assert response.status_code == status.HTTP_201_CREATED

    assert_dict_in({"name": "item"}, response.json())
    image = ItemImage.objects.get(id=response.json()["image"])
    assert image.data == "sample_image"


@pytest.mark.django_db
def test_get_item(client, item):
    response = client.get(reverse("item-detail-view", args=(item["upc"],)))
    assert_dict_in({"name": "name", "description": "description"}, response.json())
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_delete_item(client, item):
    response = client.delete(reverse("item-detail-view", args=(item["upc"],)))
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_update_item(client, item):
    Location.objects.create(name="The fun zone")
    response = client.put(
        reverse("item-detail-view", args=(item["upc"],)),
        {"description": "updated description", "location": "The fun zone"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["description"] == "updated description"
