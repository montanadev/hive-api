from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.response import Response

from hive.api.models.item import Item
from hive.api.models.item_image import ItemImage
from hive.api.models.location import Location, get_default_new_item_location
from hive.api.serializers import (
    ItemCreateRequestSerializer,
    ItemSerializer,
    ItemUpdateRequestSerializer,
)
from hive.api.utils import print_qr_label


class ItemListView(ListCreateAPIView):
    queryset = Item.objects.all().prefetch_related("location")
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = ItemCreateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        location = get_default_new_item_location()

        image = None
        if serializer.data["image"]:
            image = ItemImage.objects.create(data=serializer.data["image"])

        item = Item.objects.create(
            description=serializer.data["description"],
            name=serializer.data["name"],
            location=location,
            image=image,
        )

        if serializer.data["print"]:
            print_qr_label(item.upc, item.name)

        response_data = ItemSerializer(item).data
        return JsonResponse(data=response_data, status=status.HTTP_201_CREATED)


class ItemDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def update(self, request, *args, **kwargs):
        serializer = ItemUpdateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        item = self.get_object()

        if serializer.validated_data['location']:
            location = get_object_or_404(Location, name=serializer.data["location"])
            item.location = location

        item.description = serializer.validated_data['description'] or item.description
        item.touched += 1
        item.save()

        response_data = ItemSerializer(item).data
        return Response(response_data)
