from email.mime import image
from email.policy import default
from operator import truediv
from tkinter import CASCADE
from django.db import models
from Register.models import User,Company
from automation import settings
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class Employee(models.Model):
    sexuality_choises = [
        ("M","Male",),
        ("F","Female",),
        ("O","Other",)
    ]
    maritalـstatus_choises = [
        ("M","Maried",),
        ("S","Single",)
    ]
    degreeـofـeducationـchoises = [
        ("D","Diploma",),
        ("B","Bachelor",),
        ("M","Master",),
        ("O","Other")
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) 
    birthdate = models.DateField(null=True,blank=True)
    image = models.ImageField(_("image"), upload_to=None, height_field=20, width_field=20, max_length=None,default = "",null = True)
    personal_id = models.CharField(max_length=10,validators=[RegexValidator(regex='^[0-9]{10}')],null=True,blank=True)
    father_full_name = models.CharField(max_length=50,null=True,blank=True)
    mother_full_name = models.CharField(max_length=50,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    postal_code = models.CharField(max_length=10,validators=[RegexValidator(regex='^[0-9]{10}')])
    sexuality = models.CharField(max_length=1,choices=sexuality_choises,default="M")
    telephone = models.CharField(max_length=11,validators=[RegexValidator(regex='^0[0-9]{2,}[0-9]{7,}$')])
    maritalـstatus = models.CharField(max_length=1,choices=maritalـstatus_choises,default="S")
    degreeـofـeducation = models.CharField(max_length=1,choices=degreeـofـeducationـchoises,default="O")
    
class CompanyOwner(Employee,models.Model):
    pass