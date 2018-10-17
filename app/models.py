from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    link=models.URLField(max_length=100)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
