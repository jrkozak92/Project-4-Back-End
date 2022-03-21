from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    task = models.CharField(max_length=50)
    todo_choices_list = [
        ('todo','todo'),
        ('doing','doing'),
        ('done','done')
    ]
    todo_choices = models.CharField(
        max_length=5,
        choices= todo_choices_list,
        default= 'todo'
    )