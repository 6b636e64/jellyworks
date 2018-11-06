import uuid

from django.db import models
from django.urls import reverse

class publicProfile(models.Model):
    """Model representing a public profile."""

    public_fname = models.CharField(max_length=50, help_text="First name", default="Biggie")
    public_lname = models.CharField(max_length=50, help_text="Last name", default="Smalls")
    public_displayname = models.CharField(max_length=30, help_text="Display name", default="Tupac")
    public_email = models.CharField(max_length=50, help_text="Email", default="Tupac@gmail.com")
    

    def __str__(self):
        """String for representing the Model object."""
        return self.public_displayname

class appUser(models.Model):
    """Model representing a private student (user account)"""

    user_fname = models.CharField(max_length=50, help_text="First name", default="Kendrick")
    user_lname = models.CharField(max_length=50, help_text="Last name", default="Lamar")
    user_unique_email = models.CharField(max_length=100, default="Tupac@gmail.com")
    user_password = models.CharField(max_length=50, default="abc123")
    
    def __str__(self):
        """String for representing the Model object."""
        return self.user_unique_email

class Reviews(models.Model):
    """Model representing a customer review."""
		
    review_like_count = models.IntegerField()
    review_star_count = models.IntegerField()
    review_text = models.TextField(help_text = "Type a review", default="Macklemore is amazeballs")
    review_date_posted = models.DateField(default="1/1/18")
    
    def __str__(self):
        """String for representing the Model object."""
        return self.review_text
    
class Services(models.Model):
    """Model representing a service offered on Sidehustles."""

    # A character field for the service name.
    service_name = models.CharField(max_length=200, default = "Tupac's 3-Pack Sodas")
    public_displayname = models.CharField(max_length=30, help_text="Display name", default="Tupac")
    # A integer field for the service cost.
    service_cost = models.IntegerField()
    
    # A character field for the service category.
    service_category = models.CharField(max_length=200, default = "J Cole")
    
    # A character field to indicate the service's location.
    service_location = models.CharField(max_length=200, default = "Grandmaster Flash")
    
    # A integer field to indicate proficieny (scale to be determined)
    service_proficiency = models.IntegerField()
    
    # A character field for a review.
    service_reviews = models.TextField(help_text = "Type a review.")
    
    skill_info = models.CharField(max_length=1000, help_text="Tell us more about your skill!", default="I am very skilled!")
    SKILL_TYPE = [("Computers", "Computers"), ("Music", "Music"), ("Art", "Art"), ("Sports", "Sports"), ("Manual Labor", "Manual Labor"),
                  ("Tutoring", "Tutoring")]
    skill = models.CharField(max_length=50, choices=SKILL_TYPE, default='Computers')
    LOCATION_TYPE = [("UMass Amherst", "UMass Amherst"), ("5-College", "5-College"), ("Off Campus", "Off Campus")]
    location = models.CharField(max_length=50, choices=LOCATION_TYPE, default='1')
    AVAILABILITY_TYPE = [("M", "M"), ("T", "T"), ("W", "W"), ("Th", "Th"), ("F", "F"),
                  ("Sat", "Sat"), ("Sun", "Sun"), ("Unavailable", "Unavailable")]
    availability = models.CharField(max_length=9, choices=AVAILABILITY_TYPE, default='8')
    # id = models.UUIDField(primary_key = True, default=uuid.uuid4, unique=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.service_name
        
    def get_absolute_url(self):
        return reverse("product", args=[str(self.id)])
