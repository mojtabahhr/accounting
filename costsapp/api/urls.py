from django.urls import path
from costsapp.api import views 
urlpatterns = [
    path('costs/', views.CostsListView.as_view(), name="Costs-list"),
]
