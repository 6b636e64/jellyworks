from django import forms
from .models import Reviews
from django.contrib.auth.models import User

class UserEdits(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']
      
class AddReview(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ['review_text', 'review_star_count']
