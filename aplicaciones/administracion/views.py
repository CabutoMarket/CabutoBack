from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.files import ImageFieldFile
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate, login, logout
import requests
import json
import random
from django.core import serializers
from itertools import chain
from .models import *

# Create your views here.

def inicio(request):
    if request.method == "POST":
        correo = request.POST.get("correo",None)
        contrasena = request.POST.get("contrasena",None)
        paquete = {}
        if correo and contrasena:
            usuario = authenticate(username=correo, password=contrasena)
            if usuario is not None:
                try:
                    admin=Usuario.objects.get(usuario=usuario)
                        #detalles = Detalles_Personales.objects.get(usuario=usuario)
                        #crearSesion(request,detalles) ##CREANDO SESION DEL USUARIO
                    return redirect("productos")
                except:
                    print("Correo o contraseña incorrecta")
            else:
                print("Correo o contraseña incorrecta")
        else:
            print("Correo o contraseña invalida")
        return render(request, "Login/login.html", paquete)
    return render(request, "Login/login.html")

def principalSuperAdmin(request):
	return render(request,'Principal/SuperAdmin_Principal.html')

def principalAdmin(request):
	return render(request,'Principal/Admin_Principal.html')

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


def admin_rol(request):
	paquete = []
	return render(request, "roles/admin_rol.html", paquete)

def producto_page(request):
	if request.method=='GET':
		data_productsxestab=Establecimiento_Producto.objects.select_related("id_producto")
		#data_estabxprod=Establecimiento_Producto.objects.all()
		#data_establecimiento=Establecimiento.objects.all()
		#for p in data_products:
		#	for e in data_establecimiento:
		#		for exp in data_estabxprod:
		#			if p.id_producto == exp.id_producto and e.id_establecimiento == exp.id_establecimiento:
		#				dicc={"nombre":p.name, "descripcion": p.descripcion, "precio": p.precio, "image": p.image, "stock": exp.stock_disponible}
		#				res.append(dicc)
		print(str(data_productsxestab.query))
		return render(request, "Productos/productos.html",{"datos":data_productsxestab})
	return HttpResponse(status=400)



def agregar_producto(request):
	#data_products = Producto.objects.all()
	data_category = Categoria.objects.all()
	data_establecimeinto=Establecimiento.objects.get(pk=1)
	res=[]
	if request.method=='POST':
		name=request.POST.get('nombre',None)
		description = request.POST.get('descripcion',None)
		price = request.POST.get('precio',None)
		imagen = request.FILES.get('image',None)
		category = request.POST.get('id_categoria',None)
		cantidad=request.POST.get('stock_disponible',None)
		data=Producto(nombre=name, descripcion=description, precio=price, image=imagen, id_categoria=category)
		data_estabxprod=Establecimiento_Producto(id_producto=data, stock_disponible=cantidad, id_establecimiento=data_establecimeinto, stock_despacho=100)
		data.save()
		data_estabxprod.save()
		#for p in data_products:
			#dicc={"id":p.id_producto, "nombre":p.nombre, "descripcion":p.descripcion, "precio":p.precio, "imagen":p.image, "categoria":p.id_categoria}
			#res.append(dicc)
		#return JsonResponse(res, safe=False)
		return render(request, "Productos/añadir_productos.html", {"data": data_category})
	if request.method=='GET':
		return render(request, "Productos/añadir_productos.html",{"data":data_category})
	return HttpResponse(status=400)

def editar_producto(request,id_producto):
	data_productsxestab = Establecimiento_Producto.objects.select_related(id_producto)
	data_producto = Producto.objects.get(id_producto=id_producto)
	return render(request, "Productos/editar_productos.html",{"data":data_producto})

def eliminar_producto(request,id_producto):
	data_producto=Producto.objects.get(id_producto=id_producto)
	data_producto.delete()
	data_productsxestab = Establecimiento_Producto.objects.select_related(id_producto)
	data_productsxestab.delete()
	return redirect("/productos")

def agregar_politica(request):
	#data_empresa=Empresa.objects.get(pk=1)
	if request.method == 'POST':
		name = request.POST.get('nombre', None)
		description = request.POST.get('descripcion', None)
		#data_politica = Politica(nombre=name, descripcion=description, id_empresa=data_empresa)
		data_politica = Politica(nombre=name, descripcion=description)
		data_politica.save()
		return render(request,"Politica/politica.html")
	if request.method=="GET":
		return render(request, "Politica/politica.html")


