from os import link
from django.contrib.auth.models import User
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    subTitle = models.CharField(max_length=20)
    autorName = models.CharField(max_length=10)
    autorSurname = models.CharField(max_length=15)
    fecha = models.CharField(max_length=10)
    cuerpo = models.TextField(blank = True, null=True)
    image = models.ImageField(upload_to='blog', null=True, blank=True)

    def str(self):
        return f'{self.title} -- Fecha de entrega: {self.fecha}'

class Profile(models.Model):
    nombre = models.CharField(max_length=15)
    descripcion = models.TextField(blank = True, null=True)
    email = models.EmailField()
    image = models.ImageField(upload_to='profile', null=True, blank=True)
    link = models.TextField(blank = True, null=True)
    
    def __str__(self):
        return f'url: {self.image.url}'

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)

    def __str__(self):
        return f'url: {self.image.url}'
