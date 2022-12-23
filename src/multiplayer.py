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
        vs=[]
        for nodos in self.partida:
            grafo = graph(nodos,self.matriz,self.fim)
            algs = algoritmos(grafo,nodos,self.fim,self.matriz,paths)
            path = None
            match algoritmosPlayer[i]:
                case "A*":
                    path,v = algs.AEstrela()
                case "Greedy":
                    path,v = algs.Greedy()
                case "DFS":
                    path,v = algs.DFS()
                case "BFS":
                    path,v = algs.BFS()
            paths.append(path)
            vs.append(v)
            algs.plotPath(path)
            i += 1
        #print(self.matriz)
        return paths,v