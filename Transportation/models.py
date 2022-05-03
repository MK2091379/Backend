from django.db import models
from Register.models import User
from location_field.models.plain import PlainLocationField




class AdminTransportation(models.Model):
    address= models.TextField()
    maximum_capacity=models.PositiveIntegerField()
    details=models.TextField()
    address_search = models.CharField(max_length=255,null=True)
    location = PlainLocationField(based_fields=['address_search'], zoom=7)
    arrival_time=models.TimeField()
    Return_time=models.TimeField()
    admin=models.ForeignKey(User , on_delete=models.CASCADE)
    last_update=models.DateTimeField( auto_now=True)
    creation_time=models.DateTimeField( auto_now_add=True)
# Create your models here.
