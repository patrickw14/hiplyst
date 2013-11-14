from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django import forms
from datetime import datetime
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

def login(request):
    username = password = ''
    error = False
    state = ''
    if request.POST:
        username = request.POST.get('username')
	password = request.POST.get('password')

        #we will use django's built in user auth system
        user = authenticate(username = username, password = password)
	if user is not None:
          if user.is_active:
            auth_login(request, user)
            #return HttpResponseRedirect('/')
            state = "You're successfully logged in!"
          else:
            state = "Your account is not active, please contact the site admin."
        else:
            #error = True
            state = "Your username and/or password are incorrect."
    return render_to_response('login.html', {'error': error, 'username':username, 'state': state}, 
                                          context_instance=RequestContext(request))

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')

# TODO - Error handling mechanisms
def signup(request):
    username = password = email = fname = lname = ""
    error = False
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()

        #Now, log in user and redirect to home
        user = authenticate(username = username, password = password)
        auth_login(request, user)
        return HttpResponseRedirect('/')
