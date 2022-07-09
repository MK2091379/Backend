from operator import truediv
from django.db import models
from Register.models import User
# Create your models here.



class CompanyAssets(models.Model):
    name = models.CharField(null=True,blank=True,max_length=200)
    description = models.TextField(null=True,blank=True)
    number = models.IntegerField(blank=True,null=True)
    user = models.ForeignKey(User,null = True,blank = True,on_delete=models.CASCADE)