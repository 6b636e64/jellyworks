from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ValidationError
from django.template import RequestContext
from django.contrib.auth import login

from jellyworks.settings import LOGOUT_REDIRECT_URL
#from sidehustles.forms import ChangeNameForm
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

from sidehustles.models import publicProfile, appUser, Reviews, Services
from .forms import UserEdits, AddReview, ProfileImage, UserForm
from users.models import CustomUser

def index(request):
    """This is the view function for the sidehustles landing page."""

    context = {
        "list_o_services": Services.objects.all()
    }

    return render(request,'index.html',context=context)

def profile(request):
    if request.user.is_authenticated:
        context = {"user": request.user}
        return render(request, 'profile.html', context)
    else:
        return redirect('index')

def about(request):
    return render(request, 'about.html')


def product(request, pk):

    context = {
        'service': Services.objects.get(id=pk),
        'reviews': Reviews.objects.filter(service=pk).distinct(),
        #'review_instance' : Reviews
    }

    if request.method == "POST":
        form = AddReview(request.POST, request.user)
        if form.is_valid():
            edits = form.save(commit=False)
            edits.review_text = form.cleaned_data['review_text']
            edits.service = Services.objects.get(id=pk)
            edits.user = request.user
            edits.save()
            context.update({'form':form})
            return redirect('product', pk=pk)
        else:
            context.update({'form':form})
            return render(request, 'product.html', context)
    else:
        form = AddReview()
        context.update({'form':form})


    return render(request, 'product.html', context)

#   return render(request, 'product.html', context)    

def search(request):
    user_list = Services.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'filtersearch.html', {'filter': user_filter})

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

def upload_image(request):
    if request.method == 'POST':
        form = ProfileImage(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            newImage = form.save()
            newImage.save()
            return redirect('profile')
    else:
        form = ProfileImage()
    
    return render(request, 'change_picture.html', {'form':form, })


def new_account(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = CustomUser.objects.create_user(**form.cleaned_data)
            login(request,new_user)
            # redirect, or however you want to get to the main view
            return redirect('index')
    else:
        form = UserForm() 

    return render(request, 'new_account.html', {'form': form}) 