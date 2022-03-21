from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
    list_names = models.TextField(default='')
    requests = models.JSONField(default=dict)
