from django.contrib.auth.models import User
from django.db import models

from .categoria import Categoria


class ArtigoConhecimento(models.Model):
	
	titulo = models.CharField(max_length=200)
	conteudo = models.TextField()
	categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
	anexos = models.FileField(upload_to='anexos/', blank=True, null=True)
	criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	criado_em = models.DateTimeField(auto_now_add=True)
	atualizado_em = models.DateTimeField(auto_now=True)
	publico = models.BooleanField(default=True)

	def __str__(self):
		return self.titulo
	
	class Meta:
		db_table = 'artigo_conhecimento'
		verbose_name = 'Artigo de Conhecimento'
		verbose_name_plural = 'Artigos de Conhecimento'
