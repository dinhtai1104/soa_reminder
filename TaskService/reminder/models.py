from statistics import mode
from django.db import models

# Create your models here.

class Task (models.Model):
    nameTask = models.CharField(max_length=255)
    deadline = models.DateField()
    sentMail = models.BooleanField(default=False)
    
    