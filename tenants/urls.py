from django.urls import path
from . import views

urlpatterns = [
    path('tenants/', views.list_tenants, name='tenant-list'),
]
