from django.db import models
#from django.contrib.auth.models import User
# Create your models here.

class Snippet(models.Model):
    title = models.TextField()
    code = models.TextField()
'''
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
'''