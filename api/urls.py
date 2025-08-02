from django.urls import path
from .views import drawstepsViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('items/<str:name>/', drawstepsViewSet.as_view(), name='item-by-name'),
]