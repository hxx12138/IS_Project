from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req, 'index.html')

def index2(req):

    return render(req, 'index2.html')