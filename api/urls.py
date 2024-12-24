# api/urls.py
from django.urls import path
from . import views 

urlpatterns = [
    path('1024995/', views.data_api, name='1024995'),
]
