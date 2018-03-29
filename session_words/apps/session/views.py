# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
# Create your views here.
def index(request):
    if 'word_list' not in request.session:
        request.session['word_list'] = []
      
    context = {
        'activities' : request.session['word_list'],
    }

        
    return render(request, 'session/index.html', context)

def add(request):
    request.session['word'] = request.POST['word']
    request.session['color'] = request.POST['color']
    request.session['date'] = datetime.strftime(datetime.now(), '%B %d, %Y')
    request.session['time'] = datetime.strftime(datetime.now(), '%I:%M:%S %p')

    if 'fonts' in request.POST:
        request.session['fonts'] = "big"
    else:
        request.session['fonts'] = "normal"

    request.session['word_list'].append({
        'word' : request.session['word'],
        'color' : request.session['color'],
        'date' : request.session['date'],
        'time' : request.session['time'],
        'fonts' : request.session['fonts'],
    })


    
    return redirect ('/')

def reset(request):
    request.session.clear()
    return redirect ('/')