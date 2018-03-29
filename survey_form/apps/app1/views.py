# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request, 'app1/index.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['desc'] = request.POST['desc']
    request.session['counter'] += 1
     
    return redirect ('/result')

def result(request):
    return render(request, 'app1/result.html')