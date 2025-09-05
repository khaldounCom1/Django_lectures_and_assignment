from django.urls import path
from . import views

urlpatterns = [
    path('patients_index', views.index, name='patients_index'),
]
