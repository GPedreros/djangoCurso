from django.shortcuts import render, redirect
from .models import Mascotas

# Create your views here.
def home(request):
    mascota_listado = Mascotas.objects.all()
    return render(request, 'socio/mascota.html', {"mascotas": mascota_listado})

def agregar(request):
    return render, 'socio/agregar.html'

def eliminar(request, codigo):
    mascotas = Mascotas.objects.get(codigo =codigo)
    mascotas.delete()
    return redirect('/')

def edicion (request, codigo):
    mascotas = Mascotas.objects.get(codigo=codigo)
    return render(request, "agregar.html",{"mascota": mascotas} )

def editar(request):
    codigo=request.POST['idcodigo']
    nombre = request.POST['nombretxt']
    fotografia = request.POST['imagentxt']
    raza = request.POST['tipotxt']
    descripcion = request.POST['descripciontxt']
    estado = request.POST['estadotxt']
    Mascotas.save()
    return redirect('/')

def registrarMascota(request):
    codigo = request.POST['idcodigo']
    fotografia = request.POST['imagentxt']
    nombre = request.POST['nombretxt']
    raza = request.POST['tipotxt']
    descripcion = request.POST['descripciontxt']
    estado = request.POST['estadotxt']

    mascotas = Mascotas.objects.create(
        codigo = codigo, nombre = nombre, fotografia = fotografia, raza = raza, descripcion = descripcion, estado = estado
    )