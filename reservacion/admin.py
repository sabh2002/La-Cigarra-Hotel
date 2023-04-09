from django.contrib import admin
from .models import *
# Register your models here.


class ReservaAdmin(admin.ModelAdmin):
    readonly_fields = ("fechaReserva",)

admin.site.register(cliente)
admin.site.register(reserva, ReservaAdmin)
admin.site.register(habitacion)
admin.site.register(detalleReserva)