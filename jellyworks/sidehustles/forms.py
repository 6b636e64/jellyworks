from django import forms
from .models import appUser

class UserEdits(forms.ModelForm):

    class Meta:
        model = appUser
        fields = ('user_fname', 'user_lname',)
      
