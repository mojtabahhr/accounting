from rest_framework.serializers import ModelSerializer
from costsapp.models import CostsModel

class CostsSerializers(ModelSerializer):
    class Meta:
        model = CostsModel
        fields = "__all__"