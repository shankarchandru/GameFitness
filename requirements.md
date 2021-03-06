**GameFitness Requirements Overview**

Version: 1.0

Release date: 6 November 2019

Key features: login to the webside, store user login information

**Functional Requirements**

-Python 3.7 (install here: https://www.python.org/downloads/release/python-374/)
-Git (install here: https://gist.github.com/derhuerst/1b15ff4652a867391f03)
-Django 2.2 (installed in python via pip)
-Pytest 5.2.1 (installed in python via pip)
-virtual environment (installed in python via pip)

**Functional Requirements Instructions**

1. install Python 3.7 onto your machine
2. install Git onto your machine
3. On the command line interface, navigate into the folder you are interested in saving your software in
4. clone the GameFitness github repository onto your machine
    a. under the code tab in the GameFitness repository, locate the **clone or download** button and copy the repository link
    b. on your machine, in the command line interface, clone the repository ("git clone <repsitory link>")
5. on the command line interface, install Virtual Environment
    a. write the command ("pip install virtualenv")
    b. create a virtual environment (Mac and Linux: "python3 -m venv env", Windows: "python -venv env")
    c. activate virtual enviornment (Mac and Linux: "source env/bin/activate", Windows: ".\env\Scripts\activate")  
6. on the command line interface, install pytest ("pip install pytest")
7. on the command line interface, install django ("pip install django")
8. on the command line interface, install pytest-django ("pip install pytest-django")
9. on the command line interface, install django ("pip install mixer")
10. On the command line interface, navigate into the folder containing the manage.py file
11. on the command line interface, type "python manage.py runserver". This should now allow you to run the website on your local machine
12. open up a web browser and type "http://localhost:8000/"
13. the website should now be loaded and running on your local machine!

**User Doc**
1. After running django, open up your web browers and type "http://localhost:8000/". This will take you to the homepage
2. On the homepage, navigate to the top right hand corner and click on the login icon (it is an image of a stickfigure head and body)
3. Click on sign in and you will be redireced to a sign in page
4. Fill out the sign in critera and submit your information. You will be redirected to a page where you can choose a sport
5. After clicking on a sport, you will be redirected to the exercises page, which will contain the exercises you will complete

** Test Doc**
1. After configuring pytest for django plugin and mixer plugin as part of Functional Requirements Instructions, all tests for the project can be navigated to gamefitnessweb/gamefitnessweb and invoked by calling pytest
