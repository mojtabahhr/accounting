from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from costsapp.models import CostsModel
from costsapp.api.serializers import CostsSerializers


class CostsListView(ListCreateAPIView):
    queryset = CostsModel.objects.all()
    serializer_class = CostsSerializers
    

