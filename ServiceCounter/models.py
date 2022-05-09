from calendar import WEDNESDAY
import defusedxml
from django.db import models
from Register.models import User
from location_field.models.plain import PlainLocationField




class AdminTransportation(models.Model):
    address= models.TextField()
    maximum_capacity=models.PositiveIntegerField(null=True)
    details=models.TextField(null=True)
    address_search = models.CharField(max_length=255,null=True)
    location = PlainLocationField(based_fields=['address_search'], zoom=7,null=True)
    arrival_time=models.TimeField(null=True)
    Return_time=models.TimeField(null=True)
    admin=models.ForeignKey(User , on_delete=models.CASCADE,null=True)
    last_update=models.DateTimeField( auto_now=True)
    creation_time=models.DateTimeField( auto_now_add=True)
# Create your models here.
    ##days
    saturday=models.BooleanField(default=False)
    sunday=models.BooleanField(default=False)
    monday=models.BooleanField(default=False)
    tuesday=models.BooleanField(default=False)
    wednesday=models.BooleanField(default=False)
    thursday=models.BooleanField(default=False)
    friday=models.BooleanField(default=False)
    
    
    
class TransportationsRequest(models.Model):
    
    Services=[
    
        ("E","Etc"),
        ("T","Transportation"),
    ]
    
    
    request=models.TextField()
    type_of_service=models.CharField(max_length=2,choices=Services,default='E')
    creation_time=models.DateTimeField( auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    

