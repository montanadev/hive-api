from django.db import models

from hive.api.models.item_image import ItemImage
from hive.api.models.location import Location


class Item(models.Model):
    upc = models.BigAutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    touched = models.IntegerField(default=0)

    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    image = models.ForeignKey(ItemImage, null=True, on_delete=models.SET_NULL)
