from django.db import models

# Create your models here.

class Prepations(models.Model):
    name = models.CharField(max_length=124)
    type_prepations = models.CharField(max_length = 100)
    maker = models.CharField(max_length = 50, default = " ")
    form_release = models.CharField(max_length = 30, default = " ")

class List_prepations(models.Model):
    id_recept = models.IntegerField()
    id_pripations = models.IntegerField()

class Patiens(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, default = " ")
    patronymic = models.CharField(max_length=50, default = " ")
    address = models.CharField(max_length = 100)  
    polis = models.CharField(max_length = 16)
    phone = models.CharField(max_length = 15, default = " ")     
    date_of_birth = models.CharField(max_length = 10, default = " ")
    sector = models.CharField(max_length = 30, default = " ")
    Recording_date = models.CharField(max_length = 10, default = " ")
    
