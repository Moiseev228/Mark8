from django.db import models

# Create your models here.

class Recepts(models.Model):
    name_prepations = models.CharField(max_length = 50, default = " ")
    name_patient = models.CharField(max_length = 50, default = " ")
    lastname_patient = models.CharField(max_length = 50, default = " ")
    patronymic_patient = models.CharField(max_length = 50, default = " ")
    id_staff = models.IntegerField()
    date_issue = models.CharField(max_length = 8)
  

    # # # id_prepations = models.IntegerField()
    # # # id_patiens = models.IntegerField()
    # # # id_staff = models.IntegerField()
    # # # date_issue = models.CharField(max_length = 8)