from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import RequestContext
from .forms import BodegaForm, ProductoForm, TiendaForm
from .models import Tienda, Producto, Bodega
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

def info_index(request):
    return render(request, 'tienda/index.html')

#-------------------------- Vista de Tienda-----------------------------------

def tienda_list(request):
    tiendas = Tienda.objects.all()
    return render(request, 'tienda/tienda_list.html', {'tiendas':tiendas})

def tienda_detalle(request, pk):
    tiendas = get_object_or_404(Tienda, pk=pk)
    return render(request, 'tienda/tienda_detalle.html', {'tiendas': tiendas})

@login_required
def tienda_nueva(request):
    if request.method == "POST":
        formulario = TiendaForm(request.POST)
        if formulario.is_valid():
            tienda = Tienda(nombre = formulario.cleaned_data['nombre'], direccion = formulario.cleaned_data['direccion'], correo = formulario.cleaned_data['correo'],telefono = formulario.cleaned_data['telefono'])
            tienda.save()
        return redirect('tienda.views.tienda_list')
    else:
        formulario = TiendaForm()
    return render(request, 'tienda/tienda_nueva.html', {'formulario': formulario})

@login_required
def tienda_editar(request, pk):
    tienda = get_object_or_404(Tienda, pk=pk)
    if request.method == "POST":
        formulario = TiendaForm(request.POST, instance=tienda)
        if formulario.is_valid():
            tienda = formulario.save(commit=False)
            tienda.save()
        return redirect('tienda.views.tienda_list')
    else:
        formulario = TiendaForm(instance=tienda)
    return render(request, 'tienda/tienda_editar.html', {'formulario': formulario})

@login_required
def tienda_del(request, pk):
    tienda = get_object_or_404(Tienda, pk=pk)
    tienda.delete()
    return redirect('tienda.views.tienda_list')

#-------------------------- Vista de Producto -----------------------------------

def producto_lista(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/producto_lista.html', {'productos':productos})

def producto_detalle(request, pk):
    productos = get_object_or_404(Producto, pk=pk)
    return render(request, 'tienda/producto_detalle.html', {'productos': productos})

@login_required
def producto_nuevo(request):
    if request.method == "POST":
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            producto = formulario.save(commit=False)
            producto = Producto(nombre = formulario.cleaned_data['nombre'], descripcion = formulario.cleaned_data['descripcion'], precio = formulario.cleaned_data['precio'])
            producto.save()
        return redirect('tienda.views.producto_lista')
    else:
        formulario = ProductoForm()
    return render(request, 'tienda/producto_nuevo.html', {'formulario': formulario})

@login_required
def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        formulario = ProductoForm(request.POST, instance=producto)
        if formulario.is_valid():
            producto = formulario.save(commit=False)
            producto.save()
        return redirect('tienda.views.producto_lista')
    else:
        formulario = ProductoForm(instance=producto)
    return render(request, 'tienda/producto_editar.html', {'formulario': formulario})

@login_required
def producto_del(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('tienda.views.producto_lista')


##------------------Bodega--------------------------------------

def bodega_list(request):
    bodegas = Bodega.objects.all()
    return render(request, 'tienda/bodega_lista.html', {'bodegas':bodegas})

def bodega_detalle(request, pk):
    bodegas = get_object_or_404(Bodega, pk=pk)
    return render(request, 'tienda/bodega_detalle.html', {'bodegas': bodegas})

@login_required
def bodega_nueva(request):
    if request.method == "POST":
        formulario = BodegaForm(request.POST)
        if formulario.is_valid():
            bodega = formulario.save(commit=False)
            for tienda_id in request.POST.getlist('tienda'):
                for producto_id in request.POST.getlist('producto'):
                    bodega = Bodega(tienda_id=tienda_id, producto_id = producto_id,existencia = formulario.cleaned_data['existencia'])
                    bodega.save()
        return redirect('tienda.views.bodega_list')
    else:
        formulario = BodegaForm()
    return render(request, 'tienda/bodega_nueva.html', {'formulario': formulario})

@login_required
def bodega_editar(request, pk):
    bodega = get_object_or_404(Bodega, pk=pk)
    if request.method == "POST":
        formulario = BodegaForm(request.POST, instance=bodega)
        if formulario.is_valid():
            bodega = formulario.save(commit=False)
            for tienda_id in request.POST.getlist('tienda'):
                for producto_id in request.POST.getlist('producto'):
                    bodega.save()
        return redirect('tienda.views.bodega_list')
    else:
        formulario = BodegaForm(instance=bodega)
    return render(request, 'tienda/bodega_editar.html', {'formulario': formulario})

@login_required
def bodega_del(request, pk):
    bodega = get_object_or_404(Bodega, pk=pk)
    bodega.delete()
    return redirect('tienda.views.bodega_list')
