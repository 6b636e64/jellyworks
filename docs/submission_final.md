# Jellyworks
## Side Hustles
### Fall 2018

#### Overview of Our Application
Our app aims to match “buyers” to “sellers”. Each seller will have the opportunity to offer services like a haircut or a physical product such as a bike. We’ve limited our potential users—buyers and sellers—to students from UMass. When buyers select a seller to patronize, they “match” with that person i.e. they find their Side Hustle Match. The application is inspired by Etsy and Amazon. We are merging salient components of each e.g. the amateur marketplace fostered by Etsy and the intuitive and accessible UI of Amazon, to create something unique that focuses on college students.

#### Team Members 
Edwood Brice, Chinh Do, Suzy Balles, Sarah Manlove, and Jeff Reardon

#### User Interface
##### Home (index.html)
[See index.html](https://docs.google.com/presentation/d/13AwvAlMSheO8p57olAXyON-s7m54rFnKWu-zINYwF4M/edit?usp=sharing)
This is the application’s homepage. This page will feature services on the Side Hustles platform. It will also allow buyers to search for a service of their interest (the search bar is a mock item, it is not functional).  When a buyer clickers on the “Match” button, they are brought to a specific service page. In terms of the data model, this page indicates a services name, category, location, cost and the number of likes it accrues.

##### Browse (filtersearch.html)
[See filtersearch.html](https://docs.google.com/presentation/d/1TqYybVUPP-yMWcBrDa7fzG5kuGkxGqaqMfStML4WWNU/edit?usp=sharing)
The Browse page can be accessed from the Home page. The Browse page allows users to filter the different types of services offered by things such as location, availability, and type of service (this is not yet implemented but should be by the next iteration). This page is the place for users to find their service beyond just the few samples found on the homepage. After filtering on what kind of service the user wants, they are able to see a brief blurb about each service as well as its name, the person providing the service, and a link to the product page where more information can be found.

##### About Us (about.html)
This page is static and does not need data.

##### My Profile (profile.html)
[See profile.html](https://docs.google.com/presentation/d/1-CbIoMj_4-Qt6bJk48lTv5J3hZQ_3HZbM1br_q5-OIQ/edit?usp=sharing)
The My Profile page enables users to make changes to their personal information (email, password, profile picture, first and last name, username/NetID). 

##### Specific Service Page (product.html)
[See product.html](https://docs.google.com/presentation/d/1tV1oYvCJs7TnhmAxvQDywLC2mlTY-kI3gs0V36WHGY8/edit?usp=sharing)
The product.html page focuses on a specific service, particularly the service that the user clicks on to be redirected to this page. This page describes the service in more detail, ranging from a photo for the product (uploaded up the owner) to the name of the service to price to reviews. This page’s data is derived from the Services and Reviews model. 

#### Data Model
[Data Model Diagram](https://docs.google.com/presentation/d/19vwKNK6Vyh6MzYC5Ext7m2ycqMJo5GNv0LoV1OwoGjg/edit?usp=sharing)

#### CustomUser: Model representing a user (extends Django’s built in User model - it can be found in users/models.py)

image: contains profile picture associated with a user

first_name: contains the user’s first name (built-in)

last_name: contains the user’s last name (built-in)

username: contains the user’s last name (built-in)

#### Reviews: Model representing a customer review

Service: contains the title of the service

User: contains the name of the user associated with the review

Review_like_count: contains the number of likes that a service has

review_text: contains the text that users input for a review via a form

Editable_text: This is not being used. Review_text serves this purpose

review_date_posted: contains the date a review was posted

#### Services: Model representing a service characteristics 

service_name: contains the name of the service

service_cost: contains the cost of a service

service_category: contains a service’s category 

service_location: contains the location of a service

service_proficiency: contains a seller’s numerical proficiency level

skill_info: contains a description of the skill/service   

SKILL_TYPE: contains a pre-coded list of skill types

skill: converted SKILL_TYPE list into choosable options

LOCATION_TYPE: contains a pre-coded list of locations

location: converted LOCATION_TYPE list into choosable options

AVAILIBILITY_TYPE: contains pre-coded list of days of the week

availability: converted AVAILABILITY-TYPE list into choosable options

### URL Routes/Mapping
#### path('', views.index, name='index') 
Side Hustles home screen 

#### path('profile/', views.profile, name="profile") 
Profile page where users can change details about themselves. Must be logged in.  

#### path('filtersearch/', views.search, name="filtersearch") 
Page where users can filter and search for what they want based on their selected criteria.

#### path('product/<int:pk>', views.product, name="product") 
Specific product page where users can leave reviews. Must be logged in to leave reviews 

#### path('about/', views.about, name="about") 
Static “About” page

#### path('change_password/', views.change_password, name="change_password") 
Form to change password. You must be logged in to change your password.

#### path('sidehustles/profile_changes/', views.profile_changes, name="profile_changes") 
Form to change first and last names. You must be logged in to change your first and last name.

#### path('change_picture', views.upload_image, name="change_picture") 
Form to upload image to serve as new profile picture. You must be logged in to change your profile picture.

#### path('new_account', views.new_account, name="new_account") 
Non-users can make an account here. You cannot be logged in.

#### Authentication/Authorization
Our application’s login/logout and user interaction functionality is dependent on context. Subsequently, when a user is logged in and authenticated, they will be able to navigate to their profile and interact with forms that logged out users cannot. Additionally, on product pages, users are able to submit reviews that provide insight about what a particular vendor is offering. 
Each page that makes use of functionality that is specific to authentication/authorization is explained in detail below: 

##### Home (index.html)
This is the application’s homepage. This page will feature services on the Sidehustles platform. When a user logs in, they will be brought to the login page. There they will enter their credentials. Afterwards, they will be redirected to the homepage. If users logout on the homepage, they will remain on the homepage.  In the dropdown menu in the top right corner, users will now be able to access the their profile via “My Profile”. 

##### Browse (filtersearch.html)
The browse page can be accessed from the Home page. The Browse page allows users to filter the different types of services offered by things such as location, availability, and type of service (this is not yet implemented). If a user logs in or logs out on the browse page, they will remain on the browse page. 

##### About Us (about.html)
This page is static and does not need data. If a user logs in or logs out on the about us page, they will remain on the about us page. 

##### My Profile (profile.html)
The My Profile page enables users to make changes to their personal information (password, profile picture, first and last name). My Profile is only accessible after a user logs into the application (in the dropdown menu in the top right corner). If a user logs out while on the My Profile page, the page redirects to the Sidehustles home page. 

##### Specific Service Page (product.html)
The product.html page focuses on a specific service, particularly the service that the user clicks on to be redirected to this page. Users are able to submit a review (via a form) on these pages. If the user logs in or out on this page, they will remain on this page. 

#### Team Choice
Side Hustles is college student oriented application. Unlike our sources of inspiration, Etsy and Amazon, it is likely that buyers and sellers will know each other from classes, meeting on campus, their networks, and etc. Subsequently, our application’s team choice is to implement a means of uploading, storing, and displaying profile pictures using the database. Profile pictures are a salient component on social media. By making use of them in our application, users will be able to identify people that they will interact with as they look for their Side Hustle match. 

This change affects our Profile page, as the photo will replace the placeholder image that was on the page up to this point. We implemented the Team Choice by adding an Image File to our Custom User model and pulling the appropriate profile picture into the profile template.

#### Conclusion
Jellyworks has come a long way. Side Hustles has grown significantly since the first project.  Throughout this project, we had a fine-tuned focus and idea of what we wanted to implement because of the previous projects. Subsequently, we were all on the same page: we needed to get our team choice, uploading profile pictures, off the ground. To accomplish this, we read the Mozilla documentation and pulled together all the resources we could find. We ultimately realized, however, that our model structure and decision to extend the default Django user model complicated things. As a result, although we understood the various tutorials we came across, things were not working as they were supposed to (at first). For one thing, we did not understanding how to link particular images to particular users when the default user has been extended. Figuring out how to refer to the extended model was a team effort. Everyone looked into ways to get our application working until a team member was able to push through and find a solution.  

Over the course of the semester, our team has worked hard to learn Django and implement our idea. There were times of frustration, such as when we couldn’t fully grasp a topic e.g. reflecting our idea in a model structure, associated information with particular services, implementing forms throughout the application, and etc.  and relied on internet tutorial after internet tutorial. If we had more time or if we had to do this class again, we probably would have laid out our data model differently, erased ancient non-functional code earlier (in lieu of letting it rot and confuse us later on), and commented more of our code (because much of our code made little sense after awhile). With that being said, there were also times of pride, such as when we were finally able to submit a project or when our semester-long efforts culminated in a successful pitch.

Our team had little-to-no web programming experience coming into this class. That being said, Jellyworks accomplished a lot in these short months. We worked well as a team.  
