from django.db import models
from apps.producto import Compra


class Venta(models.Model):
	compra = models.ForeignKey(Compra, on_delete=models.CASCADE)

class Cliente(models.Model):
	nombre = models.CharField(max_lenght=70)
	telefono = models.IntegerField(blank=False, 
		help_text="Número de teléfono del cliente", 
		verbose_name="Número de teléfonp")
	direccion = models.CharField(max_lenght=300)
	correo = models.CharField(max_lenght=70)
	dni = models.IntegerField(unique=True)