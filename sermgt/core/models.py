from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Service(models.Model):
    title = models.CharField(max_length=35)
    description = models.CharField(max_length=35)
    price =  models.CharField(max_length=10)
    def __str__(self):
        return self.title



class Appointement(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    address = models.CharField(max_length=100)