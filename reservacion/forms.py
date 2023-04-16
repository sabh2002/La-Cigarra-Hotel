from django.forms import ModelForm
from django import forms
from .models import *

class crear_cliente(ModelForm):
    class Meta:
        model = cliente
        fields = ['cedula', 'nombre', 'apellido', 'direccion', 'telefono', 'correo']

class crear_reservacion(ModelForm):

    class Meta:
        model = reserva
        fields = ['fechaLlegada', 'fechaSalida', 'habitacion', 'cliente']

        widgets = {
            'fechaLlegada': forms.DateInput(attrs={'type': 'date'}),
            'fechaSalida': forms.DateInput(attrs={'type': 'date'})
        }
