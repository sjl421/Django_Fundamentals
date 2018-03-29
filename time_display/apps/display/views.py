# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import gmtime, strftime, localtime

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "time": strftime("%b %d, %Y %I:%M %p", gmtime())#Oct 26, 2014 11:26AM
    }
    return render(request, 'display/index.html', context)

