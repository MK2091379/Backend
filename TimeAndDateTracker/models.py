from xml.parsers.expat import model
from django.db import models

class TimeAndDateTracker(models.Model):
    start_point = models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank = True)
    end_point = models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank = True)
    difference =  models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank = True)
    delay = models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank = True)
    

