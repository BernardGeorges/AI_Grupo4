# Biblioteca de tratamento de grafos necessária para desenhar graficamente o grafo
import queue
import time
import networkx as nx
# Biblioteca de tratamento de grafos necessária para desenhar graficamente o grafo
import matplotlib.pyplot as plt

# biblioteca necessária para se poder utilizar o valor math.inf  (infinito)
import math
import pygame

from xmlrpc.client import Boolean


class graph:
    # o x se encontra na pos[0]
    X = 0
    # Y se encontra no pos[1]
    Y = 1

    def __init__(self, partida, matriz, fim):
        self.matrix = matriz
        self.end = fim
        self.ac = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        self.grafo = self.criaGrafo(partida, (0, 0))
        pygame.init()

    def getGrafo(self):
        return self.grafo

    def createSquare(self, x, y, color, janela, x1, y1, x2, y2):
        r = pygame.draw.rect(janela, color, [x, y, math.ceil(x1 / x2), math.ceil(y1 / y2)])
        return r

    def plot(self, janela, x1, y1):
        y2 = len(self.matrix)
        x2 = len(self.matrix[0])
        y = 0
        for row in self.matrix:
            x = 0
            for item in row:
                if item == 'X':
                    self.createSquare(x, y, (255, 255, 255), janela, x1, y1, x2, y2)
                elif item == 'P':
                    self.createSquare(x, y, (0, 255, 0), janela, x1, y1, x2, y2)
                elif item == 'F':
                    self.createSquare(x, y, (255, 0, 0), janela, x1, y1, x2, y2)
                else:
                    self.createSquare(x, y, (128, 128, 128), janela, x1, y1, x2, y2)
                x += x1 / x2
            y += y1 / y2
        pygame.display.update()
        return x, y

    def plotpaths(self,janela,paths, x1, y1):
        i=1
        self.plot(janela,x1,y1)
        for path in paths:
            self.plotpath(janela,path,x1,y1, False,i)
            i=i+1

    # Faz a representação em VectorRace do circuito
    def plotpath(self, janela, path, x1, y1, repeat = True, i =1):
        y2 = len(self.matrix)
        x2 = len(self.matrix[0])
        if i ==1:
            color=(0,0,255)
        elif i == 2:
            color=(255,0,0)
        elif i == 3:
            color=(0,255,0)
        elif i == 4:
            color=(0,255,255)
        elif i == 5:
            color= (255,0,255)
        elif i == 6:
            color = (255,255,0)
        else:
            color = (150, 75, 0)

        if repeat:
            y = 0
            for row in self.matrix:
                x = 0
                for item in row:
                    if item == 'X':
                        self.createSquare(x, y, (255, 255, 255), janela, x1, y1, x2, y2)
                    elif item == 'P':
                        self.createSquare(x, y, (0, 255, 0), janela, x1, y1, x2, y2)
                    elif item == 'F':
                        self.createSquare(x, y, (255, 0, 0), janela, x1, y1, x2, y2)
                    else:
                        self.createSquare(x, y, (128, 128, 128), janela, x1, y1, x2, y2)
                    x += x1 / x2
                y += y1 / y2
        for (x, y), vel in path:
            plotX = x * x1 / x2
            plotY = y * y1 / y2
            # time.sleep(1)
            self.createSquare(plotX, plotY, color, janela, x1, y1, x2, y2)
        pygame.display.update()  # inutil nao sei pq e que ta aqui

    def plotpathreset(self, janela, path, x1, y1):
        y2 = len(self.matrix)
        x2 = len(self.matrix[0])
        for (x, y), vel in path:
            plotX = x * x1 / x2
            plotY = y * y1 / y2
            r = self.createSquare(plotX, plotY, (128, 128, 128), janela, x1, y1, x2, y2)
            janela.blit(janela, plotX, plotY)
        pygame.display.update()

    def plotpathupdate(self, janela, path, x1, y1, blitx,blity,screen):
        
        y2 = len(self.matrix)
        x2 = len(self.matrix[0])

        for (x, y), vel in path:
            plotX = x * x1 / x2
            plotY = y * y1 / y2
            time.sleep(0.3)
            self.createSquare(plotX, plotY, (0, 0, 255), janela, x1, y1, x2, y2)
            screen.blit(janela, (blitx,blity))
            pygame.display.update()

    def __str__(self):
        out = " "
        for k in self.grafo.keys():
            out = out + "node " + str(k) + ": " + str(self.grafo[k]) + "\n"
        return out

    # funcao que cria e devolve o grafo de todos os estados possiveis
    # Grafo é: key = estado, ou seja, (nodo,velocidade), values são seus filhos: (estado: (nodo,velocidade), peso)
    def criaGrafo(self, pos, vel):
        porVisitar = [(pos, vel)]
        grafo = {}
        first = True
        while len(porVisitar) > 0:
            posicao, velocidade = porVisitar.pop(0)
            if (posicao, velocidade) not in grafo.keys():
                grafo[(posicao, velocidade)] = set()
                for aceleracao in self.ac:
                    nextPos, nextVel = self.calcNextPos(posicao, velocidade, aceleracao), self.calcVel(velocidade,
                                                                                                       aceleracao)
                    if ((nextPos, nextVel) not in grafo.keys() or first) and self.estadoPossivel(
                            nextPos) and self.passagemPossivel(posicao, nextPos, True):
                        grafo[(posicao, velocidade)].add(
                            ((nextPos, nextVel), self.calcBestHeuristica([(posicao, velocidade)], self.end, False)))
                        porVisitar.append((nextPos, nextVel))
                    elif (nextPos, nextVel) not in grafo.keys():
                        grafo[(posicao, velocidade)].add(((nextPos, nextVel),
                                                          25 * self.calcBestHeuristica([(posicao, velocidade)],
                                                                                       self.end, False)))
                        grafo[(nextPos, nextVel)] = set()
                        grafo[(nextPos, nextVel)].add(((posicao, velocidade), 250))
                first = False
        return grafo

    # calcula a melhor heuristica em relação aos possiveis fins. Escolhe o melhor final para se ter
    # argumento isAEstrela permite utilizar esta função para ambos as pesquisas caso ser falsa ela não calcula o custo do path
    # recebe o path = lista de (nodo, velocidade) e uma lista de fins possiveis = nodos
    def calcBestHeuristica(self, path, end, isAEstrela=True):
        i = len(path) - 1
        (x1, y1) = ponto = path[i][0]
        i -= 1
        best = math.inf
        for x2, y2 in end:
            tenta = math.sqrt((math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)))
            if (tenta < best):
                best = tenta
        if isAEstrela:
            first = ponto
            while i >= 0:
                for (nodo2, velocidade), peso in self.grafo[path[i]]:
                    if nodo2 == first:
                        best += peso
                first = path[i][0]
                i -= 1
        return best

    # calcula o proximo nodo em relação a velocidade e aceleração (formula dada pelo stor)
    def calcNextPos(self, posAtual, vel, ac):
        (pL, pC) = posAtual
        (vL, vC) = vel
        (aL, aC) = ac
        retPL = pL + vL + aL
        retPC = pC + vC + aC
        return (retPL, retPC)

    # calcula a nova velocidade (formula dada pelo stor)
    def calcVel(self, vel, acel):
        (vl, vc) = vel
        (al, ac) = acel
        retVL = vl + al
        retVC = vc + ac
        return (retVL, retVC)

    # remove da lista de nodos seguintes todos que passem pelo o nodo atual (nota: devia ter um já visitados para retirar tmb)
    def removePossiveis(self, next, possiveis):
        for (nodo, velAtual, acelAtual, heuristica, path) in possiveis:
            if next == nodo:
                possiveis.remove((nodo, velAtual, acelAtual, heuristica, path))
        return possiveis

    # verifica se pos não é uma posição valida para um futuro movimento (ou seja devolve true se for parede ou se a posição estiver fora do mapa)
    def estadoPossivel(self, pos):
        return (0 < pos[self.X] < len(self.matrix[0]) and 0 < pos[self.Y] < len(self.matrix) and
                self.matrix[pos[self.Y]][pos[self.X]] != 'X')

    # verifica se há uma passagem direta entre o inicio (coordenadas da possição inicial) e fim (pos final)
    def passagemPossivel(self, inicio, fim, first: bool, ac=[]):
        if inicio == fim:
            return True
        else:
            if first:
                ac = []
            if len(ac) == 0:
                difX, difY = fim[0] - inicio[0], fim[1] - inicio[1]
                if difX > 0:
                    ac.append((1, 0))
                elif difX < 0:
                    ac.append((-1, 0))
                if difY > 0:
                    ac.append((0, 1))
                    if (ac[0][0], 1) not in ac:
                        ac.append((ac[0][0], 1))
                elif difY < 0:
                    ac.append((0, -1))
                    if (ac[0][0], -1) not in ac:
                        ac.append((ac[0][0], -1))
            factor = ac[len(ac) - 1]
            filhos = []
            for vel in ac:
                x, y = inicio[0] + vel[0], inicio[1] + vel[1]
                if x * factor[0] <= fim[0] * factor[0] and y * factor[1] <= fim[1] * factor[1] and self.estadoPossivel(
                        (x, y)):
                    filhos.append(((x, y), self.calcBestHeuristica([((x, y), (0, 0))], [fim], False)))
            filhos.sort(key=lambda a: a[1])
            result = False
            while len(filhos) > 0 and result is False:
                best = filhos.pop(0)
                result = self.passagemPossivel(best[0], fim, False, ac)
            return result

    def custoFinal(self, response):
        caminho = []
        custo = 0
        for i in response:
            caminho.append(i[0])
        for passo in caminho:
            if self.matrix[passo[1]][passo[0]] == "X":
                custo += 25
            else:
                custo += 1
        custo -= 1  # nodo inicial
        return custo

    def desenha(self):
        ##criar lista de vertices
        lista_v = self.grafo
        g = nx.Graph()
        # Converter para o formato usado pela biblioteca networkx
        for nodo in lista_v.keys():
            n = nodo[0]
            g.add_node(n)
            for (estado, peso) in self.grafo[nodo]:
                g.add_edge(n, estado[0], weight=peso)
        # desenhar o grafo
        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
        plt.draw()
        plt.show()