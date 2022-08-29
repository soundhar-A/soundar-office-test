from wsgiref import validate
from django.db import models
from django.forms import EmailField

# Create your models here.
class Office(models.Model):
    id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    company_code = models.CharField(max_length=50)
    strength = models.IntegerField(max_length=1000)
    web_site = models.CharField(max_length=250)
    created_time = models.DateTimeField(auto_now_add=True)

