# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random


# Create your views here.
def index(request):

    if 'counter' not in request.session:
        request.session['counter'] = 0
        request.session['running_total'] = 0
        request.session['desc'] = []
        request.session['activities'] = ""

    ## add content

    return render(request, 'ninja/index.html')


def process(request):
    if request.POST['building'] == "farm":
        x = random.randrange(10, 21)
        request.session['activities'] = "Earned {} golds from the farm! {}".format(x, datetime.now())

    elif request.POST['building'] == "cave":
        x = random.randrange(5, 10)
        request.session['activities'] = "Earned {} golds from the cave! {}".format(x, datetime.now())
        
    elif request.POST['building'] == "house":
        x = random.randrange(2, 5)
        request.session['activities'] = "Earned {} golds from the house! {}".format(x, datetime.now())

    elif request.POST['building'] == "casino":
        x = random.randrange(-50, 51)
        if x < 0:
            request.session['activities'] = "Entered a casino and lost {} golds..Ouch! {}".format(x, datetime.now())
        elif x > 0:
            request.session['activities'] = "Earned {} golds from the casino! {}".format(x, datetime.now())


    request.session['running_total'] += x
    print "Running total is {}".format(request.session['running_total'])
    request.session['desc'].append(request.session['activities'])
    print request.session['activities']
    print request.session['desc']
    request.session['counter'] += 1
    return redirect ('/')
        

def reset(request):
    request.session.clear()
    return redirect ('/')