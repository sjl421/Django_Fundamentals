Assignment: Time Display
Create a Django app called time_display according to the below wireframe.

![alt tag](https://user-images.githubusercontent.com/32435667/38094442-bb467512-333b-11e8-95b5-ddc8015e9db2.png)

In timedisplay's controller (apps/time_display/views.py), create a method named index.

When you go to the URL localhost:8000 or localhost:8000/time_display/ this should run the index method in your controller file, (views.py). Have that method render a template that displays the current date and time.

from django.shortcuts import render, HttpResponse, redirect
def yourMethodFromUrls(request):
  context = {
  "somekey":"somevalue"
  }
  return render(request,'appname/page.html', context)
The keys of your context dictionary are available to be accessed on your page.html.

<div class="line">{{somekey}}</div>
The above line will print out “somevalue” on your HTML!

To see how you can get the current time in Python, you could for example make sure views.py import gmtime, strftime from 'time' and pass the appropriate string to the render method.  For example, your views.py could look like:

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
  context = {
  "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
  }
  return render(request,'appname/index.html', context)
To learn more about strftime, see https://docs.python.org/3.3/library/time.html?highlight=time.strftime#time.strftime

Please also see https://stackoverflow.com/questions/466345/converting-string-into-datetime

Assignment: Random Word Generator
Create a new Django app called 'random_word'. Your template will show a random word with 14 characters in length.

The first time you use this app, it should say 'attempt #1'. Each time you generate a new random keyword, it should increment the attempt figure. The purpose of this assignment is to reinforce your understanding of form submissions and session. Don't spend too much time on the random word generator, it's okay if your random word is not a real word.

Also when an http request is sent to, say, localhost:8000/random_word/reset, have it reset the counter for the attempt and redirect back to localhost:8000/random_word.

![alt tag](https://user-images.githubusercontent.com/32435667/38100956-d77c827e-334c-11e8-8df7-ef5d320ade65.png)

Hint for generating a random word: See https://stackoverflow.com/questions/25943850/django-package-to-generate-random-alphanumeric-string

There are many ways you could create a random string, but one way you could do this is by

importing get_random_string from django.utils.crypto (remember that you can import other libraries/modules in your views.py or any other python files)
use get_random_string(length=14) to get a random string of length 14
As the goal of this assignment is to really help you get familiar with creating a new app, setting up routing, views, templates, etc, we've given you some hints. :)