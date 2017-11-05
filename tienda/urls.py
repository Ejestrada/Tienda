from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.info_index),
    url(r'^tiendas', views.tienda_list),
    url(r'^tienda/(?P<pk>[0-9]+)/$', views.tienda_detalle, name='tienda_detalle'),
    url(r'^tienda/nueva/$', views.tienda_nueva, name='tienda_nueva'),
    url(r'^tienda/(?P<pk>[0-9]+)/editar/$', views.tienda_editar, name='tienda_editar'),
    url(r'^tienda/(?P<pk>\d+)/del/$', views.tienda_del, name='tienda_del'),
    url(r'^productos/', views.producto_lista, name='producto_lista'),
    url(r'^producto/(?P<pk>[0-9]+)/$', views.producto_detalle, name='producto_detalle'),
    url(r'^producto/nuevo/$', views.producto_nuevo, name='producto_nuevo'),
    url(r'^producto/(?P<pk>[0-9]+)/editar/$', views.producto_editar, name='producto_editar'),
    url(r'^producto/(?P<pk>\d+)/del/$', views.producto_del, name='producto_del'),
    url(r'^bodegas', views.bodega_list, name='bodega_list'),
    #url(r'^$', views.tienda_list),
    url(r'^bodega/(?P<pk>[0-9]+)/$', views.bodega_detalle, name='bodega_detalle'),
    url(r'^bodega/nueva/$', views.bodega_nueva, name='bodega_nueva'),
    url(r'^bodega/(?P<pk>[0-9]+)/editar/$', views.bodega_editar, name='bodega_editar'),
    url(r'^bodega/(?P<pk>\d+)/del/$', views.bodega_del, name='bodega_del'),

    #url(r'^doctores/', views.doctor_lista, name='doctor_lista'),

]
