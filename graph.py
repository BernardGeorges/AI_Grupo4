import math


class graph:
    def __init__(self,partida,fim,matriz):
        self.start = partida
        self.end = fim
        self.matrix = matriz
        self.ac = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]

     #funcao que cria e devolve o grafo dos estados possiveis
    def criaGrafo(self,pos, velocidade, aceleracao,path = []):
        if self.estadoNaoPossivel(pos) or (pos in path and velocidade != 0):
            return None
        path.append(pos)
        grafo = {}
        grafo[(pos,velocidade,aceleracao)] = set()
        for acel in self.ac:
            newPos,newVel,newAcel = self.calcNextPos(velocidade,aceleracao,pos),self.calcVel(velocidade,aceleracao),self.calcAcel(aceleracao,acel)
            grafoFilhos = self.criaGrafo(newPos,newVel,newAcel,path)
            if grafoFilhos == None:
                grafo[(pos,velocidade,aceleracao)].add(0)
            else:
                grafo[(pos,velocidade,aceleracao)].add(grafoFilhos)
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
    def calcNextPos(self,vel,ac,posAtual):
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

   # pls fazerem dada a posição(ponto) verifica se este é uma prosição valida para um futuro movimento (ou seja devolve false se for parede)
    def estadoNaoPossivel(self,pos):
        return (pos[0] < 0 or pos[1] < 0 or pos == self.end or self.matrix[pos[1]][pos[0]] == '#')
    def AEstrela(self):
       #possiveis = [(posição,velocidade,aceleração,heuristica,caminho)]
       possiveis = [(self.start,(0,0),(0,0),math.inf,[])]
       # caminho que o bot deve seguir
       path = []
       #ainda nao implementei mas devia XD (visitados = [])
       #best = (posição,velocidade,aceleração,heuristica,caminho)
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

#O Rafa teve aqui