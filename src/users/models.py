from django.db import models

# Create your models here.
class Usuario(models.Model):
    user_id     = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=25, blank=False)
    last_name   = models.CharField(max_length=25, blank=False)
    email       = models.EmailField(max_length=150, blank=False)
    password    = models.CharField(max_length=35, blank=False)
    cpf         = models.CharField(max_length=11, blank=False)
    