from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User,related_name='profile',on_delete=models.DO_NOTHING,)
    avatar = models.FileField(upload_to='upload/avatar')
