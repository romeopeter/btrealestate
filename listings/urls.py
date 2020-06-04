# This handle the url for routing

from django.urls import path
from . import views

# Defines views to pass dynamic data to listings page
urlpatterns = [
  path('', views.index, name='listings'),
  path('<int:listing_id>', views.listing, name='listing'),
  path('search', views.search, name='search')
]