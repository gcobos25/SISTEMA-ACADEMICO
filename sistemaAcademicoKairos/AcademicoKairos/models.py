from django.db import models

# Create your models here.
class ConfiguracionUsuario(models.Model):
    usuario = models.CharField(max_length=45,unique=True)
    clave = models.CharField(max_length=45)

    class Meta:
        verbose_name = 'Usuario',
        verbose_name_plural = 'Usuarios',
        
    def __str__(self):
        return self.usuario