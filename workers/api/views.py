from workers.models import (WorkerModel)
from workers.api.serializers import (WorkersSerializers)
from rest_framework import generics

class WorkersListView(generics.ListCreateAPIView):
    queryset = WorkerModel.objects.all()
    serializer_class = WorkersSerializers



class WorkerDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkerModel.objects.all()
    serializer_class = WorkersSerializers
    lookup_field = "pk"




