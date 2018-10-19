import uuid

from django.db import models
from django.urls import reverse

class PublicProfile(models.Model):
    """Model representing a public profile."""

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    displayname = models.CharField(max_length=30)
    email = models.ForgeinKey()

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class PrivateStudent(models.Model):
    """Model representing a private student (user account)"""

    fname = models.CharField(max_length=50)

    # Author is a foreign Key because book can only have one author, but
    # authors can have multiple books.
    #
    # Author as a string rather than object because it hasn't been
    # declared yet in the file
    email = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)

    # Summary is a simple text field.
    summary = models.TextField(
        max_length=1000, help_text="Enter a brief description of the book"
    )

    # ISBN is a simple character field.
    isbn = models.CharField(
        "ISBN",
        max_length=13,
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>',
    )

    # Genre is a ManyToManyField because genre can contain many
    # books. Books can cover many genres.  Genre class has already
    # been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        # This function uses the string object's join method to "join"
        # all the genre strings into a single string separated by ',
        # '. This uses Python's list comprehension feature. If you do
        # not know what this is you should look this up to see what
        # this is. It is a very powerful language feature!
        #
        # We also use Python's list slicing notation ([:3]). This
        # indicates that we will only take the first 3 elements from
        # the list. This is done so we only display some of the genres
        # rather than all of them - efficiency!
        return ", ".join(genre.name for genre in self.genre.all()[:3])

    # This defines a property on the method (yes, functions and
    # methods can have properties in Python) that can be used in the
    # admin site for this method.
    display_genre.short_description = "Genre"

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse("book-detail", args=[str(self.id)])


class Reviews(models.Model):
    """Model representing a customer review."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular book across whole library",
    )

    book = models.ForeignKey("Book", on_delete=models.SET_NULL, null=True)

    imprint = models.CharField(max_length=200)

    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="m",
        help_text="Book availability",
    )

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.id} ({self.book.title})"


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

    class Meta: 
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse("author-detail", args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.last_name}, {self.first_name}"
