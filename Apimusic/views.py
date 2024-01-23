from rest_framework import viewsets
from .serializer import MusicSerializer
from .models import Music

# Create your views here.

class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()  # No serializer_class here
    serializer_class = MusicSerializer  # Set it as a class attribute
