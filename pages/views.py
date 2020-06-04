# Create your views here.
from django.shortcuts import render
from listings.choice import priceChoices, bedroomChoice, stateChoices

from listings.models import Listing
from realtors.models import Realtor

def index(request):
  # Get all listings by date (DESC)
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3] # Limit listing to just 3

  # Pass listings to template
  context = {
    'listings': listings,
    'stateChoices': stateChoices,
    'bedroomChoices': bedroomChoice,
    'priceChoices': priceChoices 
  }
  return render(request, 'pages/index.html', context)

def about(request):
  # Get all realtors
  realtors = Realtor.objects.order_by('-hire_date')

  # Get MVP
  mvps = Realtor.objects.all().filter(is_mvp=True)

  # Pass realors & mvp to template
  context = {
    'realtors': realtors,
    'mvps': mvps
  }

  return render(request, 'pages/about.html', context)