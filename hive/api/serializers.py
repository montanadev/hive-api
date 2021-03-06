from rest_framework import serializers

from hive.api.models.item import Item
from hive.api.models.location import Location


class ItemImageCreateRequestSerializer(serializers.Serializer):
    image = serializers.CharField()


class LocationCreateRequestSerializer(serializers.Serializer):
    name = serializers.CharField()


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    # todo - drop this, hydrate location name directly
    location_id = serializers.IntegerField(source="location.id")
    location = serializers.SerializerMethodField()

    @staticmethod
    def get_location(obj):
        return LocationSerializer(obj.location).data

    class Meta:
        model = Item
        fields = ("upc", "name", "description", "touched", "location", "location_id", "image")


class ItemCreateRequestSerializer(serializers.Serializer):
    description = serializers.CharField(default='')
    name = serializers.CharField()
    print = serializers.BooleanField(default=False)
    image = serializers.CharField(default='')


class ItemUpdateRequestSerializer(serializers.Serializer):
    location = serializers.CharField(default='')
    description = serializers.CharField(default='')


class PrintRequestSerializer(serializers.Serializer):
    upc = serializers.CharField()
    description = serializers.CharField()
