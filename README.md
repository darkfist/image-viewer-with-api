[![Python](https://img.shields.io/badge/Python-3.6-brightgreen.svg)](http://www.python.org/download/)
# Django Image Gallery

A simple Image Gallery with API made with Python and Django.

## Description

Django Image Gallery with API is the extention of Django Image Gallery project where users can register and then upload their images with the API also. These images can be viewed by anyone.
Accepted Image Formats : JPEG, JPG, PNG, GIF

## Installation and Dependencies

After cloning the repository on your machine move into the ```src\``` directory and install the dependencies by ```pip install requirements.txt```


##### Connecting to database:
This application requires MySQL Database.
Check [this link](https://goo.gl/85wAeM) if you don't know how to install MySQL.

Create a database with name "imagesDB" and set the MySQL username and password in the ```base.py``` file present at ```src\image_gallery\settings```.

## Starting the App
from the ```src\``` directory run the following commands:
```
~/src$ python3 manage.py makemigrations
~/src$ python3 manage.py migrate
~/src$ python3 manage.py collectstatic
~/src$ python3 manage.py createsuperuser
```
then enter the details which will be asked, like username, email and password.

Now the app is fully setup.
Run the following command to start the app in your browser:
```
~/src$ python manage.py runserver
```
Now just go to ```http://127.0.0.1:8000/api/images``` in your browser to access the app.
You can also go to ```http://127.0.0.1:8000/admin``` in your browser and login with your 'superuser' credentials (created in previous step) to access the admin panel.

## Features

- Users can register for a new account.
- Users can login and upload images on behalf of themselves.
- Users can upload multiple images at a time (Max=10).
- Users can give title and description to the images.
- Users can view the images (with or without login).
- Users can delete their own images.

## API Features

- Users can get all images. (BASE_URL/api/images)
- Users can get a particular image by passing the ID. (BASE_URL/api/images/<image_id>)
- Users can get all images of a particular user. (BASE_URL/api/images/?user=<username>)
- Users can upload an image. (BASE_URL/api/images/create)
- Users can update an image. (BASE_URL/api/images/<image_id>/edit)
- Users can delete an image. (BASE_URL/api/images/<image_id>/delete)

## Library's Used

- [Django Rest Framework](https://www.django-rest-framework.org/)

## Development

This project was made as a screening task for the [FOSSEE Fellowship 2019 Collaborative Communities](https://fossee.in/)