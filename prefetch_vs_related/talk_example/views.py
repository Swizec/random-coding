# Create your views here.

from django.shortcuts import render_to_response

def home(request):
    return render_to_response('index.html',
                              {})

def prefetch(request):
    pass

def select(request):
    pass

def both(request):
    pass

