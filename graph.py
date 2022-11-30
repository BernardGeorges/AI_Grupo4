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



    def createSquare(self,x, y, color,janela):
        pygame.draw.rect(janela, color, [x, y, self.largura, self.altura])

    #Faz a representação em VectorRace do circuito
    def plot(self,janela,path):
        y = 0
        for row in self.matrix:
            x = 0
            for item in row:
                if item == 'X':
                    self.createSquare(x, y, (255, 255, 255),janela)
                elif item == 'P':
                    self.createSquare(x,y,(0,255,0),janela)
                elif item == 'F':
                    self.createSquare(x,y,(255,0,0),janela)
                else:
                    self.createSquare(x, y, (128,128,128),janela)
                x += self.largura
            y += self.altura
        for (x,y), vel in path:
            plotX = x * self.largura
            plotY = y * self.altura
            self.createSquare(plotX, plotY, (0, 0, 255), janela)
        pygame.display.update()


    def __str__(self):
        out = " "
        for k in self.grafo.keys():
            out = out + "node " + str(k) + ": " + str(self.grafo[k]) + "\n"
        return out

    #funcao que cria e devolve o grafo de todos os estados possiveis
    #Grafo é: key = estado, ou seja, (nodo,velocidade), values são seus filhos: (estado: (nodo,velocidade), peso)
    def criaGrafo(self,pos, vel):
        porVisitar = [(pos,vel)]
        grafo = {}
        first = True
        while len(porVisitar) > 0:
            posicao, velocidade = porVisitar.pop(0)
            if (posicao,velocidade) not in grafo.keys():
                grafo[(posicao,velocidade)] = set()
                for aceleracao in self.ac:
                    nextPos,nextVel = self.calcNextPos(posicao,velocidade,aceleracao),self.calcVel(velocidade,aceleracao)
                    if ((nextPos,nextVel) not in grafo.keys() or first) and self.estadoPossivel(nextPos) and self.passagemPossivel(posicao,nextPos):
                        grafo[(posicao,velocidade)].add(((nextPos,nextVel),self.calcBestHeuristica([(posicao,velocidade)],[nextPos],False)))
                        porVisitar.append((nextPos,nextVel))
                    else:
                        grafo[(posicao,velocidade)].add(((nextPos,nextVel),25*self.calcBestHeuristica([(posicao,velocidade)],[nextPos],False)))
                first = False
        return grafo

    #calcula a melhor heuristica em relação aos possiveis fins. Escolhe o melhor final para se ter
    # argumento isAEstrela permite utilizar esta função para ambos as pesquisas caso ser falsa ela não calcula o path
    # recebe o path = lista de (nodo, velocidade) e uma lista de fins possiveis = nodos
    def calcBestHeuristica(self,path,end,isAEstrela = True):
        i = len(path) - 1
        (x1,y1) = ponto = path[i][0]
        i -= 1
        best = math.inf
        for x2,y2 in end:
            tenta = math.sqrt((math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)))
            if(tenta < best):
                best = tenta
        if isAEstrela:
            first = ponto
            while i >= 0:
                for (nodo2,velocidade), peso in self.grafo[path[i]]:
                        if nodo2 == first:
                            best += peso
                first = path[i][0]
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

    #verifica se há uma passagem direta entre o inicio (possição inicial) e fim (pos final)
    def passagemPossivel(self,inicio,fim):
        if inicio == fim:
            return True
        else:
            filhos = []
            for vel in self.ac:
                x,y = inicio[0] + vel[0], inicio[1] + vel[1]
                filhos.append(((x,y),self.calcBestHeuristica([((x,y),(0,0))],[fim],False)))
            best = ((0,0),math.inf)
            for filho, heuristica in filhos:
                if heuristica < best[1]:
                    best = (filho,heuristica)
            if self.estadoPossivel(best[0]):
                return self.passagemPossivel(best[0], fim)
            else:
                return False



    #algoritmo de pesquisa A*
    def AEstrela(self):
        #possiveis = list de (estado: (coordenada,velocidade), heuristica, path tomado)
        possiveis = [((self.start,(0,0)),self.calcBestHeuristica([(self.start,(0,0))],self.end),[(self.start,(0,0))])]
        visitados = [(self.start,(0,0))]
        while len(possiveis) > 0:
            #best = (estado, heuristica em A*,path)
            best = (((0,0),(0,0)),math.inf,[])
            #por todos os nodos possiveis de visitar encontra o com a melhor heuristica
            for estado, heuristica, path in possiveis:
                if heuristica < best[1]:
                    best = (estado,heuristica,path)
            #remove o nodo que vai visitar dos nodos que falta visitar
            possiveis.remove(best)
            #para todos os seus filhos:
            for estado, peso in self.grafo[best[0]]:
                pathUntilNow = best[2].copy()
                #se o filho for um dos nodos finais retorna o caminho
                if estado[0] in self.end:
                    best[2].append(estado)
                    return best[2]
                # se não e não estiver nos visitados adiciona-o ao nodos ainda por visitar
                elif estado not in visitados:
                    pathUntilNow.append(estado)
                    visitados.append(estado)
                    possiveis.append((estado,self.calcBestHeuristica(pathUntilNow,self.end),pathUntilNow))

    def desenha(self):
        ##criar lista de vertices
        lista_v = self.grafo
        g=nx.Graph()
        #Converter para o formato usado pela biblioteca networkx
        for nodo in lista_v.keys():
            n = nodo[0]
            g.add_node(n)
            for (estado , peso) in self.grafo[nodo]:
                g.add_edge(n,estado[0],weight=peso)
        #desenhar o grafo
        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
        plt.draw()
        plt.show()
