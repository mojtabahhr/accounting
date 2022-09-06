from rest_framework.serializers import (ModelSerializer)
from workers.models import (WorkerModel)



class WorkersSerializers(ModelSerializer):
    class Meta:
        model = WorkerModel
        fields = "__all__"
        
