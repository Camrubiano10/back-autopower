from rest_framework.viewsets import ModelViewSet
from .models import Client
from .serializers import ClientSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def retrieve(self, request, *args, **kwargs):
        search=Client.objects.get(license_plate=kwargs['pk'])
        serializer = self.serializer_class(search)
        return Response(serializer.data)


from rest_framework.viewsets import ModelViewSet
from .models import Client
from .serializers import ClientSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def retrieve(self, request, *args, **kwargs):
        search=Client.objects.get(license_plate=kwargs['pk'])
        serializer = self.serializer_class(search)
        return Response(serializer.data)