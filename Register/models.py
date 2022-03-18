from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from .manager import UserCreateManager





class Company(models.Model):

    company_name=models.CharField(max_length=255,primary_key=True)
    company_biography=models.TextField()
    
    
    def __str__(self) :
        return self.company_name



class User(AbstractUser):
    ROLE_COMPANY_OWNER='C'
    ROLE_EMPLOYEE='E'
    ROLE_CHOICES=[
        (ROLE_COMPANY_OWNER,'Company Owner'),
        (ROLE_EMPLOYEE,'Employee'),
    ]
    
    #regex for phone iranian phone number 
    valid_number=[RegexValidator(regex='09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}')]
    
    first_name=models.CharField(_('first name'),max_length=60)
    last_name=models.CharField(_('last name'),max_length=60)
    email=models.EmailField(_('email address'), unique=True)
    role=models.CharField(max_length=1,choices=ROLE_CHOICES)
    phone=models.CharField(_('phone number'),max_length=11,validators=valid_number,unique=True)
    company=models.ForeignKey(Company,on_delete=models.PROTECT)
    username=models.CharField(max_length=255,default=phone)
    USERNAME_FIELD='phone'
    REQUIRED_FIELDS = ['email']
    
    
    object=UserCreateManager()
    
    

    
    
    def __str__(self) :
        return self.email+" "+self.first_name+" "+self.last_name
    class Meta :
        ordering=['last_name']
    