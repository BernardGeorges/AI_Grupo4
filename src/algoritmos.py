import graph as g
import math
import queue

class algoritmos:
    def __init__(self, grafo: g,inicio,fim):
        self.end = fim
        self.start = inicio
        self.grafo = grafo.getGrafo()
        self.graph = grafo

        # algoritmo de pesquisa A*
    def AEstrela(self):
        # possiveis = list de (estado: (coordenada,velocidade), heuristica, path tomado)
        possiveis = [((self.start, (0, 0)), self.graph.calcBestHeuristica([(self.start, (0, 0))], self.end),
                      [(self.start, (0, 0))])]
        visitados = [(self.start, (0, 0))]
        while len(possiveis) > 0:
            # best = (estado, heuristica em A*,path)
            best = (((0, 0), (0, 0)), math.inf, [])
            # por todos os nodos possiveis de visitar encontra o com a melhor heuristica
            for estado, heuristica, path in possiveis:
                if heuristica < best[1]:
                    best = (estado, heuristica, path)
            # remove o nodo que vai visitar dos nodos que falta visitar
            possiveis.remove(best)
            # para todos os seus filhos:
            for estado, peso in self.grafo[best[0]]:
                pathUntilNow = best[2].copy()
                # se o filho for um dos nodos finais retorna o caminho
                if estado[0] in self.end:
                    best[2].append(estado)
                    return best[2]
                # se não e não estiver nos visitados adiciona-o ao nodos ainda por visitar
                elif estado not in visitados:
                    pathUntilNow.append(estado)
                    visitados.append(estado)
                    possiveis.append((estado, self.graph.calcBestHeuristica(pathUntilNow, self.end), pathUntilNow))

    def Greedy(self,ponto = None,path=[],visited=set()):
        if ponto == None:
            ponto = (self.start,(0,0))
        path.append(ponto)
        visited.add(ponto)
        best_nodes = []
        if ponto[0] in self.end:
            return path
        for (adjacente, peso) in self.grafo[ponto]:
             if adjacente not in visited:
                 best_nodes.append((adjacente, self.graph.calcBestHeuristica([ponto],self.end,False)))
        best_nodes.sort(key = lambda a: a[1])
        resultado = None
        while resultado is None and len(best_nodes) > 0:
           best_node = best_nodes.pop(0)
           if self.graph.estadoPossivel(best_node[0][0]):
                resultado = self.Greedy(best_node[0],path,visited)
        return resultado

    def DFS(self):
        visited = set()
        stack = []
        # adicionar o nodo inicial à fila e aos visitados
        stack.append(((self.start, (0, 0)), [(self.start, (0, 0))], 0))
        visited.add((self.start, (0, 0)))
        while len(stack) > 0:
            nodo_atual = stack.pop()
            if nodo_atual[0][0] in self.end:
                return nodo_atual[1]
            else:
                for (adjacente, peso) in self.grafo[nodo_atual[0]]:
                    if adjacente not in visited:
                        stack.append((adjacente, nodo_atual[1] + [adjacente], nodo_atual[2] + peso))
                        visited.add(adjacente)

    def BFS(self):
        # definir nodos visitados para evitar ciclos
        visited = set()
        fila = queue.Queue()
        # adicionar o nodo inicial à fila e aos visitados
        fila.put(((self.start,(0,0)),[(self.start,(0,0))],0))
        visited.add((self.start,(0,0)))
        while not fila.empty():
            nodo_atual = fila.get()
            if nodo_atual[0][0] in self.end:
                return nodo_atual[1]
            else:
                for (adjacente, peso) in self.grafo[nodo_atual[0]]:
                    if adjacente not in visited:
                        fila.put((adjacente,nodo_atual[1]+[adjacente],nodo_atual[2]+peso))
                        visited.add(adjacente)