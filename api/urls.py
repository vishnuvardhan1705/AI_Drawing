from django.urls import path
from .views import DrawingDetailView, DrawingListView, home

urlpatterns = [
    path("", home, name="home"),
    path("drawings/", DrawingListView.as_view(), name="drawing-list"),
    path("drawings/<int:pk>/", DrawingDetailView.as_view(), name="drawing-detail"),
]
