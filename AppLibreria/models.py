from django.db import models

# Create your models here.

class clientes(models.Model): 

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    def __str__(self):

        return f"{self.nombre}, {self.apellido}"


class subgeneros(models.Model):

    subgenero = models.CharField(max_length=15)
    editorial = models.CharField(max_length=30)
    def __str__(self):

        return f"{self.subgenero}"

class autor(models.Model):
    
    nombre = models.CharField(max_length=30)
    def __str__(self):

        return f"{self.nombre}"

    