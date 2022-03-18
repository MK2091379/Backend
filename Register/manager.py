import email
from django.contrib.auth.base_user import BaseUserManager



class UserCreateManager(BaseUserManager):
     use_in_migration=True
     
     
     
     def create_user(self,phone,email,password,**extra_fields):
         
         if not phone:
             raise ValueError("Please Enter your phone")
         if not email:
             raise ValueError("Please Enter your email")
         email=self.normalize_email(email)
         user=self.model(phone=phone,email=email,**extra_fields)
         user.set_password(password)
         user.save(using=self._db)
         return user
     
     
     def create_superuser(self,phone,email,password,**extra_fields):
         
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("super user staff must be True")
        
        return self.create_user(phone,email,password,**extra_fields)
        
