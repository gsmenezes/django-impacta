from django.db import models

class Curso(models.Model):
    nome = models.CharField("Nome", max_length=50)
    sigla = models.CharField("Sigla",max_length=5)
    etiqueta = models.SlugField("Etiqueta", max_length=50)

def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField("Nome", max_length=50)
    etiqueta = models.SlugField("Etiqueta", max_length=50)
    carga_horaria = models.IntegerField("Carga Horaria")

def __str__(self):
    return self.nome
    
     

# Create your models here.
