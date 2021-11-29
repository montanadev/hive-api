from rest_framework import serializers

from hive.api.models.item import Item
from hive.api.models.location import Location


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

    image = serializers.SerializerMethodField()
    image_id = serializers.SerializerMethodField()

    @staticmethod
    def get_location(obj):
        return LocationSerializer(obj.location).data

    @staticmethod
    def get_image(obj):
        if not obj.image:
            return None
        return obj.image.data

    @staticmethod
    def get_image_id(obj):
        if not obj.image:
            return None
        return obj.image.id

    class Meta:
        model = Item
        fields = "__all__"


class ItemCreateRequestSerializer(serializers.Serializer):
    description = serializers.CharField(allow_blank=True)
    name = serializers.CharField()
    print = serializers.BooleanField(default=False)
    image = serializers.CharField(allow_blank=True)


class ItemUpdateRequestSerializer(serializers.Serializer):
    location = serializers.CharField()


class PrintRequestSerializer(serializers.Serializer):
    upc = serializers.IntegerField()
    description = serializers.CharField()
