from django.shortcuts import render

# Create your views here.
def Inicial(request):
    return render(request, "inicio.xml")    

def Empleados(request):
    return render(request, "Empleados.xml")
    
def Discos(request):
    return render(request, "Discos.xml")
    
def Paises(request):
    return render(request, "Paises.xml")

def RepEmpleados(request):
    return render(request, "EmpleadosRep.xml")

def RepPaises(request):
    return render(request, "PaisesRep.xml")