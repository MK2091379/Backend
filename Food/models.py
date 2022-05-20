from datetime import date
from tkinter import CASCADE
from xml.parsers.expat import model
from django.db import models
from Register.models import User,Company

class Food(models.Model):
    user = models.ManyToManyField(User,blank = True)
    date = models.DateField(auto_now=False, auto_now_add=False,null=True,blank = True)
    name = models.TextField(null=True,blank = True)
    amount = models.IntegerField(null=True,blank = True)
    company = models.ManyToManyField(Company,blank=True)


