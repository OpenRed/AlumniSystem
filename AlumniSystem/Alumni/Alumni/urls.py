"""Alumni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from webapp.views import *
from django.contrib.auth.views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('index', index, name="index"),
    path('list', list, name="list"),
    path('content', content, name="content"),
    path('login', signin, name="login"),
    path('register', register, name="register"),
    path('logout', logout, {'next_page':'/index'}, name="logout"),
]
