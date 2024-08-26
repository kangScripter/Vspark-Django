from django.db import models
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import AbstractUser,BaseUserManager,AbstractBaseUser

User = get_user_model()
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=16)
    course = models.CharField(max_length=10)

# class UserManager(BaseUserManager):
#     def create_user(self,username,email,mobile_number,course,password):
#         # if not username or not email or not mobile_number or not course or not password:
#         #     raise ValueError("ALL Fields is Required")
#         user = self.model(username=username,email=email,course=course,mobile_number=mobile_number)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     def create_superuser(self,username,email,password):
#         user = self.create_user()
#         user.course = None
#         user.mobile_number = None
#         user.is_active = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
     
# class User(AbstractUser):
#     username = models.CharField(max_length=100,unique=True)
#     email = models.EmailField()
#     password = models.CharField(max_length=16,unique=True)
#     course = models.CharField(max_length=10,blank=True, null=True)
#     mobile_number = models.CharField(max_length=10,blank=True, null=True)
#     USERNAME_FIELD= "username"
#     objects = UserManager()
