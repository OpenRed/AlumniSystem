# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User,related_name='profile')
    nickname = models.CharField(max_length=64,unique=True,null=True,blank=True)
    image = models.FileField(upload_to='profile_image',null=True,blank=True)
    SEX_CHOICES = (
        ('男', '男'),
        ('女', '女'),
    )
    sex = models.CharField(max_length=10, choices=SEX_CHOICES,null=True, blank=True)
    def __str__(self):
        return str(self.belong_to)

class UserInfo(models.Model):
    username = models.CharField(max_length=64,primary_key=True)
    password = models.CharField(max_length=64)

class OAuthQQ(models.Model):
    """User models ex"""
    user = models.ForeignKey(to=User,on_delete=models.DO_NOTHING)
    qq_openid = models.CharField(max_length = 64)

# class OAuth_ex(models.Model):
#     """User models ex"""
#     user = models.ForeignKey(to=User,on_delete=models.DO_NOTHING)
#     qq_openid = models.CharField(max_length = 64)
