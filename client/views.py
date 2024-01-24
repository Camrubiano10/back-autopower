from rest_framework.viewsets import ModelViewSet
from .models import Client
from .serializers import ClientSerializer
# from rest_framework.permissions import IsAuthenticated


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field='license_plate'    # permission_classes = [IsAuthenticated]
