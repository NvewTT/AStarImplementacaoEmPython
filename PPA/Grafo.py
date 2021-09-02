import numpy as np


class Grafo:
    def __init__(self, numeroNos, verteces, heuristica):
        self.matrizAdjacencia = self.criaMatrizAdjacencia(numeroNos, verteces)
        self.valorH = self.criaValoresH(numeroNos, heuristica)

    @staticmethod
    def criaMatrizAdjacencia(numeroDeNos, verteces):
        matrizDeCustos = np.zeros((numeroDeNos, numeroDeNos))
        for vertex in verteces:
            matrizDeCustos[vertex[0], vertex[1]] = vertex[2]
            matrizDeCustos[vertex[1], vertex[0]] = vertex[2]
        return matrizDeCustos

    @staticmethod
    def criaValoresH(numeroDeNos, heuristica):
        custosH = np.zeros(numeroDeNos)
        for no in heuristica:
            custoGDoNo = no[1]
            custosH[no[0]] = custoGDoNo
        return custosH

    def custoH(self, no):
        return self.valorH[no]

    def custoG(self, noAnterior, no):
        return self.matrizAdjacencia[no, noAnterior]

    def custoF(self, anterior, atual):
        return self.custoH(atual) + self.custoG(anterior, atual)

    def vizinhos(self, no):
        return np.where(self.matrizAdjacencia[no, :] > 0)[0]


class GrafoCidades:
    def __init__(self):
        self.matrixDeAdjacencia = np.genfromtxt('custos.csv', delimiter=',',dtype=np.int)
        self.nomes = self.obtemNomes()
        self.valoresH = self.criaValoresH()

    @staticmethod
    def obtemNomes():
        dicionarioNomes = {}
        with open('cidades.txt') as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
        for i, nome in enumerate(lines):
            dicionarioNomes[nome] = i
        return dicionarioNomes

    def nomeParaIndex(self, nome):
        return self.nomes[nome]

    def indexParaNome(self, index):
        listaDeNomes = list(self.nomes.keys())
        listaDeIndex = list(self.nomes.values())
        possicaoDoIndex = listaDeIndex.index(index)
        nome = listaDeNomes[possicaoDoIndex]
        return nome

    @staticmethod
    def criaValoresH():
        with open('distancias.txt') as file:
            linhas = file.readlines()
            linhas = [line.rstrip() for line in linhas]
        valoresH = list(map(int, linhas))
        return valoresH

    def quantidadeDeVertex(self):
        return self.matrixDeAdjacencia.shape[0]

    def custoH(self, no):
        return self.valoresH[no]

    def custoG(self, atual, vizinho):
        return self.matrixDeAdjacencia[vizinho, atual]

    def custoF(self, atual, vizinho):
        return self.custoH(vizinho) + self.custoG(atual, vizinho)

    def vizinhos(self, no):
        return np.where(self.matrixDeAdjacencia[no, :] > 0)[0]

    def caminhoIndexToNome(self, caminho):
        return [self.indexParaNome(index) for index in caminho ]