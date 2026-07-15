from django.db import models

# Create your models here.
class Prato(models.Model):
    nome_prato = models.CharField(max_length=100)
    categoria_prato = models.CharField(max_length=50)
    imagem_prato = models.ImageField(upload_to="imagens_pratos/")