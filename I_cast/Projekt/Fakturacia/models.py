# Projekt/Fakturacia/models.py/ -- verzia 0.1 Cast_1-kapitola


from django.db import models

# Create your models here.

class Faktura(models.Model):
    var_symbol = models.CharField(max_length=255, unique=True)
    datum_vystavenia = models.DateField()    #(auto_now_add=True)
    datum_dodania = models.DateField()
    doba_splatnosti = models.DateField()