from django.shortcuts import get_object_or_404, render

# Import extra libraries/models here
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #For Pagination
from .models import Listing
from .choices import (bedroom_choices, price_choices, state_choices)

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)
    paginator = Paginator(listings, 3)
    page_number = request.GET.get('page')
    paged_listings = paginator.get_page(page_number)
    context = {
        'listings': paged_listings,
    }
    return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk = listing_id)
    # listing = Listing.objects.get(id = listing_id)
    context = {
        "id" : listing_id,
        "listing": listing
    }
    return render(request, "listings/listing.html", context)

def search(request):
    queryset = Listing.objects.order_by("-list_date")
    
    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset = queryset.filter(description__icontains = keywords)
            
    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset = queryset.filter(city__iexact = city)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset = queryset.filter(price__lte = price)
            
    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset = queryset.filter(bedrooms__lte=bedrooms)
    
    #State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset = queryset.filter(state__iexact=state)
            
    context = {
        "bedroom_choices"   : bedroom_choices,
        "price_choices"     : price_choices,
        "state_choices"     : state_choices,
        "listings"          : queryset,
        "values"            : request.GET
    }
    return render(request, "listings/search.html", context)