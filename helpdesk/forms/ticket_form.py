from django import forms

from helpdesk.models.comentario import Comentario
from helpdesk.models.ticket import Ticket


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['titulo', 'descricao', 'categoria', 'prioridade']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }


class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['mensagem']
        widgets = {
            'mensagem': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Digite seu comentário...'}),
        }
