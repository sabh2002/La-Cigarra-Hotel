from django.db import models

# Create your models here.

class cliente(models.Model):
    cedula = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.EmailField()

    def __str__(self):
        return self.nombre + " " + self.apellido

class habitacion(models.Model):
    numeroHabitacion = models.IntegerField(primary_key=True)
    tipoHabitacion = models.CharField(max_length=25)
    precio = models.IntegerField()
    #reserva = models.ForeignKey(reserva, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField()

    def __str__(self):

        return f"Habitacion #{self.numeroHabitacion}"


class reserva(models.Model):
    codigo = models.AutoField(primary_key=True)
    fechaReserva = models.DateField(auto_now=True)
    fechaLlegada = models.DateField()
    fechaSalida = models.DateField()
    estado = models.CharField(max_length=25)
    habitacion = models.OneToOneField(habitacion, on_delete=models.CASCADE)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    origen = models.CharField(max_length=25)


    def __str__(self):
        codigo = self.codigo
        #codigo = str(codigo)
        return f"{self.cliente} codigo de reserva: {codigo}"

class detalleReserva(models.Model):
    codigo = models.IntegerField(primary_key=True)
    codigoReserva = models.ForeignKey(reserva, on_delete=models.CASCADE)
    codigoHabitacion = models.ForeignKey(habitacion, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.codigo}"