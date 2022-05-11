from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class TaskModel(models.Model):
    nameTask = models.CharField(max_length=50)
    userCreate = models.CharField(max_length=255)

    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    deadline = models.DateTimeField()
    alert5min = models.BooleanField(default=False)
    alert = models.BooleanField(default=False)

