from django.db import models

# Create your models here.
class Equipos(models.Model):

    nombre= models.CharField(max_length=40)
    ano= models.IntegerField()


class Camisetas(models.Model):
    nom_equipo=models.CharField(max_length=40)
    ano_camiseta= models.IntegerField()

class Copas(models.Model):
    copa= models.CharField(max_length=40)
    num_copa= models.IntegerField()