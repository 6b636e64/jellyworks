import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from faker import Faker

from Sidehustles.models import PublicProfile,  Services, PrivateStudent, Reviews

fake = Faker()

# Create Private Student 
privatestudent = []
  ps_fname = fake.first_name()
  ps_lname = fake.last_name()
  ps_email = fake.ascii_free_email()
  ps_password = fake.password()
	student = privatestudent(
        first_name=ps_fname, last_name=ps_lname, ascii_free_email = p_email, ps_password = password
    )
  privatestudents.save()
  privatestudents.append(privatestudent)

# Create Public Profile
publicProfile = []
for i in range(1, 10):
    p_fname = fake.first_name()
    p_lname = fake.last_name()
    p_display = fake.display_name()
    p_email = fake.ascii_free_email()
    profile = publicProfile(
        first_name=p_fname, last_name=p_lname, display_name = p_display, ascii_free_email = p_email
    )
    publicProfile.save()
    publicProfiles.append(publicProfile)


# Create Reviews
reviews = []
for i in range(1, 10):
    a_title = fake.text(50)
    a_author = authors[fake.random_int(0, len(privatestudent)) - 1]
    a_review = fake.text(1000)
    review = Review(title=a_title, author=a_author, review=a_review)
    review.save()
    review.save()
    reviews.append(review)

# Create Services
services = []
for i in range(1, 400):
    a_services = books[fake.random_int(0, len(books)) - 1]
    a_imprint = fake.text(200)
    a_status = "a"
    instance = BookInstance(book=a_book, imprint=a_imprint, status=a_status)
    instance.save()
    instances.append(instance)

print("Genre:")
for g in Genre.objects.all():
    print(g)

print("\nAuthor:")
for a in Author.objects.all():
    print(a)

print("\nBook:")
for b in Book.objects.all():
    print(b)

print("\nBookInstance:")
for i in BookInstance.objects.all():
    print(i)

# Retrieve a random Service from model and print it.
books_count = Book.objects.count()
book = Book.objects.all()[fake.random_int(0, books_count - 1)]

print("\nExample Book:")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"ISBN: {book.isbn}")
print(f"Summary:\n{textwrap.fill(book.summary, 77)}")


username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
message = f"""
====================================================================
The database has been setup with the following credentials:
  username: {username}
  password: {password}
  email: {email}
You will need to use the username {username} and password {password}
to login to the administrative webapp in Django.
Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:
  $ python3 manage.py runserver 0.0.0.0:8080"
====================================================================
"""
print(message)
