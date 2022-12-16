#ficheiro para o caso dos jogos com mais que um jogador
import math
from graph import graph
from algoritmos import algoritmos

#player tem como o id o seu index na lista players
#estado para o player n: ((coordenada atual, velocidade atual) bloco que esta a subtituir na matrix)
class multiplayer:
    def __init__(self, partida, fim, matriz):
        self.partida = partida
        self.fim = fim
        self.matriz = matriz

    #recebe a lista dos algoritmos que deve usar para cada jogador
    def run(self, algoritmosPlayer):
        if len(self.partida) != len(algoritmosPlayer):
            return None
        i = 0
        paths = []
        for nodos in self.partida:
            grafo = graph(nodos,self.matriz,self.fim)
            algs = algoritmos(grafo,nodos,self.fim,self.matriz,paths)
            path = None
            match algoritmosPlayer[i]:
                case "A*":
                    path = algs.AEstrela()
                case "Greedy":
                    path = algs.Greedy()
                case "DFS":
                    path = algs.DFS()
                case "BFS":
                    path = algs.BFS()
            paths.append(path)
            algs.plotPath(path)
            i += 1
        print(self.matriz)
        return paths