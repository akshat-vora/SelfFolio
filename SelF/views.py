from django.shortcuts import render, redirect, HttpResponse
from .models import Profile
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django import forms

# Create your views here.
# def signup(response):
#     if response.method == "POST":
#         form = RegisterForm(response.POST)
#         if form.is_valid():
#             form.save
#         return redirect("/")
#     else:
#         form = RegisterForm()
    
#     return render(response, "registration/signup.html", {"form":form})

def signup(request):
    if request.method == 'GET':
        return render(request, 'registration/signup.html')
        
    elif request.method == 'POST':
        #form = event_registration_form(request.POST)
        #if form.is_valid():
        #    form.save()
        #    return HttpResponse("Saved")
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        bio = request.POST['bio']
        univ = request.POST['univ']
        date = request.POST['date']
        prof = request.POST['prof']
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']
        user_info = Profile.objects.create(
            UserName = user_name,
            FirstName = first_name,
            LastName = last_name,
            Bio = bio,
            University = univ,
            DOB = date,
            Profession = prof,
            UserEmail = user_email,
            Password = user_password
        )
        user_info.save()
        
        return render(request, 'home.html')


def welcome(request):
    return redirect('login')
