from django.db import models

# Create your models here.

class Recepts(models.Model):
    id_prepations = models.IntegerField()
    id_patiens = models.IntegerField()
    id_staff = models.IntegerField()
    date_issue = models.CharField(max_length = 8)
  