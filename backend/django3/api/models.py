from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Coche(models.Model):
    modelo = models.CharField(max_length=60)
    marca = models.CharField(max_length=60)
    propietario = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=False, default=1, related_name='cars')
    def __str__(self):
        return self.modelo+" - "+self.marca