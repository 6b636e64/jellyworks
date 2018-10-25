import uuid

from django.db import models
from django.urls import reverse

class PublicProfile(models.Model):
    """Model representing a public profile."""

    fname = models.CharField(max_length=50, help_text="First name")
    lname = models.CharField(max_length=50, help_text="Last name")
    displayname = models.CharField(max_length=30, help_text="Display name")
    email = models.ForeignKey()

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class User(models.Model):
    """Model representing a private student (user account)"""

    fname = models.CharField(max_length=50, help_text="First name")
    lname = models.CharField(max_length=50, help_text="Last name")
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    # Email as a string rather than object because it hasn't been
    # declared yet in the file
    
    #email = models.PrimaryKey("Email", on_delete=models.SET_NULL, null=True)

    

  
    
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Reviews(models.Model):
    """Model representing a customer review."""

    review = models.ForeignKey("Review", on_delete=models.SET_NULL, null=True)

    review_text = models.TextField(help_text = "Type a review")

    date_posted = models.DateField(null=True, blank=True)


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
    serivce_reviews = models.TextField(help_text = "Type a review.")
