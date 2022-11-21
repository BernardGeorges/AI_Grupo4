import math


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

     #funcao que cria e devolve o grafo dos estados possiveis
    def criaGrafo(self,pos, vel, acel):
        porVisitar = [(pos,vel,acel)]
        grafo = {}
        first = True
        while len(porVisitar) > 0:
            posicao, velocidade, aceleracao = porVisitar.pop(0)
            if posicao not in grafo.keys():
                grafo[posicao] = set()
            for newAceleracao in self.ac:
                nextPos,nextVel,nextAcel = self.calcNextPos(posicao,velocidade,aceleracao),self.calcVel(velocidade,aceleracao),self.calcAcel(aceleracao,newAceleracao)
                if (nextPos not in grafo.keys() or first) and self.estadoPossivel(nextPos):
                    grafo[posicao].add(nextPos)
                    porVisitar.append((nextPos,nextVel,nextAcel))
            first = False
        return grafo


    #calcula a melhor heuristica em relação aos possiveis fins. Escolhe o melhor final para se ter
    def calcBestHeuristica(self, ponto):
        (x1,y1) = ponto
        best = math.inf
        for x2,y2 in self.end:
            tenta = math.sqrt((math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)))
            if(tenta < best):
                best = tenta
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

    #calcula a nova Aceleração
    def calcAcel(self,acelAtual, acelAdd):
        (x1,y1) = acelAtual
        (x2,y2) = acelAdd
        return (x1 + x2),(y1 + y2)

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
       #possiveis = [(posição,velocidade,aceleração,heuristica,caminho)]
       possiveis = [(self.start,(0,0),(0,0),math.inf,[])]
       # caminho que o bot deve seguir
       path = []
       #ainda nao implementei mas devia XD (visitados = [])
       #best = (0: posição, 1: velocidade, 2: aceleração, 3: heuristica, 4: caminho)
       best = (self.start,(0,0),(0,0),self.calcBestHeuristica(self.start),[])
       while True:
          if best[0] == self.end:
               break
           #percore todos os nodos possiveis de forma a encontrar aquele com a melhor heuristica (armazenado no best)
          for (nodo,velAtual,acelAtual,heuristica,path) in possiveis:
               best = (nodo,velAtual,acelAtual,heuristica)
               possiveis = self.removePossiveis(best[0],possiveis)
          path = best[4]
          path.append(best[0])
          #percorre todos as possiveis jogadas com as varias velocidades.
          for acel in self.ac:
               nextVel = self.calcVel(best[1],acel)
               ponto = self.calcNextPos(best[1],acel,best[0])
               possiveis.append((ponto,nextVel,self.calcAcel(best[2],acel),self.calcBestHeuristica(ponto)+len(path),path))
       return path

