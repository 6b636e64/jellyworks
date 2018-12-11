from django import forms
from django.forms import ModelForm
from .models import Reviews
from . import models
from users.models import CustomUser
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import UserInstance
from .models import publicProfile
from django.contrib.auth.models import User

class UserEdits(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']
      
class AddReview(ModelForm):

    def clean_review_text(self):
       data = self.cleaned_data['review_text']

       if "fuck" in data :
           raise forms.ValidationError(_("Don't be rude!"))

       # Remember to always return the cleaned data.
       return data

    class Meta:
        model = Reviews
        fields = ['review_text']

class ProfileImage(forms.ModelForm):

    class Meta:
      model = CustomUser
      fields = ['image']

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


