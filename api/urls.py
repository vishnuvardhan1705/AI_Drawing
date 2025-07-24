from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import drawstepsViewSet

router = DefaultRouter()
router.register(r'drawing', drawstepsViewSet, basename='drawpage')

urlpatterns = [
    path('', include(router.urls)),
]