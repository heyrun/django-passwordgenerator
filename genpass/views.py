from django.shortcuts import render
import random

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'genpass/home.html', {'password': 'tsting a password'})

def password(request):
    xters = 'abcdefghijklmnopqrstuvwxyz'
    characters = list(xters)
    length = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        characters.extend(list(xters.upper()))
      

    if request.GET.get('special'):
        special = list('!@#$%^&*-_')
        characters.extend(special)
        
    if request.GET.get('numbers'):
        numbers = list('1234567890')
        characters.extend(numbers)

    thepassword = ''
    for x in range(length):
        thepassword+=random.choice(characters)
    return render(request, 'genpass/password.html', {'password':thepassword })

def about(request):
    return render(request, 'genpass/generic.html')