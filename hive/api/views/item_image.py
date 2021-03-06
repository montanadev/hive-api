from base64 import b64decode

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from hive.api.models.item import Item
from hive.api.models.item_image import ItemImage
from hive.api.serializers import ItemImageCreateRequestSerializer, ItemSerializer


class ItemImageDetailView(APIView):
    @staticmethod
    def get(request, pk=None):
        item = get_object_or_404(Item, upc=pk)
        if not item.image:
            return Response(status=status.HTTP_404_NOT_FOUND)

        barray = item.image.data.split("data:image/png;base64,")[-1]
        return HttpResponse(
            bytes(b64decode(barray)), headers={"Content-Type": "image/png"}
        )

    @staticmethod
    def post(request, pk=None):
        serializer = ItemImageCreateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        image = ItemImage.objects.create(data=serializer.data["image"])

        item = get_object_or_404(Item, upc=pk)
        item.image = image
        item.save()

        response_data = ItemSerializer(item).data
        return Response(response_data)

    @staticmethod
    def delete(request, pk=None):
        item = get_object_or_404(Item, upc=pk)
        if item.image:
            item.image.delete()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)
