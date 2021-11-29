from django.conf import settings
from django.db import models


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()


def get_default_new_item_location():
    try:
        return Location.objects.get(name=settings.NEW_ITEM_DEFAULT_LOCATION)
    except Location.DoesNotExist:
        return Location.objects.create(
            name=settings.NEW_ITEM_DEFAULT_LOCATION,
            description="Default new item location",
        )
