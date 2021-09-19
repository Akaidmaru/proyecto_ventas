from django.contrib import admin
from apps.producto.models import categoria,proveedor,producto,compra

# Register your models here.
admin.site.register(categoria)
admin.site.register(proveedor)
admin.site.register(producto)
admin.site.register(compra)
