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


