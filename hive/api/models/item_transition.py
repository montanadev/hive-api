from django.db import models
from hive.api.models.location import Location
from hive.api.models.item import Item

class ItemTransition(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    from_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='from_location')
    to_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='to_location')

    created_at = models.DateTimeField(auto_now_add=True)

