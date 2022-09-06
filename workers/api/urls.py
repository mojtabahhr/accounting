from django.urls import path
from workers.api import views 
urlpatterns = [
    path('workers/', views.WorkersListView.as_view(), name='workers-list'),
    path('workers/<int:pk>/', views.WorkerDetailsView.as_view(), name='workers-details-list'),
]
