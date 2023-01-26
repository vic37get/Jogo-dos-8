from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from algoritmos.buscaEmLargura import buscaEmLarguraMain
from algoritmos.buscaEmProfundidade import buscaEmProfundidadeMain
from algoritmos.buscaGulosa import buscaGulosa
from algoritmos.aEstrela import buscaAEstrela
import numpy as np

# Create your views here.
def home(request):
    estadoFinal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    context = {
        'estadoFinal': estadoFinal,
    }
    template = loader.get_template('jogoApp/home.html')
    return HttpResponse(template.render(context, request))


def executaBusca(request):
    template = loader.get_template('jogoApp/jogoDos8.html')
    entrada = request.GET['entrada']
    algoritmo = request.GET['algoritmo']
    estadoFinal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    entrada = entrada.replace(' ', '')
    entrada = entrada.split(',')
    entrada = list(map(int, entrada))
    entrada = np.reshape(entrada, (3, 3)).tolist()
    if algoritmo != -1 and len(entrada) == 3:
        if algoritmo == 'buscaEmLargura':
            estadoAtual, custoCaminho, tam_fronteira, custoCaminho, profundidadeSolucao, profundidadeMaxima, iteracoes = buscaEmLarguraMain(entrada, estadoFinal)
            context = {
                'tipoBusca': 'Busca em Largura',
                'tabuleiro': iteracoes,
            }
            return HttpResponse(template.render(context, request))
        elif algoritmo == 'buscaEmProfundidade':
            estadoAtual, custoCaminho, tam_fronteira, custoCaminho, profundidadeSolucao, profundidadeMaxima, iteracoes = buscaEmProfundidadeMain(entrada, estadoFinal)
            context = {
                'tipoBusca': 'Busca em Profundidade',
                'tabuleiro': iteracoes,
            }
            return HttpResponse(template.render(context, request))
        
        elif algoritmo == 'buscaGulosa':
            estadoAtual, custoCaminho, tam_fronteira, custoCaminho, profundidadeSolucao, profundidadeMaxima, iteracoes = buscaGulosa(entrada, estadoFinal)
            context = {
                'tipoBusca': 'Busca em Gulosa',
                'tabuleiro': iteracoes,
            }
            return HttpResponse(template.render(context, request))
        
        elif algoritmo == 'buscaA*':
            estadoAtual, custoCaminho, tam_fronteira, custoCaminho, profundidadeSolucao, profundidadeMaxima, iteracoes = buscaAEstrela(entrada, estadoFinal)
            context = {
                'tipoBusca': 'Busca A*',
                'tabuleiro': iteracoes,
            }
            return HttpResponse(template.render(context, request))
            
    else:
        return redirect('/')
