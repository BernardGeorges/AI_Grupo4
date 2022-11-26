# Biblioteca de tratamento de grafos necessária para desenhar graficamente o grafo
import queue
import networkx as nx
# Biblioteca de tratamento de grafos necessária para desenhar graficamente o grafo
import matplotlib.pyplot as plt

#biblioteca necessária para se poder utilizar o valor math.inf  (infinito)
import math
import pygame

from xmlrpc.client import Boolean



class graph:

    #o x se encontra na pos[0]
    X = 0
    # Y se encontra no pos[1]
    Y = 1
    
    def __init__(self,partida,fim,matriz):
        self.start = partida
        self.end = fim
        self.matrix = matriz
        self.ac = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
        self.grafo = self.criaGrafo(partida,(0,0))
        pygame.init()
        self.largura = 15
        self.altura = 15
        self.janela = pygame.display.set_mode((30*len(matriz), 30*len(matriz[0])))


    def createSquare(self,x, y, color):
        pygame.draw.rect(self.janela, color, [x, y, self.largura , self.altura])

    #Faz a representação em VectorRace do circuito
    def plot(self):
        y = 0
        for row in self.matrix:
            x = 0
            for item in row:
                if item == 'X':
                    self.createSquare(x, y, (255, 255, 255))
                elif item == 'P':
                    self.createSquare(x,y,(0,255,0))
                elif item == 'F':
                    self.createSquare(x,y,(255,0,0))
                else:
                    self.createSquare(x, y, (128,128,128))

                x += self.largura
            y += self.altura
        pygame.display.update()

    def __str__(self):
        out = " "
        for k in self.grafo.keys():
            out = out + "node " + str(k) + ": " + str(self.grafo[k]) + "\n"
        return out

     #funcao que cria e devolve o grafo dos estados possiveis
    def criaGrafo(self,pos, vel):
        porVisitar = [(pos,vel)]
        grafo = {}
        first = True
        while len(porVisitar) > 0:
            posicao, velocidade = porVisitar.pop(0)
            if posicao not in grafo.keys():
                grafo[posicao] = set()
            for aceleracao in self.ac:
                nextPos,nextVel = self.calcNextPos(posicao,velocidade,aceleracao),self.calcVel(velocidade,aceleracao)
                if (nextPos not in grafo.keys() or first) and self.estadoPossivel(nextPos):
                    grafo[posicao].add((nextPos,1))
                    porVisitar.append((nextPos,nextVel))
                else:
                    grafo[posicao].add((nextPos,25))
            first = False
        return grafo

    #calcula a melhor heuristica em relação aos possiveis fins. Escolhe o melhor final para se ter
    def calcBestHeuristica(self,path):
        i = len(path) - 1
        (x1,y1) = ponto = path[i]
        i -= 1
        best = math.inf
        for x2,y2 in self.end:
            tenta = math.sqrt((math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)))
            if(tenta < best):
                best = tenta
        first = ponto
        while i >= 0 :
            for nodo2, peso in self.grafo[path[i]]:
                    if nodo2 == first:
                        best += peso
            first = path[i]
            i -= 1
        return best

    #calcula o proximo nodo em relação a velocidade e aceleração (formula dada pelo stor)
    def calcNextPos(self,posAtual,vel,ac):
        (pL,pC) = posAtual
        (vL,vC) = vel
        (aL,aC) = ac
        retPL = pL + vL + aL
        retPC = pC + vC + aC
        return (retPL,retPC)

    #calcula a nova velocidade (formula dada pelo stor)
    def calcVel(self,vel,acel):
        (vl,vc) = vel
        (al,ac) = acel
        retVL = vl + al
        retVC = vc + ac
        return (retVL,retVC)

    #remove da lista de nodos seguintes todos que passem pelo o nodo atual (nota: devia ter um já visitados para retirar tmb)
    def removePossiveis(self,next,possiveis):
        for (nodo, velAtual, acelAtual, heuristica,path) in possiveis:
            if next == nodo:
                possiveis.remove((nodo, velAtual, acelAtual, heuristica,path))
        return possiveis

   # verifica se pos não é uma posição valida para um futuro movimento (ou seja devolve true se for parede ou se a posição estiver fora do mapa)
    def estadoPossivel(self,pos):
        return ( 0 < pos[self.X] < len(self.matrix[0]) and 0 < pos[self.Y] < len(self.matrix) and self.matrix[pos[self.Y]][pos[self.X]] != 'X')

    #algoritmo de pesquisa A*
    def AEstrela(self):
        possiveis = [(self.start,self.calcBestHeuristica([self.start]),[self.start])]
        visitados = [self.start]
        while len(possiveis) > 0:
            best = ((0,0),math.inf)
            for nodo, heuristica, path in possiveis:
                if heuristica < best[1]:
                    best = (nodo,heuristica,path)
            possiveis.remove(best)
            for nodos, peso in self.grafo[best[0]]:
                pathUntilNow = best[2].copy()
                if nodos in self.end:
                    best[2].append(nodos)
                    return best[2]
                elif nodos not in visitados:
                    pathUntilNow.append(nodos)
                    visitados.append(nodos)
                    possiveis.append((nodos,self.calcBestHeuristica(pathUntilNow),pathUntilNow))

