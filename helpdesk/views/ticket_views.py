from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from helpdesk.models.ticket import Ticket
from helpdesk.forms.ticket_form import (
    ComentarioForm,
    TicketForm,
)


@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def ticket_list(request):
    if request.user.groups.filter(name='Agente').exists():
        tickets = Ticket.objects.all()
    else:
        tickets = Ticket.objects.filter(criado_por=request.user)
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})


@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    comentarios = ticket.comentarios.all()
    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.ticket = ticket
            comentario.autor = request.user
            comentario.save()
            return redirect('ticket_detail', ticket_id=ticket.id)
    else:
        comentario_form = ComentarioForm()
    return render(request, 'tickets/ticket_detail.html', {
        'ticket': ticket,
        'comentarios': comentarios,
        'comentario_form': comentario_form
    })


@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.criado_por = request.user
            ticket.save()
            return redirect('ticket_detail', ticket_id=ticket.id)
    else:
        form = TicketForm()
    return render(request, 'tickets/ticket_form.html', {'form': form})
