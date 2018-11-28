from django import forms
from .models import Reviews
from users.models import CustomUser


class UserEdits(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']
      
class AddReview(forms.ModelForm):

    def clean_due_back(self):
       data = self.cleaned_data['editable_text']

       # Check if a date is not in the past.
       if "fuck" in data :
           raise ValidationError(_("Don't be rude!"))

       # Remember to always return the cleaned data.
       return data

    class Meta:
        model = Reviews
        fields = ['editable_text']
