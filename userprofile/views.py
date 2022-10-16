from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import userPref
from .functions import *
import json
from django.http import HttpResponse
# Create your views here.
def index(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Already Used')
            return redirect('index')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username Already Used')
            return redirect('index')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')

    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('intro')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def survey(request):

    if request.method == "POST":
        meal = request.POST['meal']
        restriction = request.POST['restriction']
        cuisine = request.POST['cuisine']
        favorite = request.POST['favorite']
        ingredient = request.POST['ingredient']

        preferences = [meal, restriction, cuisine, favorite, ingredient]

        #newPref = userPref(username=request.user, pref=preferences )
        #newPref.save()
        recList = []
        big_list = giant_list(preferences)
        for i in big_list:
            for item in i:
                label = item.label
                calories = item.calories
                image = item.image

                recList.append({"label": item.label, "calories": item.calories, "image": item.image})


        mylist = json.dumps(recList)



        return render(request, 'match.html', {'recList': mylist})

    return render(request, 'survey.html')

def match(request):
    return render(request, 'match.html')


def intro(request):
    username = request.user.username
    return render(request, 'intro.html', {'username': username})


