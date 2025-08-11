from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from helpdesk.models.artigo import ArtigoConhecimento

@login_required
def artigo_list(request):
    artigos = ArtigoConhecimento.objects.filter(publico=True)
    return render(request, 'kb/artigo_list.html', {'artigos': artigos})

@login_required
def artigo_detail(request, artigo_id):
    artigo = get_object_or_404(ArtigoConhecimento, id=artigo_id, publico=True)
    return render(request, 'kb/artigo_detail.html', {'artigo': artigo})
