from django.shortcuts import render,redirect,Http404,HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from webapp.form import LoginForm
import random

# Create your views here.

def signin(request):
    context = {}
    if request.method == "GET":
        form = AuthenticationForm
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(to="index")
    context['form'] = form
    return render(request, 'login.html', context)

def register(request):
    context = {}
    if request.method == "GET":
        form = UserCreationForm
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="signin")
    context['form'] = form
    return render(request, 'login.html', context)

def index(request):
    context = {}
    context['visitor'] = random.randint(0,1000)
    return render(request, 'index.html', context)

def list(request):
    context = {}
    return render(request, 'list.html', context)

def content(request):
    context = {}
    return render(request, 'content.html', context)
