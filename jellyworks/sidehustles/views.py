from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ValidationError

from jellyworks.settings import LOGOUT_REDIRECT_URL
#from sidehustles.forms import ChangeNameForm
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

from sidehustles.models import publicProfile, appUser, Reviews, Services
from .forms import UserEdits, AddReview


def index(request):
    """This is the view function for the sidehustles landing page."""

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
    review_instance = get_object_or_404(Reviews, pk=pk)

    if request.method == "POST":
        form = AddReview(request.POST, instance=request.user)
        if form.is_valid():
            review_instance.editable_text = form.cleaned_data['editable_text']
            review_instance.save()
            return redirect('product', pk)

    else:
        form = AddReview()

    context = {
        'service': Services.objects.get(id=pk),
        'reviews': Reviews.objects.filter(service=pk).distinct(),
        'form' : form,
        'review_instance' : Reviews
    }
    return render(request, 'product.html', context=context)

#   return render(request, 'product.html', context)    


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

def profile_changes(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = UserEdits(data=request.POST, instance=request.user)
            if form.is_valid():
                edits = form.save()
                edits.save()
                return redirect('profile')
        else:
            form = UserEdits()
            context = {
                'form' : form
            }
            return render(request, 'profile_changes.html', context=context) 
    else:
        return redirect('index')

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('profile')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
            context = {
                'form' : form
            }
            return render(request, 'accounts/change_password.html', context=context)
    else:
        return redirect('index') 

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
