from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html', )

def description(request):
    return render(request, 'generator/description.html')

#Generation password
def password(request):

    characters = list('abcdefghjklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special char'):
        characters.extend(list('!@#$%^&*()|":;/?'))

    length = int(request.GET.get('length'))

    #variable thepassword save generated password 
    # and  the for loop  generates  the password
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html',{'password': thepassword})

