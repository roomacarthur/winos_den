# Winos Den

To easily navigate please click the the small headings selector to the top left of this document. 

![navigation hint](https://github.com/roomacarthur/winos-den/blob/main/documentation/images/readme_navigation.png)




# Overview 
Winos Den has a strong standing reputation with it's customers and with this has managed to become the market leader for fine wines within it's local area. With the turbulent times over the past couple years the management have taken the decision to increase their presence online, opting to grow the business via the forms of E-commerce rather than to open a second outlet. 

With the move to push Winos Den online the business will benefit largely from the marketing outreach with promoting both the physical outlet and online store. An aggressive marketing strategy will be outlined below providing the business with the avenues needed to hit the ground running once the site goes live. 


#  User Experience (UX)

## Target Audience 

With Winos Den already being the market leader for fine wines in it's geographical area the idea to move online comes at zero loss. This move will allow the business to focus not just on it's local captive audience but to promote the business online to larger audiences and not be concerned about wasting money on potential customers who fall outside the local catchment area. 

The marketing strategy will push the boundaries on your typical audience and with the use of social media be able to push the business to audiences across the UK. The wine industry has a very large consumer base with any person over the age of 18 in the UK being a potential customer, thus targeting smaller groups can have it's pros a cons. When looking at age ranges, people over the age of 65 comprised the largest group of wine consumers, yet anyone can be a potential customer as wine is one of the most common gifts.

### User Stories

Following a strategy meeting with the management of Winos Den we created a base of user stories to cover most scenarios that may be encountered for all levels of site users. Below is some examples of the user stories we came up with during the meeting. All user stories can be viewed by clicking the link at the bottom of this section. 

| As A/An | I Can | So That|
| --- | ------ | ------ |
| Site User | Register an account | So That I can save my details and make purchases. |
| Site User | Register an account | So That I can save my details and make purchases. |
| Site User | Register an account | So That I can save my details and make purchases. |


For the purpose of development process these user stories have also been added to a kanban board. This is to aid in an agile workflow and streamline the development process as much as possible. 

### *User story kanban board can be viewed Here:* [LINK](https://github.com/roomacarthur/winos-den/projects/1)

## Strategy 

Working closely with Winos Den We aim to create a sleek and interactive platform which will be fully responsive and and allow for great user interaction (via CRUD) by allowing users to leave reviews, create carts and complete orders. 

**Our Ideal user:** Someone who has a passion for fine or is in the market for purchasing wine.

**Project Goal:** Provide a platform where users can easily navigate and purchase the products they require, Make this process as easy and effortless as possible to prompt users to want to return.

**Site Users Needs**

+ To be able to view the site on any device.
+ To be able to navigate the site with ease.
+ To easily register an account.
+ To be able to easily add items to a cart and checkout
+ To be able to log in and out.
+ To be able to update personal info.

**Project Objectives:**

+ Create a fully responsive web app. 
+ Allow for safe payments via Stripe
+ Create a stylish and easy to navigate web app.
+ Create a strong marketing strategy for instant traffic.
+ Streamline the buying process to keep customers captive. 


## Scope

Provided that the site is a success and the sales figures keep the business owners happy, the site will be able to flow through multiple iterations to keep the site interesting and moving forward with the times. With the first iteration of the Winos Den website we are aiming to launch quick so we will strongly focus on getting an MVP(minimum viable product) out as soon as possible. Even though we are aiming to launch with an MVP we know that any flaws/bugs could have a negative impact on potential customers so thorough testing will be carried out. 

### MVP release: 

+ User account creation and management 
+ Payment gateway - Stripe
+ Fully responsive
+ Crud functionality for users to leave reviews on products. 
+ Admin product management
+ User posted content moderation for admin.

### Future Releases/Updates:

+ Stock management for Admin.
+ More in depth user profile customisation e.g. profile picture, rating scores, 
+ Loyalty scheme for returning customer. 

## Structure

As the platform will be user driven, the structure is based on allowing users to be drawn to products and offers. Users will be prompted with messages when a hard action has been made e.g. "successfully logged in", "Review Posted Successfully", "You have logged out".

There Will be a news letter sign up promotion which will be located in different places from time to time but it will always have a constant place in the footer. 

+ Header

    + Winos Den Logo
    + Desktop and mobile navigation
    + User Access
    + 

+ Banner

    + Promotional offers

+ Messages

    + Display success messages for users
    + Messages based on users actions

+ Main content

    + provided in a block content this will be the Majority of site content.

+ Footer

    + Winos Den Location
    + Business Links (T&C, Privacy Policy etc.)
    + Links to socials
    + News Letter Sign up.


## Skeleton

### Wireframes

As an unwritten rule with all of my design work I opt for a mobile first approach, All of our initial planning with the management at winos den was based on designing the site in mobile first as we both believe that the majority of the consumer base will be mobile/tablet users. From this it is quite simple to extend the site to look great in desktop view also.


# *Add Wireframes Here*



### Database

## Surface

### Typography

### Colours

For Winos den we will be keeping inline with their current house style using the following colours:

- raisin-black: #272727ff;
- old-gold: #b3a400ff;
- ivory: #f1f7e6ff;
- viridian-green: #21a0a0ff;
- skobeloff: #046865ff;

![site colours]()
# Deployment

This project will be deployed to [Heroku](https://heroku.com) using the following outlined steps:

## Setting up Heroku Deployment

1. Navigate to [Heroku](https://heroku.com).
2. Create an account or log in.
   - If creating an account select **Python** as the **_Primary development language_**
3. Click the **New** button found top right of page and select **Create New App** from the dropdown menu.
4. Provide an app name **_this has to be unique_**
5. Select your region.
6. Click **Create App**
7. Navigate to the **Deploy tab**
8. Scroll down the page until you come across **Deployment Method**
9. Click **GitHub**
   - Connect your GitHub account if this is your first time.
10. Search for your projects GitHub Repository and click **connect**

## Automatic Deployment

When it comes to deployment there are two options **Automatic Deployment** or **Manual Deployment**.

For this project I have opted for **Automatic Deployment** as this allows for Heroku to re run the build and update my deployment every time I push code to my GitHub Repository.

To activate this:

1. Navigate to the **Deploy Tab**
2. Scroll down until you come across **Automatic Deployment**
3. Ensure that the correct branch is selected.
   - In Most cases this will be either main or master
   - In my case it will be main
4. Click **Enable Automatic Deploys**

The project is now deployed and will automatically re-run the build and deploy every time I push code to GitHub.

## Environment Variables

Within my local files my Environmental Variables are set within a env.py file, the details of this file are confidential and are added to the _.gitignore_ file so that they aren't publicly available. But because these files are not pushed to GitHub we need to enable the same Variables within Heroku for the application to run successfully.

# Credits