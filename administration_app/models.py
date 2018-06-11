from django.db import models

# Create your models here.

class Staff(models.Model):
    login_employee = models.CharField(max_length = 150, default = " ")
    type_users = models.CharField(max_length = 30, default = " ")
    address = models.CharField(max_length = 100, default = " ")  
    phone = models.CharField(max_length = 16, default = " ") 
    post = models.CharField(max_length = 100, default = " " )
    specialization = models.CharField(max_length = 100, default = " ") 
    passport = models.CharField(max_length = 11, default = " ")
