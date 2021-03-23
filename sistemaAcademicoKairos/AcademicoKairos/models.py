from django.db import models
from AcademicoKairos.Apps.validaciones import *

# Create your models here.
class ConfiguracionUsuario(models.Model):
    usuario = models.CharField(
    		max_length=45,
    		unique=True, 
    		validators=[
    			validate_nombre,
    			longitud, 
    			alfanumerico, 
    			espaciosusu,
    		]
    	)
    
    clave = models.CharField(
    		max_length=45,
    		validators=[
    			longitudPassword, 
    			minuscula, 
    			mayuscula, 
    			numero, 
    			espacios, 
    			alfanumericoPassword,
    		]
    	)

    class Meta:
        verbose_name = 'Usuario',
        verbose_name_plural = 'Usuarios',
        
    def __str__(self):
        return self.usuario