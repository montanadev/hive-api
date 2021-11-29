from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from hive.api.serializers import PrintRequestSerializer
from hive.api.utils import print_qr_label


@api_view(["POST"])
def print_handler(request):
    serializer = PrintRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    print_qr_label(serializer.data["upc"], serializer.data["description"])

    return JsonResponse(data={}, status=status.HTTP_200_OK)
