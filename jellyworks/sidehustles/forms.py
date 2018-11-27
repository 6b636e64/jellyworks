from django import forms
from .models import Reviews
from users.models import CustomUser


class UserEdits(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']
      
class AddReview(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ['review_text', 'review_star_count']
