from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name = 'index'),
    path('admin/', views.admin, name = 'admin'),
    path('add/', views.add, name = 'add'),
    path('upload/', views.upload, name = 'upload'),
]
