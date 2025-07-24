from django.shortcuts import render
from rest_framework import viewsets
from .models import drawpage
from .serializers import drawpageSerializer

class drawstepsViewSet(viewsets.ModelViewSet):
    queryset=drawpage.objects.all()
    serializer_class=drawpageSerializer
