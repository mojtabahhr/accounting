from pyexpat import model
from django.forms import ModelForm
from workers.models import CostsModel


class AddCostForm(ModelForm):
    class Meta:
        model = CostsModel
        fields = "__all__"