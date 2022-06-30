from operator import truediv
from django.db import models
from Register.models import User
# Create your models here.


class Dormitory(models.Model):
    number = models.IntegerField(null = True,blank=True)
    builing_name = models.CharField(max_length=200,null = True,blank=True)
    capacity = models.IntegerField(null = True,blank = True)
    remaining_capacity = models.IntegerField(null=True,blank=True)
    user = models.ForeignKey(User,null = True,blank = True,on_delete=models.CASCADE)
    #company = models.CharField(max_length=200,null=True,blank=True)
    
