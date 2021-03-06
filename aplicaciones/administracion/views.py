from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.files import ImageFieldFile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, logout
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate, login, logout
import requests
import json
import random
from django.core import serializers
from .models import *
from django.db.models import Q

# Create your views here.

## REDIRECCIONAR ##
def inicio(request):
	return render(request, 'Login/login.html')



# MENU PRINCIPAL SUPER ADMIN  ##
def principalSuperAdmin(request):
	return render(request,'Principal/SuperAdmin_Principal.html')





# MENU PRINCIPAL ADMIN  ##
def principalAdmin(request):
	return render(request,'Principal/Admin_Principal.html')


## EMPRESAS ##
def empresas(request):
	return render(request,'Empresa/index.html')

def getEmpresas(request):
	if request.method=='GET':
		res=[]
		
		empresas=Empresa.objects.all()
		for emp in empresas:
			dicc={"id":emp.id_empresa,"nombre":emp.nombre,"descripcion":emp.descripcion,"razon_social":emp.razon_social,"ruc_cedula":emp.ruc_cedula}
			res.append(dicc)
		return JsonResponse(res,safe=False)
	return HttpResponse(status=400)


## ROLES ##
def admin_rol(request):
	paquete = []
	return render(request, "roles/admin_rol.html", paquete)


## PRODUCTOS ##
def producto_page(request):
	if request.method=='GET':
		data_products=Producto.objects.all()
	return render(request, "Productos/productos.html",{"datos":data_products})

def agregar_producto(request):
	#data_products = Producto.objects.all()
	data_category = Categoria.objects.all()
	res=[]
	if request.method=='POST':
		name=request.POST.get('nombre',None)
		description = request.POST.get('descripcion',None)
		price = request.POST.get('precio',None)
		imagen = request.FILES.get('image',None)
		category = request.POST.get('id_categoria',None)
		data=Producto(nombre=name, descripcion=description, precio=price, image=imagen, id_categoria=category)
		data.save()
		#for p in data_products:
			#dicc={"id":p.id_producto, "nombre":p.nombre, "descripcion":p.descripcion, "precio":p.precio, "imagen":p.image, "categoria":p.id_categoria}
			#res.append(dicc)
		#return JsonResponse(res, safe=False)
		return render(request, "Productos/añadir_productos.html", {"data": data_category})
	if request.method=='GET':
		return render(request, "Productos/añadir_productos.html",{"data":data_category})
	return HttpResponse(status=400)


## CATEGORIAS ##
def get_categoria(request):
	if request.method=='GET':
		data_category=Categoria.objects.all()
	return render(request, "Productos/añadir_productos.html",{"datos":data_category})

