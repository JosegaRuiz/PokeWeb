from django.db import models

# Create your models here.
class Type(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50)


class Afeccion(models.Model):
    id_source = models.CharField(max_length=50)
    id_dest = models.CharField(max_length=50)
    dmg = models.CharField(max_length=50)
