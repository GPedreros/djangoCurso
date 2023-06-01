from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Mascotas(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    fotografia = models.CharField(max_length=250)
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title