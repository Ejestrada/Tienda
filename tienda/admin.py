from django.contrib import admin
from .models import Tienda, Producto,Bodega,BodegaInLine,ProductoAdmin,TiendaAdmin

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Tienda, TiendaAdmin)
admin.site.register(Bodega)
