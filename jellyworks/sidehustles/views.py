from django.shortcuts import render

# Create your views here.

from sidehustles.models import publicProfile, appUser, Reviews, Services

def index(request):
    """This is the view function for the sidehustles landing page."""

    #Counting the number of public profiles, reviews, and services

    num_publicprofiles = publicProfile.objects.all.count() 
    num_reviews = Reviews.objects.all.count()
    num_services = Services.objects.all.count()
    
    
    context = {
        "num_publicprofiles": num_publicprofiles,
        "num_reviews": num_reviews,
        "num_services": num_services,
        }
    
    return render(request,'index.html',context=context)
