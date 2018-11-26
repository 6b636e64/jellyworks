from django import forms
#from .models import appUser
from django.contrib.auth.models import User

class UserEdits(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']
      
