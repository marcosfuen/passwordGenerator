from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html',)

def password(request):
    characters = list('abcdefghijklmnñopqrstuvwxyz')
    length = int(request.GET.get('length', 12))
    thepassword = ''
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*().-_+'))
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
    