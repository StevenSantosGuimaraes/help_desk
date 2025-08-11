from django.contrib.auth.models import User
from django.db import models

from helpdesk.models.ticket import Ticket


class Comentario(models.Model):
	
	ticket = models.ForeignKey(Ticket, related_name='comentarios', on_delete=models.CASCADE)
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	mensagem = models.TextField()
	criado_em = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Comentário de {self.autor} em {self.ticket}"

	class Meta:
		db_table = 'comentario'
		verbose_name = 'Comentário'
		verbose_name_plural = 'Comentários'
