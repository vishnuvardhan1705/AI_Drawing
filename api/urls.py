from django.urls import path
from .views import drawstepsViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('drawing/',drawstepsViewSet.as_view()),
]