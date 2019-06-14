from django.db import models

from django.utils import timezone

# Create your models here.

class Registro(models.Model):
	codigoReg=models.CharField(max_length=7,primary_key=True)
	fecha=models.DateField(auto_now_add=timezone.now().date())
	lugar=models.CharField(max_length=100)
	cantidadPasajeros=models.IntegerField()
	cantidadDinero=models.FloatField(null=True, blank=True)
	#puntoControl=models.ForeignKey(PuntoControl,on_delete=models.CASCADE)
	#unidadtransporte=models.ForeignKey(UnidadTransporte,on_delete=models.CASCADE)

class UnidadTransporte(models.Model):
	nombreMotoriste=models.CharField(max_length=30,null=False)
	numeroPlaca=models.CharField(max_length=8,null=False)
	numeroAsientos=models.IntegerField(null=True, blank=True)
	#punto = models.ForeignKey(PuntoRuta, null=True,blank=True)

class PuntoRuta(models.Model):
	codigoPuntoRuta=models.CharField(max_length=7,primary_key=True)
	nombrePunto=models.CharField(max_length=30,null=False)
	cantidadUnidades=models.IntegerField(null=True, blank=True)

class PuntoControl(models.Model):
	codigoPuntoControl=models.CharField(max_length=7,primary_key=True)
	nom_responsable=models.CharField(max_length=30,null=False)
	lugar_asignado=models.CharField(max_length=100)
	puntocontrolregistro=models.ManyToManyField(UnidadTransporte,null=True,blank=True)

