from rest_framework import viewsets
from .serializer import GatosSerializer
from .models import Gatos

class GatosView(viewsets.ModelViewSet):
    serializer_class = GatosSerializer  # Assign serializer class to serializer_class attribute
    queryset = Gatos.objects.all()