from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import drawpage
from .serializers import drawpageSerializer

class drawstepsViewSet(APIView):
    def get(self, request,name,format=None):
        try:
            drawing = drawpage.objects.get(name=name)
            serializer = drawpageSerializer(drawing)
            return Response(serializer.data)
        except drawpage.DoesNotExist:
            return Response({'detail': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

