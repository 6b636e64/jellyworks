import textwrap
from random import *
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from faker import Faker
from faker.providers import person, internet, date_time, address, lorem

from users.models import CustomUser
from sidehustles.models import Services, publicProfile, appUser, Reviews

fake = Faker()
  
# Create 10 fake Public Profile
publicProfiles = []
for i in range(1, 10):
    public_fname = fake.first_name()
    public_lname = fake.last_name()
    public_displayname = fake.name()
    public_email = fake.ascii_free_email()
    
    profile = publicProfile(
        public_fname = public_fname, public_lname = public_lname, public_displayname = public_displayname,  public_email =  public_email 
    )
    profile.save()
    publicProfiles.append(profile)


 # Create 10 fake users 
users = []
for i in range(1,10):
    user_fname = fake.first_name()
    user_lname = fake.last_name()
    user_unique_email = fake.ascii_free_email()
    user_password = fake.password()
    user = appUser(user_fname = user_fname, user_lname = user_lname, user_unique_email = user_unique_email, user_password = user_password)
    user.save()
    users.append(user)   
  
  
# Create Services
services = []
for i in range(1, 5):
    service_name = fake.text(20)
    public_displayname = fake.name()
    service_cost = int(fake.random_number())
    service_category = fake.text(200)
    service_location = fake.street_address()
    service_proficiency = int(fake.random_number())
    skill_info = fake.job()
    x = randint(0, len(Services.SKILL_TYPE)-1)
    skill = Services.SKILL_TYPE[x][0]
    x = randint(0, len(Services.LOCATION_TYPE)-1)
    location = Services.LOCATION_TYPE[x][0]
    x = randint(0, len(Services.AVAILABILITY_TYPE)-1)
    availability = Services.AVAILABILITY_TYPE[x][0]
    service = Services(public_displayname = public_displayname, service_name = service_name, service_cost = service_cost, service_category = service_category, service_location = service_location, service_proficiency = service_proficiency, skill_info = skill_info, skill = skill, location = location, availability = availability)
    service.save()
    services.append(service)

# Create Reviews
reviews = []
for i in range(1, 10):
    review_like_count = int(fake.random_number())
    review_text = fake.text(1000)
    review_date_posted = fake.date()
    r_service = services[fake.random_int(0, len(services)) - 1]
    review = Reviews(service = r_service, review_like_count = review_like_count, review_text = review_text, review_date_posted = review_date_posted)
    review.save()
    reviews.append(review)

print("User:")
for u in appUser.objects.all():
    print(u)

print("\nPublic Profile:")
for p in publicProfile.objects.all():
    print(p)

print("\nReviews:")
for r in Reviews.objects.all():
    print(r)

print("\nServices:")
for s in Services.objects.all():
    print(s)
'''
print("\nExample Service:")
print(f"User: {service.user}")
print(f"Public Profile: {service.profile}")
print(f"Review: {service.review}")
print(f"Service: {service.service_name}")
'''

username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = CustomUser.objects.create_user(username, email, password)
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
