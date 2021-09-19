from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class categoria(models.Model):
    """Model definition for categoria."""

    nombre = models.CharField(null=False, blank=False, max_length=50)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

class producto(models.Model):

    nombre = models.CharField(null=False, blank=False, max_length=50)
    marca = models.CharField(null=False, blank=False, max_length=50)
    costo = models.FloatField()
    precio_venta = models.FloatField()
    id_categiria = models.ForeignKey(categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.nombre

class proveedor(models.Model):

    nombre = models.CharField(null=False, blank=False, max_length=50)
    telefono = models.IntegerField()
    ruc = models.IntegerField()
    direccion = models.CharField(null=False, blank=False, max_length=50)
    id_producto = models.ForeignKey(producto,on_delete=CASCADE)

    class Meta:
        
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'

    def __str__(self):
        return self.nombre

class compra(models.Model):

    cantidad = models.IntegerField()
    id_producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(proveedor, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = 'compra'
        verbose_name_plural = 'compras'

    def __str__(self):
        return self.fecha
