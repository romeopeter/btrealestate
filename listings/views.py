# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from listings.choice import stateChoices, bedroomChoice, priceChoices

from .models import Listing, Realtor

def index(request):
  # Get all listings by date (DESC)
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  # Paginate listings
  paginator = Paginator(listings, 6) # Shows six per page
  page = request.GET.get('page')
  
  pagedListing = paginator.get_page(page)

  # Pass listings to template
  context = {
    'listings': pagedListing,
  }

  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  # Get specific listing & realtor or return 404
  listing = get_object_or_404(Listing, pk=listing_id)

  # Pas data to template
  context = {
    'listing': listing,
  }

  return render(request, 'listings/listing.html', context)

def search(request):
  querysetList = Listing.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      querysetList = querysetList.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      querysetList = querysetList.filter(city__iexact=city)

  # States
  if 'state'  in request.GET:
    state = request.GET['state']
    if state:
      querysetList = querysetList.filter(state__iexact=state)

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedroom = request.GET['bedrooms']
    if bedroom:
      querysetList = querysetList.filter(bedroom__lte=bedroom)

  # Prices
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      querysetList = querysetList.filter(price__lte=price)

  context = {
    'stateChoices': stateChoices,
    'bedroomChoices': bedroomChoice,
    'priceChoices': priceChoices,
    'listings': querysetList,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context)