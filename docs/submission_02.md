# Jellyworks Team Submission
## Overview
Our app aims to match “buyers” to “sellers”. Each seller will have the opportunity to offer services like a haircut or a physical product such as a bike. We’ve limited our potential users—buyers and sellers—to students from UMass. When buyers select a seller to patronize, they “match” with that person i.e. they find their Sidehustle Match. The application is inspired by Etsy and Amazon. We are merging salient components of each e.g. the amature marketplace fostered by Etsy and the intuitive and accessible UI of Amazon, to create something unique that focuses on college students. 

## Team Members
Sarah Manlove, Edwood Brice, Chinh Do, Suzy Balles, and Jeff Reardon

## Video Link
[3-5 minute video that provides an overview of your data model and how your data model connects to the code that you have implemented for that data model in your Django project. You should also show your application running.]  

## Design Overview
Our application’s data model is implemented in four salient components: publicProfile, appUser, Reviews, and Services.  We have attached a document visualizing it in Github ([Sidehustles Data Model](https://github.com/suzyballes/jellyworks/blob/master/docs/Data%20Model.pdf)). The URL routes of our app primarily manifest in the navbar with Home, Browse, About Us, and My Profile. Clicking on services on the Home page or on the Browse page will direct users to a specific service page. Each of the pages in the navbar and the linked user pages on the home page and the browse page make up our implemented UI views. Each page is explained below:


### Home (index.html)
This is the application’s homepage. This page will feature services on the Sidehustles platform. It will also allow buyers to search for a service of their interest (the search bar is a mock item, it is not functional).  When a buyer clickers on the “Match” button, they will be brought to a specific service page. In terms of the data model, this page indicates a services name, category, location, cost and the number of likes it accrues. Subsequently, these data are drawn from Services, Reviews, and publicProfile tables in the data model. 

### Browse (filtersearch.html)
The Browse page can be accessed from the Home page. The Browse page allows users to filter the different types of services offered by things such as location, availability, and type of service (this is not yet implemented but should be by the next iteration). This page is the place for users to find their service beyond just the few samples found on the homepage. After filtering on what kind of service the user wants, they are able to see a brief blurb about each service as well as its name, the person providing the service, and a link to the product page where more information can be found. In terms of the data model, the data on this page is dependent on the publicProfile and the Services tables.

### About Us (about.html)
This page is static and does not need data.

### My Profile (profile.html)
The My Profile page enables users to make changes to their personal information (email, password, profile picture, first and last name, display name, username/NetID). In it is current state, these functions are not operational. The data on this page are derived from the appUser and publicProfile tables. 

### Specific Service Page (product.html)
The product.html page focuses on a specific service, particularly the service that the user clicks on to be redirected to this page. This page describes the service in more detail, ranging from a photo for the product (uploaded up the owner) to the name of the service to price to reviews. This page’s data is derived from the Services and Reviews model. We have changed this from the original plan by taking out stars and the date that the review was posted as it would involve capturing data as the user submitted each review (and this is more of a stretch goal).


## Problems/Successes
Our team as a whole works quite well together when we can meet. Since we are a group of 5, it is hard for our group to be able to meet all at once. In order to compensate for that, we met up in smaller groups and kept everyone else up-to-date in the Slack. It was extremely helpful to have in-class time to work on the project as all of the members of our group could be together. In order to complete the next section of the project on time, we are going to improve more upon our communication in Slack and compare schedules earlier on in the process. We are also going to try and spread out our working sessions more in order to avoid late nights close to the deadline. 

One of our biggest issues was working with Github. We had many issues with merging branches and the command line. We were able to solve this issue by meeting up in person and working through the problem in order to ensure that it didn’t happen again. Once we met, we had very few commit issues. 

Another issue that we had during this project was connecting all of our faker data across all of the pages. Since we each worked on one specific page, connecting those pages (especially if they shared data) was a challenge that we should have anticipated earlier on in the process. In the future, we need to pay more attention to overlap earlier on in the process in order to avoid scrambling. 

As far as implementing our application, our team exhibited a synergy that exceeded everyone’s expectations. Each of us focused on working on our own pages. As a result, it was easy to focus because we each knew exactly what we had to tackle. Towards the end of the project, some of us managed to finish their pages before others. Subsequently, whenever one of us encountered an issue, they were able to help others get past their issues. 

