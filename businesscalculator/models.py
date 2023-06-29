from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(max_length=4)
    founder = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    form = models.CharField(max_length=3)
    industry = models.CharField(max_length=50)
    activity = models.CharField(max_length=50)
    registration_date = models.DateTimeField(auto_now_add=True)
