from rest_framework  import serializers
from .models import Gatos

class GatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gatos
        fields = "__all__"