# The framework for this website is Django project <h1>
## Instructions <h2>
  The link to the instructions for how to use this software: [instructions](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/How_to_use.md)
## Purpose <h2>
  The purpose of this website is for many reasons:
  1. Be able to search Ebay's database, based of keywords, and get back past sold items only. There's a maximum of 100 items that can be retrieved from Ebay's database. Another advantage is that the response content from Ebay goes back up to four months, whereas manually searching on Ebay on goes up to two months in the past.
  2. Make predictions, based of the keywords entered, using different prediction models. The three prediction models have different ways of making predictions. The prediction models used were: Artificial Neural Network, Multivariate Linear Regression and an 'Out of Sample' Step forward analysis.
## In order to build the project, from scratch, do the following: <h2>
  > "using" means use the command line in the following instructions...
  - download pip (may need "easy-install" to do so, if so download easy-install first to install pip)
  - download virtualenv
  - download one of the following (if not already installed):
     1. Anaconda package (with Anaconda Navigator, Spyder are only needed) OR
     2. sublime text IDE OR
     3. PyCharm IDE
  - create a directory, such as 'dev' or 'development'
  - go inside the 'dev' folder and make a virtual environment using: virtualenv (name of your environment here)
  - activate your virtualenv using:
     1. (name of virtualenv)\Scripts\activate (for Windows)
     2. source bin/activate (for macOS)
  - download django using: pip install django==2.2
  - create 'src' folder using: mkdir src
  - go into the 'src' folder using: cd src
  - once inside, make the django project using: django-admin startproject (name of your django website here)
  - (optional) you can then create an app using: django-admin startapp (name of your app, i.e. - homepage, aboutme, etc.)
  - then type on the command line: python manage.py runserver
  - then bring up a browser window and type in the url: localhost:8000 (or http://127.0.0.1:8000)
    > NOTE: There was a bug using Google chrome/chromium to login to Django admin page (instead use Internet Explorer, Safari, etc., another browser other than Google Chrome/Chromium)
  - you should see the rocket ship on the page of local port 8000
  - Congrats! You just went on your way to becoming a web developer!
  
## In order to build the project, from forking this repository and downloading, do the following: <h2>
  > "using" means use the command line in the following instructions...
  - download pip (may need "easy-install" to do so, if so download easy-install first to install pip)
  - download virtualenv
  - download one of the following (if not already installed):
     1. Anaconda package (with Anaconda Navigator, Spyder are only needed) OR
     2. sublime text IDE OR
     3. PyCharm IDE
  - create a directory, such as 'dev' or 'development'
  - get inside the 'dev' directory by using: cd dev
  - then run the command line using: git clone (address of clone/download for this repository)
  - then change dir to project-ordo_ab_chao by using: cd project-ordo_ab_chao
  - then change dir to 'src' by using: cd src
  - then download new virtualenv by using the command line again: pip install virtualenv
  - then create the virtual environment by using: virtualenv (name of your virtual environment)
  - activate your virtualenv using:
     1. (name of virtualenv)\Scripts\activate (for Windows)
     2. source bin/activate (for macOS)
  - download all the dependencies by typing on the command line: pip install -r requirements.txt
  - go inside 'django_webiste' by using: cd django_website
  - then, while in the 'django_website' directory, use this on the command line: python manage.py runserver
    > NOTE: There was a bug (on certain computers with Windows OS) trying to run the 'python manage.py runserver' command. 
  The error will read 'Error: [WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions'. 
  The fix to this is to instead run the server on port 8080, using this command instead: python manage.py runserver 8080
  - then bring up a browser window and type in the url: localhost:8000 (or http://127.0.0.1:8000)
    > NOTE: There was a bug using Google chrome/chromium to login to Django admin page (instead use Internet Explorer, Safari, etc., another browser other than Google Chrome/Chromium)
  - You will then see the homepage of ordo_ab_chao's website (under construction right now...)
  - (optional) While in the same directory as 'django_website' with manage.py, run this on the command line to do unit testing: 

  python manage.py test<br>

  OR
 
  manage.py test
 
  
## Known bugs: <h2>
  - When using Windows 10, trying to sign into the django-admin site in Google Chrome or Google Chromium causes the browser to load indefinitely. Chrome/Chromium had no issues when running 'localhost:8000', but would never load for django-admin login page. For the Django-admin login page, use another browser like Internet Explorer, Safari, Mozilla, Bing, etc...
