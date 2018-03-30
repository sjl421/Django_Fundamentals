# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

# Create your views here.
def index(request):
    if 'qty' not in request.session:
        request.session['qty'] = 0
        request.session['products'] = [
            {'item': "Dojo Tshirt", 'price' : 19.99},
            {'item': "Dojo Sweater", 'price':29.99},
            {'item': 'Dojo Cup', 'price':4.99},
            {'item': 'Algo book', 'price': 49.99}]
        
        request.session['order'] = 0

    return render(request, "amadon_app/index.html")

def buy(request):
    
    for i in request.session['products']:
        if i['item'] == request.POST['action']:
            request.session['total'] = float(i['price']) * int(request.POST['qty'])

    request.session['order'] += request.session['total']
    request.session['qty'] += int(request.POST['qty'])
    
        
    return redirect ('/amadon/checkout')


def checkout(request):
    return render(request, "amadon_app/checkout.html")

def reset(request):
    request.session.clear()
    return redirect ("/amadon")