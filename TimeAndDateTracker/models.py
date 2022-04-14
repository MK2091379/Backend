from datetime import date
from tkinter import CASCADE
from xml.parsers.expat import model
from django.db import models
from Register.models import User

class TimeAndDateTracker(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank = True)
    date = models.DateField(auto_now=False, auto_now_add=False,null=True,blank = True)
    start_point = models.TimeField(auto_now=False, auto_now_add=False,null=True,blank = True)
    end_point = models.TimeField(auto_now=False, auto_now_add=False,null=True,blank = True)
    #duration=  models.FloatField(null=True,blank = True)
    wasted_time = models.PositiveIntegerField(null=True,blank = True)


