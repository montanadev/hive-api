import pytest
from rest_framework import status

from hive.api.models import ItemImage
from tests.helpers import reverse


@pytest.mark.django_db
def test_create_image(client, item):
    # post to an existing item a new image
    response = client.post(
        reverse("item-image-detail-view", args=(item["upc"],)),
        {"image": "sample"},
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK

    image = ItemImage.objects.get(id=response.json()["image"])
    assert image.data == "sample"


@pytest.mark.django_db
def test_delete_image(client, item):
    # image doesnt exist, 404
    response = client.delete(
        reverse("item-image-detail-view", args=(item["upc"],)), format="json"
    )
    # 404 because no image attached
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # attach image
    client.post(
        reverse("item-image-detail-view", args=(item["upc"],)),
        {"image": "sample"},
        format="json",
    )
    response = client.delete(
        reverse("item-image-detail-view", args=(item["upc"],)), format="json"
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
