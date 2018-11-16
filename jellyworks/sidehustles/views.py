from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from jellyworks.settings import LOGOUT_REDIRECT_URL
from sidehustles.forms import ChangeNameForm


# Create your views here.

from sidehustles.models import publicProfile, appUser, Reviews, Services

def index(request):
    """This is the view function for the sidehustles landing page."""

    #Counting the number of public profiles, reviews, and services


    context = {
        "list_o_services": Services.objects.all()
    }

    return render(request,'index.html',context=context)

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('index')

def about(request):
    return render(request, 'about.html')


def product(request, pk):
    return render(request, 'product.html', {'service': Services.objects.get(id=pk), 'review': Reviews.objects.get(id=pk)})


def filtersearch(request):
    user_list = Services.objects.all()
    skill_types = []
    locations = []
    days = []
    for st in Services.SKILL_TYPE:
        skill_types.append(st[0])
    for st in Services.LOCATION_TYPE:
        locations.append(st[0])
    for st in Services.AVAILABILITY_TYPE:
        days.append(st[0])
    context = {
        'users': user_list,
        'skilltypes': skill_types,
        'location_types': locations,
        'availability_types': days
    }
    return render(request, 'filtersearch.html', context=context)



# def profileChanges(request, pk):
#     """View function for changing name."""
#     user_instance = get_object_or_404(UserInstance, pk=pk)

#     # If this is a POST request then process the Form data
#     if request.method == 'POST':

#         # Create a form instance and populate it with data from the request (binding):
#         form = ChangeNameForm(request.POST)

#         # Check if the form is valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required (here we just write it to the model due_back field)                                                                                                                
#             user_instance.public_fname = form.cleaned_data['first_name']
#             user_instance.public_lname = form.cleaned_data['last_name']
#             user_instance.save()

#             # redirect to a new URL:
#             return HttpResponseRedirect(reverse('/') )

#     # If this is a GET (or any other method) create the default form.
#     else:
#         form = ChangeNameForm(initial={'first_name': 'Jane', 'last_name':'Doe'})

#     context = {
#         'form': form,
#         'user_instance': user_instance,
#     }

#     return render(request, 'profile_changes.html', context)
