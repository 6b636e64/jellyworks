import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from faker import Faker

from Sidehustles.models import PublicProfile, Services, User, Reviews

fake = Faker()
  
# Create 10 fake Public Profile
publicProfiles = []
for i in range(1, 10):
    public_fname = fake.first_name()
    public_lname = fake.last_name()
    public_displayname = fake.display_name()
    public_email = fake.ascii_free_email()
    profile = publicProfile(
        first_name = public_fname, public_lname = public_lname, public_displayname = public_displayname,  public_email =  public_email
    )
    publicProfile.save()
    publicProfiles.append(publicProfile)


 # Create 10 fake users 
users = []
for i in range(1,10):
    user_fname = fake.first_name()
    user_lname = fake.last_name()
    user_unique_email = fake.ascii_free_email()
    user_password = fake.password()
    user = user(user_fname = user_fname, user_lname = user_lname, user_unique_email = user_unique_email, user_password = user_password)
    user.save()
    users.append(user)   
  

# Create Reviews
reviews = []
for i in range(1, 10):
    
    review_like_count = fake.random_number()
    review_star_count = fake.random_number() 
    review_text = fake.text(1000)
    review_date_posted = fake.date()
    review = review(review_like_count = review_like_count, review_star_count = review_star_count, review_text = review_text, review_date_posted = review_date_posted)
    review.save()
    reviews.append(review)
  
  
# Create Services
services = []
for i in range(1, 10):
    service_name = fake.text(200)
    service_cost = fake.random.number()
    service_category = fake.text(200)
    service_location = fake.street_address()
    service_proficiency = fake.random_uppercase_letter()
    service_reviews = fake.text(500)
    service = services(service_name = service_name, service_cost = service_cost, service_category = service_category, service_location = service_location, service_location = service_location, 
                      service_proficiency = service_proficiency, service_reviews = service_reviews)
    service.save()
    services.append(service)

print("User:")
for u in User.objects.all():
    print(u)

print("\nPublic Profile:")
for p in publicProfile.objects.all():
    print(p)

print("\nReviews:")
for r in reviews.objects.all():
    print(r)

print("\nServices:")
for s in services.objects.all():
    print(s)

print("\nExample Service:")
print(f"User: {service.user}")
print(f"Public Profile: {service.profile}")
print(f"Review: {service.review}")
print(f"Service: {service.service_name}")


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
