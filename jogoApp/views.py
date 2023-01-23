from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from algoritmos.buscaEmLargura import buscaEmLarguraMain
from algoritmos.buscaEmProfundidade import buscaEmProfundidadeMain

# Create your views here.
def home(request):
    context = {}
    template = loader.get_template('jogoApp/home.html')
    return HttpResponse(template.render(context, request))

def buscaEmLargura(request):
    estadoInicial = [1, 2, 3, 4, 5, 6, 0, 7, 8]
    estadoFinal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    solucao, fronteira, nosGerados, profundidadeMaxima, profundidadeSolucao, estadosVisitados, iteracoes = buscaEmLarguraMain(estadoInicial, estadoFinal)
    context = {
        'tipoBusca': 'Busca em Largura',
        'tabuleiro': iteracoes,
    }
    template = loader.get_template('jogoApp/jogoDos8.html')
    return HttpResponse(template.render(context, request))

def buscaEmProfundidade(request):
    estadoInicial = [1, 2, 3, 4, 5, 6, 0, 7, 8]
    estadoFinal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    solucao, fronteira, nosGerados, profundidadeMaxima, profundidadeSolucao, estadosVisitados, iteracoes = buscaEmProfundidadeMain(estadoInicial, estadoFinal)
    context = {
        'tipoBusca': 'Busca em Profundidade',
        'tabuleiro': iteracoes,
    }
    template = loader.get_template('jogoApp/jogoDos8.html')
    return HttpResponse(template.render(context, request))

