from django.contrib import admin
from puntocontrolapp.models import Registro,UnidadTransporte,PuntoRuta,PuntoControl

# Register your models here.
admin.site.register(Registro)
admin.site.register(UnidadTransporte)
admin.site.register(PuntoRuta)
admin.site.register(PuntoControl)
