"""hive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from hive.api.views.item import ItemDetailView, ItemListView
from hive.api.views.item_image import ItemImageDetailView
from hive.api.views.location import LocationListView
from hive.api.views.print import print_handler

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/items/", ItemListView.as_view(), name='item-list-view'),
    path("api/items/<int:pk>", ItemDetailView.as_view(), name='item-detail-view'),
    path("api/items/<int:pk>/image", ItemImageDetailView.as_view()),
    path("api/locations/", LocationListView.as_view()),
    path("api/print", print_handler),
]
