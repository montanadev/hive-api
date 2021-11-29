from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListCreateAPIView

from hive.api.models.location import Location
from hive.api.serializers import LocationCreateRequestSerializer, LocationSerializer


class LocationListView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def create(self, request, *args, **kwargs):
        serializer = LocationCreateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        location = Location.objects.create(name=serializer.data["name"])

        response_data = LocationSerializer(location).data
        return JsonResponse(data=response_data, status=status.HTTP_201_CREATED)
