from enum import unique
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


from Register.managers import CustomUserManager


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
    
    valid_number=[RegexValidator(regex='09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}')]
    
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    role=models.CharField(max_length=1,choices=ROLE_CHOICES,default=ROLE_EMPLOYEE)
    phone=models.CharField(max_length=11,validators=valid_number,unique=True)
    company=models.ForeignKey(Company,on_delete=models.SET_NULL,null=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []
    object=CustomUserManager()
    
    def __str__(self) :
        return self.email
    class Meta :
        ordering=['last_name']
    
    
    


   
        
    
    
