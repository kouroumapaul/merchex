from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Brand
from listings.models import Listing


def brand(request):
    brands = Brand.objects.all()
    return render(request,
                  "listings/brand.html",
                  {"brands": brands})


def about(request):
    return HttpResponse('<h1>About us <h1/>')


def contact(request):
    return render(request, 'listings/contact.html')


def listing(request):
    listings = Listing.objects.all()
    return render(request,
                  "listings/listing.html",
                  {"listings": listings})
