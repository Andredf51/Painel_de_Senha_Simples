from django.db import models

# Create your models here.
# class Perfil(models.Model):

#     senha = models.IntegerField(null=False)
#     status = models.CharField(max_length=255, null=False)
#     tipo = models.CharField(max_length=255, null=False)
#     categoria = models.CharField(max_length=255, null=False)

#testes - pode comentar depois
class Status_senha(models.Model):
    id_status = models.IntegerField(null=False)
    nome_status = models.CharField(max_length=255, null=False)

class Categoria_senha(models.Model):
    id_categoria = models.IntegerField(null=False)
    nome_categoria = models.CharField(max_length=255, null=False)

class Tipo_senha(models.Model):
    id_tipo = models.IntegerField(null=False)
    nome_tipo = models.CharField(max_length=255, null=False)

class Senha(models.Model):
    senha = models.IntegerField(null=False)
    Status = models.ForeignKey(Status_senha, on_delete=models.CASCADE, related_name='buscar_status')
    Tipo = models.ForeignKey(Tipo_senha, on_delete=models.CASCADE, related_name='buscar_tipos')
    Categoria = models.ForeignKey(Categoria_senha, on_delete=models.CASCADE, related_name='buscar_categorias')
    