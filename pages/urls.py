# This handle the url for routing

from django.urls import path
from . import views

# Defines views to pass dynamic data to index
urlpatterns = [
  path('', views.index, name='index'),
  path('about', views.about, name='about'),
]