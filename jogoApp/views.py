from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from algoritmos.buscaEmLargura import buscaEmLarguraMain
from algoritmos.buscaEmProfundidade import buscaEmProfundidadeMain

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
    estadoFinal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    entrada = entrada.replace(' ', '')
    entrada = entrada.split(',')
    entrada = list(map(int, entrada))
    print(entrada, len(entrada))
    print(0 in entrada)
    if algoritmo != '-1' and len(entrada) == 9:
        print('ENTRADAAAAAAAAAAAAAAA: ', entrada, type(entrada))
        if algoritmo == 'buscaEmLargura':
            solucao, fronteira, nosGerados, profundidadeMaxima, profundidadeSolucao, estadosVisitados, iteracoes = buscaEmLarguraMain(entrada, estadoFinal)
            context = {
                'tipoBusca': 'Busca em Largura',
                'tabuleiro': iteracoes,
            }
            return HttpResponse(template.render(context, request))
        elif algoritmo == 'buscaEmProfundidade':
            solucao, fronteira, nosGerados, profundidadeMaxima, profundidadeSolucao, estadosVisitados, iteracoes = buscaEmProfundidadeMain(entrada, estadoFinal)
            context = {
                'tipoBusca': 'Busca em Profundidade',
                'tabuleiro': iteracoes,
            }
            return HttpResponse(template.render(context, request))
    else:
        return redirect('/')
