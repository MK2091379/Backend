from datetime import date
from operator import truediv
from tkinter import CASCADE
from urllib.request import CacheFTPHandler
from xml.parsers.expat import model
from django.db import models
from Register.models import User,Company

class Food(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False,null=True,blank = True)
    name = models.TextField(null=True,blank = True)
    amount = models.IntegerField(null=True,blank = True)
    company = models.CharField(max_length=200,null=True,blank=True)
    price = models.DecimalField(null=True,blank=True,max_digits=5,decimal_places=0)