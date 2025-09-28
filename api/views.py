from rest_framework.generics import RetrieveAPIView, ListAPIView
from .models import drawpage
from .serializers import drawpageSerializer
from django.shortcuts import render

def home(request):
    drawings = list(drawpage.objects.values("id", "name", "category"))
    return render(request, "main.html", {"drawings": drawings})

class DrawingListView(ListAPIView):
    queryset = drawpage.objects.all()
    serializer_class = drawpageSerializer

class DrawingDetailView(RetrieveAPIView):
    queryset = drawpage.objects.all()
    serializer_class = drawpageSerializer

    def get_serializer_context(self):
        # Add request to serializer context so ImageField builds absolute URLs
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
