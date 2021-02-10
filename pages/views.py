from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import (bedroom_choices, price_choices, state_choices)
# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-price').filter(is_published = True)
    listings = listings[:3]
    context = {
        "listings"          : listings,
        "bedroom_choices"   : bedroom_choices,
        "price_choices"     : price_choices,
        "state_choices"     : state_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors        = Realtor.objects.all()
    mvp             = realtors.filter(is_mvp = True)
    context = {
        "realtors"  : realtors,
        "mvp"       : mvp
    }
    return render(request, 'pages/about.html', context)
