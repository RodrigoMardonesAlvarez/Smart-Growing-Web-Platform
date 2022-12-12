from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    categoria=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['categoria']
        verbose_name='tag'
        verbose_name_plural='tags'
    
    def __str__(self):
        return self.categoria

class Entrada(models.Model):
    titulo=models.CharField(max_length=100)
    id = models.BigAutoField(primary_key=True)
    epigrafe=models.CharField(max_length=100, null=True, blank=True)
    contenido=models.CharField(max_length=800)
    imagen=models.ImageField(upload_to='Blog', null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag)
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        verbose_name='entrada'
        verbose_name_plural='entradas'
    
    def __str__(self):
        return self.titulo

#Formulario
#Paginacion
