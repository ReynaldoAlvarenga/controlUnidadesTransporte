from django.db import models
from django.utils import timezone

# Create your models here.

class Registro(models.Model):
	codigoReg=models.CharField(max_length=7,primary_key=True)
	fecha=models.DateField(auto_now_add=timezone.now().date())
	lugar=models.CharField(max_length=200)
	cantidadPasajeros=models.IntegerField(null=True, blank=True)
	cantidadDinero=models.FloatField(null=True, blank=True)
    puntocontrolregistro=models.ForeignKey(PuntoControl,null=False)

class UnidadTransporte(models.Model):
	nombreMotoriste=models.CharField(max_length=30,null=False)
	numeroPlaca=models.CharField(max_length=7,null=False)
	numeroAsientos=models.IntegerField(null=True, blank=True)
   # puntoruta=models.ForeignKey(PuntoRuta,null=False)

class PuntoRuta(models.Model):
	codigoPuntoRuta=models.CharField(max_length=7,primary_key=True)
	nombrePunto=models.CharField(max_length=30,null=False)
	cantidadUnidades=models.IntegerField(null=True, blank=True)

class PuntoControl(models.Model):
	codigoPuntoControl=models.CharField(max_length=7,primary_key=True)
	nom_responsable=models.CharField(max_length=30,null=False)
	lugar_asignado=models.CharField(max_length=200)

