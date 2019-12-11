# The framework for this website is Django project <h1>
## Authors <h2>
  - Huda Ali
  - Ryan Goode
  - John Heinz
  - Yanet Fonseca-Lopez
## Purpose <h2>
  The purpose of this website is for many reasons:
  1. Be able to search Ebay's database, based of keywords, and get back past sold items only. There's a maximum of 100 items that can be retrieved from Ebay's database. Another advantage is that the response content from Ebay goes back up to four months, whereas manually searching on Ebay on goes up to two months in the past.
  2. Make predictions, based of the keywords entered, using different prediction models. The three prediction models have different ways of making predictions. The prediction models used were: Artificial Neural Network, Multivariate Linear Regression and an 'Out of Sample' Step forward analysis.
  3. There is a Blog where users can post blogs. The edit and delete functions don't work currently and need fixing.
## Instructions <h2>
  The link to the instructions for how to use this software: [instructions](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/How_to_use.md)
## In order to build the project, from scratch, do the following: <h2>
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
    > NOTE: There was a bug (on certain computers with Windows OS) trying to run the 'python manage.py runserver' command. 
  The error will read 'Error: [WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions'. 
  The fix to this is to instead run the server on port 8080, using this command instead: python manage.py runserver 8080
  - then bring up a browser window and type in the url: localhost:8000 (or http://127.0.0.1:8000)
    > NOTE: There was a bug using Google chrome/chromium to login to Django admin page (instead use Internet Explorer, Safari, etc., another browser other than Google Chrome/Chromium)
  - you should see the rocket ship on the page of local port 8000
  - Congrats! You just went on your way to becoming a web developer!
  
## In order to build the project, from forking this repository and downloading, do the following: <h2>
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
  - Make sure that you don't install Django yet. You also want to make sure that you have pip and virtualenv already installed on your computer
  - then create the virtual environment by using: virtualenv (name of your virtual environment)
  - activate your virtualenv using:
     1. (name of virtualenv)\Scripts\activate (for Windows)
     2. source bin/activate (for macOS)
  - download all the dependencies by typing on the command line: pip install -r requirements.txt
  - go inside 'django_webiste' by using: cd django_website
  - Once inside the 'django_website' directory, type on the command line:
  1. python manage.py makemigrations (then press ENTER on the keyboard)
  2. python manage.py migrate (then press ENTER on the keyboard)
  > NOTE: You need to make the migrations in order to use certain parts of the website, like the blog for instance...
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
  - If you run 'python manage.py runserver' and get an error that reads 'Error: [WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions', instead use: python manage.py runserver 8080 (AND make sure that you run localhost:8080 instead of localhost:8000)
  
## Images of website pages/examples: <h2>
  - Example of Home Page while user is not logged in:
  ![home page example](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/home_page_example.PNG)
  - Example of Contact Us Page:
  ![contact us page example](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/contact_us_example.PNG)
  - Three examples of About Us Page:
  ![about us page example 1](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/about_us_page_example_1.PNG)
  ![about us page example 2](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/about_us_page_example_2.PNG)
  ![about us page example 2](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/about_us_page_example_3.PNG)
  - Example of About Website Page:
  ![about website example](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/about_website_example.PNG)
  - Example of Directions Page:
  ![directions example](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/directions_page_example.PNG)
  - Example of main Blog Page:
  ![blog list example](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/blog_list_view_page_example.PNG)
  - Example of Blog detail Page:
  ![blog detail example](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/blog_detail_view_example.PNG)
  - Example of create a new Blog Page:
  ![blog create example](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/create_blog_page_example.PNG)
  - Two example images of the Display Graphs Page:
  ![graphs page example 1](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/graph_page_example_1.PNG)
  ![graphs page example 2](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/graph_page_example_2.PNG)
  - Example of create account page:
  ![create account example](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/signup_example.PNG)
  - Example of login page:
  ![login example](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/login_page_example.PNG)
  - Example of using the keyword search on the Home Page:
  ![example 1 use keywords](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/cards_example1_how_to_use_1.PNG)
  - Example of using the keyword search on the Home Page, using both keywords and using the dash operator to exclude certain keywords:
  ![example 2 use keywords](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/cards_example1_how_to_use_2.PNG)
  - Image showing the 'Past Sales' dataframe. This is used to vett out unwanted results from the keyword search:
  ![example past sales dataframe](https://github.com/IUS-CS/project-ordo_ab_chao/blob/master/doc/How_to_use_documentation/images/past_sales_dataframe.PNG)
