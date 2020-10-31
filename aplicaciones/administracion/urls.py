from django.urls import path
from .views import *
from django.conf.urls import url
from django.contrib.auth import authenticate, logout

urlpatterns = [	
	path('', inicio),
	path('principalSuperAdmin/',principalSuperAdmin),
	path('principalAdmin/',principalAdmin),
	path('principalSuperAdmin/empresas/', empresas),
	path('roles/',admin_rol),
	path('politica/', agregar_politica),
	path('productos/', producto_page, name="productos"),
	url(r'^productos/añadir_productos/', agregar_producto, name="añadir_productos"),
#	url(r'^productos/editar_producto/(?P<id_producto>\d+)', editar_producto, name="editar_producto"),
	url(r'^productos/eliminar_producto/(?P<id_producto>\d+)', eliminar_producto, name="eliminar_producto"),

]
