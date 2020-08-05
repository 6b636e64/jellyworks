from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
    image = models.ImageField(upload_to='uploads/', default="uploads/profile_pic_placeholder.jpg", blank=True, null=True)

    def __str__(self):
        return self.email