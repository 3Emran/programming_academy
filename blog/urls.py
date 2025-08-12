# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-home'),  # Adjust this based on your actual views
]
