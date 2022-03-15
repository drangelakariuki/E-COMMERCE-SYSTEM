from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models import *
from kui.models import *

# Create your views here.

def say_hello(request): # display products

    queryset = Product.objects.all()
    
    return render(request, 'hello.html', {'name': 'Dr Angela W. Kariuki', 'products': list(queryset)})

def check_base(request):
    
    return render(request, 'index.html')

