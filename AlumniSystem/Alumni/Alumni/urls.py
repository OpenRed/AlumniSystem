"""Alumni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib import admin
# from django.urls import path
from django.conf.urls import url, include
from webapp.views import *
import webapp.urls
from django.contrib.auth.views import logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^index$', index, name="index"),
    url(r'^list$', list, name="list"),
    url(r'^content$', content, name="content"),
    url(r'^login$', signin, name="login"),
    url(r'^register$', register, name="register"),
    url(r'^logout$', logout, {'next_page':'/index'}, name="logout"),

    # url(r'^web/', include(webapp.urls)),
    url(r'^oauth/qq/login', qq_login, name='qq_login'),
    url(r'^oauth/qq/check', qq_check, name='qq_check'),
    url(r'^oauth/bind/account', bind_account, name='bind_account'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
