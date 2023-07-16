from django.shortcuts import render
from .models import Colaborador

def home (request):
    return render(request, 'colaboradores/home.html')


def base (request):
    
    return render(request, 'colaboradores/base.html')


def colaboradores (request):
    #Salva os dados da tela para o banco de dados.
    novo_colaborador = Colaborador()
    novo_colaborador.nome = request.POST.get('nome')
    novo_colaborador.email = request.POST.get('email')
    novo_colaborador.departamento = request.POST.get('departamento')
    novo_colaborador.save()
    # Exibe todos os colaboradores já cadastrados em uma nova página
    colaboradores = {
        'colaboradores': Colaborador.objects.all()
    }

    #Retorno dos dados para a página de listagem de usuários
    return render(request, 'colaboradores/colaboradores.html', colaboradores)

def listaColaboradores (request):
    colaboradores = {
        'colaboradores': Colaborador.objects.all()
    }
    return render(request, 'colaboradores/painelcontrole.html', colaboradores)

def deletar (request, id):
    colaborador = Colaborador.objects.filter(id_colaborador = id)
    colaborador.delete()
    colaboradores = {
        'colaboradores': Colaborador.objects.all()
    }
    return render(request, 'colaboradores/painelcontrole.html', colaboradores)


def editar (request, id):
    #Salva os dados da tela para o banco de dados.
    colaborador = Colaborador.objects.filter(id_colaborador = id)
    colaborador.update(nome = request.POST.get('nome'), email = request.POST.get('email'), departamento = request.POST.get('departamento'))
    # Exibe todos os colaboradores já cadastrados em uma nova página
    colaboradores = {
        'colaboradores': Colaborador.objects.all()
    }
    return render(request, 'colaboradores/painelcontrole.html', colaboradores)