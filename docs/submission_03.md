# Jellyworks Team Submission
## Overview
Our app aims to match “buyers” to “sellers”. Each seller will have the opportunity to offer services like a haircut or a physical product such as a bike. We’ve limited our potential users—buyers and sellers—to students from UMass. When buyers select a seller to patronize, they “match” with that person i.e. they find their Sidehustle Match. The application is inspired by Etsy and Amazon. We are merging salient components of each e.g. the amatuer  marketplace fostered by Etsy and the intuitive and accessible UI of Amazon, to create something unique that focuses on college students. 

Since Project 2, we have modified our application’s models.py file and removed our custom “appUser” user model. Instead, we opted to extend Django’s built-in user model. We have also added functionality to our product pages via submitting reviews. Users can now also log in and log out of the application, with their profile being viewable while they are logged in.

## Team Members
Sarah Manlove, Edwood Brice, Chinh Do, Suzy Balles, and Jeff Reardon

## Video Link


## Design Overview
Our application’s login/logout and user interaction functionality is dependent on context. Subsequently, when a user is logged in and authenticated, they will be able to navigate to their profile and interact with forms that logged out users cannot. Additionally, on product pages, users are able to submit reviews that provide insight about what a particular vendor is offering. 

Each page that makes use of functionality that is specific to Project 3 is explained in detail below: 

### Home (index.html)
This is the application’s homepage. This page will feature services on the Sidehustles platform. When a user logs in, they will be brought to the login page. There they will enter their credentials. Afterwards, they will be redirected to the homepage. If users logout on the homepage, they will remain on the homepage.  In the dropdown menu in the top right corner, users will now be able to access the their profile via “My Profile”. 

### Browse (filtersearch.html)
The browse page can be accessed from the Home page. The Browse page allows users to filter the different types of services offered by things such as location, availability, and type of service (this is not yet implemented). If a user logs in or logs out on the browse page, they will remain on the browse page. 

### About Us (about.html)
This page is static and does not need data. If a user logs in or logs out on the about us page, they will remain on the about us page. 

### My Profile (profile.html)
The My Profile page enables users to make changes to their personal information (password, profile picture, first and last name). My Profile is only accessible after a user logs into the application (in the dropdown menu in the top right corner). If a user logs out while on the My Profile page, the page redirects to the Sidehustles home page. 

### Specific Service Page (product.html)
The product.html page focuses on a specific service, particularly the service that the user clicks on to be redirected to this page. Users are able to submit a review (via a form) on these pages. If the user logs in or out on this page, they will remain on this page. 

## Problems/Successes
Our team encountered a few roadblocks during this project. First, we had many issues with our data model. We had to work through using the User model that’s built into Django and extending it, and we ended up deleting appUser from our data model. Additionally, we had trouble finding times to meet up to work together because of work schedules and project due dates. We were thankful for having in-class working sessions as well as having a group that was willing to collaborate via Slack. 

Despite these problems, we were successful in implementing forms into our project. We learned from previous projects that we had to schedule meetup times early on in the project, and we are able to do this by using Slack and its pinned posts to keep track. We frequented library study rooms so often that we often reached our student limit for the week. With such an ambitious project in mind, we have slowly but surely made progress towards making Sidehustles a reality. 

## Team Choice
Sidehustles is college student oriented application. Unlike our sources of inspiration, Etsy and Amazon, it is likely that buyers and sellers will know each other from classes, meeting on campus, their networks, and etc. Subsequently, our application’s team choice is to implement a means of uploading, storing, and displaying profile pictures using the database. Profile pictures are a salient component on social media. By making use of them in our application, users will be able to identify people that they will interact with as they look for their Sidehustle match.
