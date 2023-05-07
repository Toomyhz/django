from django.shortcuts import render
from .productos import productos

def mostrar_inicio(request):
    return render(request,'index.html')

def mostrar_productos(request):
    context = {
        'productos': productos}
    return render(request,'assets\html\productos.html',context)

def mostrar_contacto(request):
    return render(request,'assets\html\contacto.html')

def mostrar_inicio_sesion(request):
    return render(request,'assets\html\iniciar-sesion.html')
