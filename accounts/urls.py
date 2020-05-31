# Handle url for routing accounts
from django.urls  import path
from . import views

# Define patter to pass dynamic data to accounts

urlpatterns = [
  path('register', views.register, name='register'),
  path('login', views.login, name='login'),
  path('logout', views.logout, name='logout'),
  path('dashboard', views.dashboard, name='dashboard'),
]