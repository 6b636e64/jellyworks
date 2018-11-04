from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView

# Create your views here.

from sidehustles.models import publicProfile, appUser, Reviews, Services

def index(request):
    """This is the view function for the sidehustles landing page."""

    #Counting the number of public profiles, reviews, and services

    num_publicprofiles = publicProfile.objects.all().count() 
    num_reviews = Reviews.objects.all().count()
    num_services = Services.objects.all().count()
    
    
    context = {
        "num_publicprofiles": num_publicprofiles,
        "num_reviews": num_reviews,
        "num_services": num_services,
    }
    
    return render(request,'index.html',context=context)

def profile(request):
    """I don't really know what this is"""

    context = {

    }

    return render(request, 'profile.html', context=context)

def about(request):
    return render(request, 'about.html')


class ProductView(generic.ListView):
    model = publicProfile
    template_name = "product.html"

class FilterSearchView(generic.ListView):
    model = publicProfile
    template_name = "filtersearch.html"