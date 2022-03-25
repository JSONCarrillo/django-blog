# Jason Carrillo Blog

A blog created using Django to showcase things I've learned, or anything I find interesting in the tech space, primarily focusing on technology and linux

For security reasons, I have added my settings.py file to my gitignore.

This blog is connected to a postgreSQL database I made in a docker container on my home server

## Table of Contents

1. Installation
2. Apps
3. Models
4. Views

## Installation

To install on your machine run the command:

    git clone https://github.com/JSONCarrillo/blog.git

Once thats downloaded, it is recommended to activate a virtual environment and then run command:
    
    pip install -r dependencies.txt

From there, you will want to create your own settings.py file

### Dependencies

1. django | for obvious reasons
2. django-ckeditor | for creating a verbose text editor for creating and editing blog posts
3. Pillow | for managing media
4. psycopg2-binary | for connecting to postgre database

## Apps

This section will explain the function of each app

### blog

This is the main application which houses the settings, urls, asgi, wsgi, and init files

### blogApp

This is the blog itself, in all of its glory. It contains views and models for blog posts, profiles, categories, and comments.

### media

This app manages all images used throughout the app for blog posts and profile pics.

### members

This app handles login and logout functionality as well as the password hashing for users

## Models

### Post

This model contains fields for the following:

1. Post name
2. Category
3. Author
4. Post date
5. Title for the html title tag
6. Article hook for when a user views the post card from the home/category page
7. Header image
8. Alt tag for the header image
9. The article content itself

### Category

This is the category model which stores the all the categories created

### Profile

This stores information of all user created profile and extends off the 'User' model from django

### Comments

This stores all comments made by users with timestamps as well as its foreign keys set to the user that created the comment and the post the comment was made on

## Views

There are views for the following:

1. Add category
2. Add post
3. Article
4. Delete post
5. Index (Home Page)
6. Update post
7. User profile
8. Login/Logout