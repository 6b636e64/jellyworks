import uuid

from django.db import models
from django.urls import reverse

class publicProfile(models.Model):
    """Model representing a public profile."""

    public_fname = models.CharField(max_length=50, help_text="First name")
    public_lname = models.CharField(max_length=50, help_text="Last name")
    public_displayname = models.CharField(max_length=30, help_text="Display name", unique=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.public_displayname

class User(models.Model):
    """Model representing a private student (user account)"""

    user_fname = models.CharField(max_length=50, help_text="First name")
    user_lname = models.CharField(max_length=50, help_text="Last name")
    user_unique_email = models.CharField(max_length=100, primary_key=True)
    user_password = models.CharField(max_length=50)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.unique_email

class Reviews(models.Model):
    """Model representing a customer review."""
		
    review_like_count = models.IntegerField()
    review_star_count = models.IntegerField()
    review_text = models.TextField(help_text = "Type a review")
    review_date_posted = models.DateField(null=True, blank=True)
    
class Services(models.Model):
    """Model representing a service offered on Sidehustles."""

    # A character field for the service name.
    service_name = models.CharField(max_length=200)
		
    # A integer field for the service cost.
    service_cost = models.IntegerField()
    
    # A character field for the service category.
    service_category = models.CharField(max_length=200)
    
    # A character field to indicate the service's location.
    service_location = models.CharField(max_length=200)
    
    # A integer field to indicate proficieny (scale to be determined)
    service_proficiency = models.IntegerField()
    
    # A character field for a review.
    service_reviews = models.TextField(help_text = "Type a review.")
