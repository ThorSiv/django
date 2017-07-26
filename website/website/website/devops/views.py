# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Host
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
# Create your views here.
def index(request):
    context = {}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def get_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template(load_template)
    return HttpResponse(template.render(context, request))

@login_required
def nice(request):
    form = Host()
    return HttpResponse("<h3>you can access system</h3>")

from django.contrib.auth import authenticate,login,logout

def user_check(request):
    errors=''
    if request.method == 'POST':

        form = Host(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            username = form['username']
            password = form['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return HttpResponse("Right")
            else:
                return render_to_response('login.html')
 
    return HttpResponse("Something is wrong")
def devops_login(request):
    logout(request)
    
    return render_to_response('login.html')

