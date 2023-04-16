from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import *
from .models import *

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    # return HttpResponse('Hola mundo')
    
    variable = 'Me la voy a cojer, algun dia'

    if request.method == 'GET':

        return render(request, 'signup.html', {
            'form_usuario': UserCreationForm
        })
        # print("Enviando Datos")

    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                usuario = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                usuario.save()
                login(request, usuario)
                return redirect('registrar_clientes')

            except IntegrityError:
                return render(request, 'signup.html', {
                    'form_usuario': UserCreationForm, "error": 'Usuario ya existe'
                })

        return render(request, 'signup.html', {
            'form_usuario': UserCreationForm, "error": 'contraseñas no coinciden'
        })


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})

    else:
        usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        
        
        if usuario is None:
            return render(request, 'signin.html', {'form': AuthenticationForm, 
            "error":'Usuario o contraseña incorrectos'})
        
        else:
            login(request, usuario)
            return redirect('registrar_clientes')
        

def clientes(request):
    clientes = cliente.objects.all()

    return render(request, 'clientes.html', {'clientes': clientes})



def registrar_clientes(request):

    if request.method=='GET':

        return render(request, 'registrar_cliente.html', {'form':
                                                        crear_cliente })
    else:
        form = crear_cliente(request.POST)
        #if form.is_valid():
        nuevo_cliente = form.save(commit=False)
        nuevo_cliente.save()
        return redirect('clientes')
        #nuevo_usuario = form.save(commit=False)
        #print(nuevo_usuario )
        

def reservacion(request):

    if request.method == 'GET':
        return render(request, 'reservacion.html', {'form' : crear_reservacion})
    
    else:
        try:
            form = crear_reservacion(request.POST)
            nueva_reservacion = form.save(commit=False)
            nueva_reservacion.save()
            return redirect('home')
        except ValueError: return render(request, 'reservacion.html',{'error':'Datos invalidos'})
        


def cerrar_sesion(request):
    logout(request)
    return redirect('home')