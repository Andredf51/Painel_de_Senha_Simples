from django.shortcuts import render
from perfis_senhas.models import Senha
from perfis_senhas.models import Tipo_senha
from perfis_senhas.models import Categoria_senha
from perfis_senhas.models import Status_senha


# Create your views here.

def index(request):
    return render(request, 'index.html', { 'perfis' : Senha.objects.all()})

def exibir(request, perfil_id):

    perfil = Senha.objects.get(id=perfil_id)
    return render(request, 'perfil.html', { "perfil" : perfil})