from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def saludar_a(request, nombre):
    return HttpResponse(f"hola como estas{nombre.capitalize()}")

def mostrar_mi_template(request):
    context = {
        "Nombre": "Rodrigo",
        "Apellido": "Tapia",
        "notas": [10, 6, 9, 5],
        "max_desaprobado": 5
        
    }
    return render(request, "AppCoder/index.html", context)
