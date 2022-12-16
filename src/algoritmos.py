import graph as g
import math
import queue

class algoritmos:
    def __init__(self, grafo: g,inicio,fim, matriz = None, paths = []):
        self.end = fim
        self.start = inicio
        self.grafo = grafo.getGrafo()
        self.graph = grafo
        self.matrix = matriz
        self.paths = paths

    def plotPath(self, path):
        i = 0
        for ((x,y), vel) in path:
            self.matrix[y][x] = str(i)
            i += 1

    def calculaReta(self,estado):
        nodoPlayer, velPlayer = estado
        if velPlayer[0] == 0:
            return math.inf, velPlayer[1]
        m = velPlayer[1] / velPlayer[0]
        b = nodoPlayer[1] - (nodoPlayer[0] * m)
        return m,b

    def calculaPonto(self,path,estadoFinal):
        m0,b0 = self.calculaReta(estadoFinal)
        m1, b1 = self.calculaReta(path)
        ponto = None
        if m1 == math.inf and m0 != math.inf:
            if m0 == 0:
                ponto = b0,b1
            else:
                ponto = (b1 - b0)/ m0 ,b1
        elif m0 == math.inf and m1 != math.inf:
            if m1 == 0:
                ponto = b1,b0
            else:
                ponto = (b0 - b1)/m1, b0
        elif m0 != 0 and m1 != 0 and m1 != math.inf and m0 != math.inf and m1 != m0:
            x = (b0 - b1) / (m1 - m0)
            ponto = x, (m0 * x) + b0
        return ponto

    def colisao(self, estadoFinal, play: int, estadoInicial):
        if self.matrix is None or len(self.paths) <= 0:
            return True
        nodoPlayer, velPlayer = estadoFinal
        if 0 < nodoPlayer[0] < len(self.matrix[0]) and 0 < nodoPlayer[1] < len(self.matrix):
            for path in self.paths:
                if len(path) <= play:
                    return True
                ponto = self.calculaPonto(path[play],estadoFinal)
                if ponto is None:
                    return self.matrix[nodoPlayer[1]][nodoPlayer[0]] != str(play)
                x,y = ponto
                if min(estadoInicial[0][0],estadoFinal[0][0]) <= x <= max(estadoInicial[0][0],estadoFinal[0][0]) and min(estadoInicial[0][1],estadoFinal[0][1]) <= y <= max(estadoInicial[0][1],estadoFinal[0][1]) and min(path[play-1][0][0], path[play][0][0]) <= x <= max(path[play-1][0][0], path[play][0][0]) and min(path[play-1][0][1], path[play][0][1]) <= y <= max(path[play-1][0][1], path[play][0][1]):
                    distanciaPlayer0 = self.graph.calcBestHeuristica([((x,y),estadoInicial[1])],[estadoFinal[0]],False)
                    distanciaPlayer1 = self.graph.calcBestHeuristica([((x,y),estadoInicial[1])],[path[play][0]],False)
                    speedPlayer0 = math.sqrt((estadoInicial[0][1]^2) + (estadoInicial[0][0]^2))
                    speedPlayer1 = math.sqrt((path[play-1][0][1]^2) + (path[play-1][0][0]^2))
                    tempoPlayer0 = round(distanciaPlayer0/speedPlayer0,1)
                    tempoPlayer1 = round(distanciaPlayer1/speedPlayer1,1)
                    return self.matrix[nodoPlayer[1]][nodoPlayer[0]] != str(play) and tempoPlayer0 != tempoPlayer1
                else:
                    return self.matrix[nodoPlayer[1]][nodoPlayer[0]] != str(play)
        else:
            return False

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
                pathUntilNow.append(estado)
                # se o filho for um dos nodos finais retorna o caminho
                if estado[0] in self.end:
                    return pathUntilNow
                # se não e não estiver nos visitados adiciona-o ao nodos ainda por visitar e caso seja multiplayer nao haja colisao
                elif estado not in visitados and self.colisao(estado,len(pathUntilNow),best[0]):
                    visitados.append(estado)
                    possiveis.append((estado, self.graph.calcBestHeuristica(pathUntilNow, self.end), pathUntilNow))

    def Greedy(self,ponto = None,path=[],visited=set()):
        if ponto == None:
            visited = set()
            ponto = (self.start,(0,0))
        path.append(ponto)
        visited.add(ponto)
        best_nodes = []
        if ponto[0] in self.end:
            return path
        for (adjacente, peso) in self.grafo[ponto]:
             if adjacente not in visited:
                 best_nodes.append((adjacente, peso))
        best_nodes.sort(key = lambda a: a[1])
        resultado = None
        while resultado is None and len(best_nodes) > 0:
           best_node = best_nodes.pop(0)
           if self.graph.estadoPossivel(best_node[0][0]) and self.colisao(best_node[0], len(path), ponto):
                oldPath = path.copy()
                resultado = self.Greedy(best_node[0],path,visited)
                path = oldPath
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
                    nodo_atual_path = nodo_atual[1].copy()
                    nodo_atual_path.append(adjacente)
                    if adjacente not in visited and self.colisao(adjacente[0],len(nodo_atual_path),nodo_atual):
                        stack.append((adjacente, nodo_atual_path, nodo_atual[2] + peso))
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
                    if adjacente not in visited and self.colisao(adjacente,len(nodo_atual[1]),nodo_atual):
                        fila.put((adjacente,nodo_atual[1]+[adjacente],nodo_atual[2]+peso))
                        visited.add(adjacente)