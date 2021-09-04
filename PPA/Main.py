import numpy as np
import random
from PPA.Grafo import Grafo, GrafoCidades

infinito = 999999


def reconstruct_path(cameFrom, current):
    total_path = []
    total_path.append(current)
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.append(current)

    total_path.reverse()

    return total_path


def AEstrela(inicio, final, quantidadeDeVertex):
    caminho = {}
    NosAVisitar = []
    pontuacaoG = (np.ones(quantidadeDeVertex) * infinito)
    pontuacaoG[inicio] = 0
    pontuacaoF = (np.ones(quantidadeDeVertex) * infinito)
    pontuacaoF[inicio] = 0
    winer = inicio
    while True:
        atual = winer
        NosAVisitar.append(atual)
        if atual == final:
            caminhoCompleto = reconstruct_path(caminho, atual)
            return caminhoCompleto
        NosAVisitar.remove(atual)
        custoF = infinito
        for vizinho in grafo.vizinhos(atual):
            tentativaValor = grafo.custoG(atual, vizinho)
            if tentativaValor < pontuacaoG[vizinho]:
                if vizinho in caminho.keys():
                    continue
                caminho[vizinho] = atual
                pontuacaoG[vizinho] = tentativaValor
                if custoF > grafo.custoF(atual, vizinho):
                    winer = vizinho
                    custoF = grafo.custoF(atual, vizinho)
                    if vizinho not in NosAVisitar:
                        NosAVisitar.append(vizinho)


vertices = [[0, 1, 15], [0, 2, 10], [0, 3, 5], [1, 2, 20], [1, 4, 15], [2, 3, 20], [2, 4, 10],
            [3, 4, 5]]
numeroDeNos = 5
heuristica = [[0, 5], [1, 3], [2, 2.5], [3, 3], [4, 0]]
grafo = Grafo(numeroDeNos, vertices, heuristica)
objetivo = 4
nos = [0,1,2,3]
for i in range (10):
    noInicial = random.choice(nos)
    print(f'No inicial: {noInicial}, no Final {objetivo}')
    print(f'Caminho: {AEstrela(noInicial, objetivo,numeroDeNos)}')

grafo = GrafoCidades()
cidades = list(filter(lambda nome: nome!= 'Bucarest', grafo.nomes))
final = grafo.nomeParaIndex('Bucarest')
quantidadeDeVertex = grafo.quantidadeDeVertex()
for i in range(10):
    cidadeAleatoria = random.choice(cidades)
    inicio = grafo.nomeParaIndex(cidadeAleatoria)
    print(f'Cidade inicial: {cidadeAleatoria}, cidade final: Bucarest')
    caminhoIndex = AEstrela(inicio, final, quantidadeDeVertex)
    print(f'Caminho: {grafo.caminhoIndexToNome(caminhoIndex)}')
