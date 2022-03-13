
import email
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from django.db import models

# from django.contrib.auth.models import User

# Create your models here.

# class Role(models.Model):# type person in company 
#     role_companyowner='CO'
#     role_employee='E'
#     role_choice=[
#         (role_companyowner,'Company owner'),
#         (role_employee,'Employee'),
#     ]
#     role=models.CharField(max_length=3,choices=role_choice,default=role_employee)

# class Company(models.Model):  #company table (name)
#     companyname=models.CharField(max_length=200) 

# class CompanyOwner(models.Model):
#      companyowner=models.ForeignKey(User,on_delete=models.CASCADE)
#      role=models.ForeignKey(Role,on_delete=models.PROTECT)
#      company=models.OneToOneField(Company,on_delete=models.CASCADE) 

# class Employee(models.Model):
#      employee=models.ForeignKey(User,on_delete=models.CASCADE)
#      companybigrophy=models.TextField()
#      role=models.ForeignKey(Role,on_delete=models.PROTECT)
#      companyowner=models.ForeignKey(CompanyOwner,on_delete=models.SET_NULL,null=True)
#      company=models.OneToOneField(Company,on_delete=models.CASCADE)
#      def __str__(self) -> str:
#          return self.em

   
        
    
    
