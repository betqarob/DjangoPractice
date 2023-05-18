# DJango Project! Polling App

So for the most part, this project serves as a way for me to remember how to work with the DJango web framework. I'm following a guide from the DJango wesbite in order to remember the steps and how everything functions all together.

Thus, this README file is going to serve step of how to do changes and make everything flow together!

From here you'll just see a more step by step of what I have to do during every change I commit in terms of terminal commands that I will be running!

```
something like this if you will
```

This will function as a bases of me coming back and working with Django when its needed.

(Small Side Note! This will also help me relearn how to work with git and how I can push any sort of changes into github remotely)

## Setting everything up to work with Django

When starting a DJango project, you will want to create a new folder that will house all the files that will be used in this project! So, for the most part, its needed to create a folder where everything will be kept.

From there, you will need to open command prompt and move into the directory of the folder. 

However before that, you will want to make sure that you have DJango installed!

You will do that by simply typing into your command prompt (or Terminal) 

```
django-admin --version
```

If you get a version number, that means that DJango is installed and you are good to go! 

Now,  in order to install all the files needed for the project, you will need to do:

```
django-admin startproject [name of the project]
```

On my end,  I just called the project something silly so I called it "ElBook", which I will be usiong to do a refresher of Django!

You will see that this will create another folder inside your directory and that will contain all the python files you will be using!

To check that it runs properly, do:

```
python manage.py runserver
```

and this will create a local host server where you can see the website display on the development server that is given! 


##Creating one of many apps inside of your main project

Since we know that the website is working properly, we can now get started with the being able to display text onto the website instead of the Django message that comes up when we run our server for the first time.

So, to start it off,  lets start off by making an app inside of our project! To do this we need to do 

```
python manage.py startapp [name of your app]
```

Once that is done, you will see a new folder being created that will have similar files inside of it! This will be the app that will be used in order to display things onto the Django website.

So, going into the views.py file inside of the new folder that was created, we are going to add a few lines of code into it, that way we are able to see text appear on the screen instead of Django's confirmation page.

```
from django.http import HttpResponse

# this will display the text that we type
def index(request):
    return HttpResponse("Hello World! Just testing something new here!")
```

This is an easy way to get text to display and it will be changed as this project continues. 

To see what we did, however, we need add a url path that we can use in order to see the view. As you can see, there is no urls.py file in the poll folder that we made, meaning that you'll have to create the file and simply call it urls.py!

Once that is done, you'll want to add this following line of code:

```
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index),
]
```

Now that we have this in our polls, we'll want to connect this to the root folder, which DOES contain a url file that we can edit.

You'll want to add theses lines of code into the urls.py within the root folder:

```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls)),
    path("admin/", admin.site.urls)
]
```

If you refresh the page, you will find that the Django page will no longer show and is now replaced with the text that we typed! This is the view that we created!