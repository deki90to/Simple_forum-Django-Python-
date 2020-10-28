from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name = 'index'),
    path('details/<int:id>', views.details, name = 'details'),
    path('admin', views.admin, name = 'admin'),
    path('add', views.add, name = 'add'),
]
