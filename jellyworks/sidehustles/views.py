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
        "list_o_services": Services.objects.all()
    }
    
    return render(request,'index.html',context=context)

def profile(request):
    """I don't really know what this is"""

    context = {

    }

    return render(request, 'profile.html', context=context)

def about(request):
    return render(request, 'about.html')


def product(request):

    seller_name = publicProfile.public_displayname
    service_name = Services.service_name
    service_reviews = Services.service_reviews
    service_likes = Reviews.review_like_count
    service_stars = Reviews.review_star_count
    
    context = {
        "list_o": Services.objects.all(),
        "list_o_reviews": Reviews.objects.all(),
        "seller_name" : seller_name,
        "service_name" : service_name,
        "service_reviews" : service_reviews,
        "service_likes" : service_likes,
        "service_stars" : service_stars
    }

    return render(request, 'product.html', context=context)

def filtersearch(request):
    user_list = publicProfile.objects.all()
    skill_types = []
    locations = []
    days = []
    for st in publicProfile.SKILL_TYPE:
        skill_types.append(st[0])
    for st in publicProfile.LOCATION_TYPE:
        locations.append(st[0])
    for st in publicProfile.AVAILABILITY_TYPE:
        days.append(st[0])
    context = {
        'users': user_list,
        'skilltypes': skill_types,
        'location_types': locations,
        'availability_types': days
    }
    return render(request, 'filtersearch.html', context=context)
