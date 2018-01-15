# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,Http404,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

import random,urllib

from django.conf import settings

# Create your views here.
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from . import models
from django.contrib.auth.hashers import make_password, check_password
from django.core import serializers
import datetime
import json
import hashlib
import re
import time
import os
from django.conf import settings
from oauth_client import OAuthQQ

def qq_login(request):
    oauth_qq = OAuthQQ(settings.QQ_APP_ID, settings.QQ_KEY, settings.QQ_RECALL_URL)

    url = oauth_qq.get_auth_url()
    return HttpResponseRedirect(url)

def qq_check(request):
    request_code = request.GET.get('code')
    oauth_qq = OAuthQQ(settings.QQ_APP_ID, settings.QQ_KEY, settings.QQ_RECALL_URL)

    access_token = oauth_qq.get_access_token(request_code)
    time.sleep(0.05)
    open_id = oauth_qq.get_open_id()
    print open_id

    qq_open_id = models.OAuthQQ.objects.filter(qq_openid=str(open_id))
    print qq_open_id
    if qq_open_id:
        # user = qq_open_id[0].user.username
        user = qq_open_id[0].user
        setattr(user, 'backend', 'django.contrib.auth.backends.ModelBackend')
        login(request, user)
        # print user
        # print type(user)
        # request.session['username'] = user
        # print request.session['username']
        # return HttpResponseRedirect('/web/')
        # return HttpResponseRedirect('/index')
        # return redirect(to="index")

        # u = User.objects.get(username=user)
        # print u
        # print type(u)
        # p = User.objects.get(username=user).password
        # print p
        # print type(p)
        return redirect(to="index")
    else:
        infos = oauth_qq.get_qq_info()
        url = '%s?open_id=%s&nickname=%s' % (reverse('bind_account'), open_id, infos['nickname'])
        return HttpResponseRedirect(url)

# def bind_account(request):
#     open_id = request.GET.get('open_id')
#     nickname = request.GET.get('nickname')
#     if request.method == 'POST' and request.POST:
#         data = request.POST
#         # user = models.UserProfile()
#         user = models.UserInfo()
#         username = data['username']
#         # password = data['password'].split(',')[0]
#         password = data['password']
#         user.username = username
#         # password = hash_sha256(password, username)
#         user.password = password
#         # user.nickname = data['nickname']
#         # user.departments_id = 1
#
#         user.save()
#         oauthqq = models.OAuthQQ()
#         oauthqq.qq_openid = open_id
#         oauthqq.user_id = models.UserInfo.objects.get(username=username).id
#         oauthqq.save()
#         # response = HttpResponseRedirect("/web/")
#         response = HttpResponseRedirect("/index")
#         request.session['username'] = username
#         return response
#     return render(request, 'qq-bind-account.html', locals())

def signin(request):
    context = {}
    if request.method == "GET":
        form = AuthenticationForm
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            print form.get_user()
            print type(form.get_user())
            return redirect(to="index")
    context['form'] = form
    return render(request, 'login.html', context)

def bind_account(request):
    open_id = request.GET.get('open_id')
    nickname = request.GET.get('nickname')
    context = {}
    if request.method == "GET":
        form = UserCreationForm
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            print request.POST
            username = request.POST["username"]
            password = request.POST["password1"]

            user = User.objects.get(username=username)
            try:
                UserProfile.objects.get(belong_to=user)
            except:
                u = models.UserProfile()
                u.belong_to = user
                u.save()

            oauthqq = models.OAuthQQ()
            oauthqq.qq_openid = open_id
            oauthqq.user_id = models.UserProfile.objects.get(belong_to=user).id
            oauthqq.user = User.objects.get(username=username)
            print oauthqq.user
            oauthqq.save()

            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect(to="index")
            # username = request.POST["username"]
            # password = request.POST["password1"]
            # form = AuthenticationForm(username=username,password=password)
            # if form.is_valid():
            #     login(request, form.get_user())
            #     return redirect(to="index")
    context['form'] = form
    return render(request, 'qq-bind-account.html', locals())

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
