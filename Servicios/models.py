from django.db import models

# Create your models here.

class Servicio(models.Model):
    sustantivo=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)
    imagen=models.ImageField(upload_to='Servicios')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    
    def __str__(self):
        return self.sustantivo

