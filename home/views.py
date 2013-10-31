from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django import forms
from datetime import datetime
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def home(request):
    context = {}
    return render(request, 'index.html', context)
