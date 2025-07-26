from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import drawpage
from .serializers import drawpageSerializer

class drawstepsViewSet(APIView):
    def get(self, request):
        drawing = drawpage.objects.get(id=1)  # or filter for a specific drawing
        serializer = drawpageSerializer(drawing)
        return Response(serializer.data)
