from django.contrib.auth.models import User
from django.db import models


class Ticket(models.Model):
	
	STATUS_CHOICES = [
		("aberto", "Aberto"),
		("em_andamento", "Em andamento"),
		("resolvido", "Resolvido"),
		("fechado", "Fechado"),
	]
	
	PRIORIDADE_CHOICES = [
		("baixa", "Baixa"),
		("media", "Média"),
		("alta", "Alta"),
	]
	
	titulo = models.CharField(max_length=200)
	descricao = models.TextField()
	categoria = models.CharField(max_length=100)
	prioridade = models.CharField(
		choices=PRIORIDADE_CHOICES,
		max_length=10,
    )
	status = models.CharField(
		choices=STATUS_CHOICES,
		default="aberto",
		max_length=20,
    )
	criado_por = models.ForeignKey(
		User,
		related_name='tickets_criados',
		on_delete=models.CASCADE
    )
	atribuido_a = models.ForeignKey(
		User,
		related_name='tickets_atribuidos',
		on_delete=models.SET_NULL,
		null=True,
		blank=True
    )
	criado_em = models.DateTimeField(auto_now_add=True)
	atualizado_em = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.titulo

	class Meta:
		db_table = 'ticket'
		verbose_name = 'Ticket'
		verbose_name_plural = 'Tickets'
