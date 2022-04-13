from datetime import date
from tkinter import CASCADE
from xml.parsers.expat import model
from django.db import models
from Register.models import User

class TimeAndDateTracker(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank = True)
    start_point = models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank = True)
    end_point = models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank = True)
    duration=  models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank = True)
    delay = models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank = True)
    

