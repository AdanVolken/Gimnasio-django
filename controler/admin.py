from django.contrib import admin

from .models import Dia,Pago,Cliente,Hora

# Register your models here.
admin.site.register(Dia)
admin.site.register(Pago)
admin.site.register(Cliente)
admin.site.register(Hora)
