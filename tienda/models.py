from django.db import models
from django.contrib import admin


class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(blank=True, max_length=200)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.nombre

class Tienda(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=80,blank=True)
    correo = models.EmailField(max_length=70,blank=True)
    telefono = models.CharField(max_length=15,blank=True)
    def __str__(self):
        return self.nombre

class Bodega (models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    existencia = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.tienda.nombre

class BodegaInLine(admin.TabularInline):
    model = Bodega
    extra = 1

class ProductoAdmin(admin.ModelAdmin):
    inlines = (BodegaInLine,)

class TiendaAdmin (admin.ModelAdmin):
    inlines = (BodegaInLine,)
