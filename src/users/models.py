from django.db import models

# Create your models here.
class Usuario(models.Model):
    name        = models.TextField()
    last_name   = models.TextField()
    email       = models.TextField()
    password    = models.TextField()
    cpf         = models.TextField()
    