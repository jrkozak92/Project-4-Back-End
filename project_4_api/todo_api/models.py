from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    task = models.CharField(max_length=50)
    
