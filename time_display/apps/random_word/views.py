# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1

    context = {
        'word' : get_random_string(length=14)
    }
    return render(request, 'random_word/index.html', context)

def generate(request):
    request.session['counter'] += 1
    
    return redirect (index)

def reset(request):
    request.session.clear()
    return redirect (index)