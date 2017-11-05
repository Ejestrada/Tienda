from django import forms
from .models import Tienda, Producto, Bodega



class BodegaForm(forms.ModelForm):
#todos los campos de Bodega
    class Meta:
        model = Bodega
        fields = ('tienda', 'producto','existencia')

#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.

def __init__ (self, *args, **kwargs):
        super(TiendaForm, self).__init__(*args, **kwargs)
#ModelChoiceField(queryset=Books.objects.all().order_by('name'))
#En este caso vamos a usar el widget checkbox multiseleccionable.
        self.fields["tienda"].widget = forms.widgets.CheckboxSelectMultiple()
#Podemos usar un texto de ayuda en el widget
        self.fields["tienda"].help_text = "Escoja el tienda a asignar producto"
        self.fields["tienda"].queryset = Tienda.objects.all()
#En este caso vamos a usar el widget checkbox multiseleccionable.
        self.fields["producto"].widget = forms.widgets.CheckboxSelectMultiple()
#Podemos usar un texto de ayuda en el widget
        self.fields["producto"].help_text = "Seleccione el producto asignado"
        self.fields["producto"].queryset = Producto.objects.all()

#-----------------Tienda--------------------

class TiendaForm(forms.ModelForm):

    class Meta:
        model = Tienda
        fields = ('nombre', 'direccion','correo','telefono',)

#-----------------Producto--------------------

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion','precio',)
