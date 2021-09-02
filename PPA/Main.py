import numpy as np

from PPA.Grafo import Grafo, GrafoCidades


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
    openList = []
    pontuacaoG = (np.ones(quantidadeDeVertex) * 999999)
    pontuacaoG[inicio] = 0
    pontuacaoF = (np.ones(quantidadeDeVertex) * 999999)
    pontuacaoF[inicio] = 0
    winer = inicio
    while True:
        atual = winer
        openList.append(atual)
        if atual == final:
            caminhoCompleto = reconstruct_path(caminho, atual)
            return caminhoCompleto
        openList.remove(atual)
        custoF = 9999999
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
                    if vizinho not in openList:
                        openList.append(vizinho)


vertices = [[0, 1, 15], [0, 2, 10], [0, 3, 5], [1, 2, 20], [1, 4, 15], [2, 3, 20], [2, 4, 10],
            [3, 4, 5]]
numeroDeNos = 5
heuristica = [[0, 5], [1, 3], [2, 2.5], [3, 3], [4, 0]]
grafo = Grafo(numeroDeNos, vertices, heuristica)
noInicial = 0
objetivo = 4


print(AEstrela(noInicial, objetivo,numeroDeNos))

grafo = GrafoCidades()
inicio = grafo.nomeParaIndex('Lugoj')
final = grafo.nomeParaIndex('Bucarest')
quantidadeDeVertex = grafo.quantidadeDeVertex()
caminhoIndex = AEstrela(inicio, final, quantidadeDeVertex)
print(grafo.caminhoIndexToNome(caminhoIndex))
