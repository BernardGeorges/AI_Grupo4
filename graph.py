import math


class graph:
    def __init__(self,partida,fim,matriz):
        self.start = partida
        self.end = fim
        self.matrix = matriz
        self.ac = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]

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
        for (nodo, velAtual, acelAtual, heuristica) in possiveis:
            if next == nodo:
                possiveis.remove((nodo, velAtual, acelAtual, heuristica))
        return possiveis

   # pls fazerem dada a posição(ponto) verifica se este é uma prosição valida para um futuro movimento (ou seja devolve false se for parede)
   # def posiçãoPossivel(self,ponto):

    def AEstrela(self):
        #possiveis = [(posição,velocidade,aceleração,heuristica)]
        possiveis = [(self.start,(0,0),(0,0),self.calcBestHeuristica(self.start))]
        # caminho que o bot deve seguir
        path = []
        #ainda nao implementei mas devia XD (visitados = [])
        #best = (posição,velocidade,aceleração,heuristica)
        best = (self.start,(0,0),(0,0),self.calcBestHeuristica(self.start))
        vel = (0,0)
        #var pra indicar se já encontrei o fim ou não. Enquanto nao encontrar se mantem True
        dontEnd = True
        while dontEnd:
            path.append(best[0])
            if best[0] == self.end:
                dontEnd = False
                break
            #percore todos os nodos possiveis de forma a encontrar aquele com a melhor heuristica (armazenado no best)
            for (nodo,velAtual,acelAtual,heuristica) in possiveis:
                if heuristica < best[3]:
                   best = (nodo,velAtual,acelAtual,heuristica)
            possiveis = self.removePossiveis(best[0],possiveis)
            #percorre todos as possiveis jogadas com as varias velocidades.
            for acel in self.ac:
                nextVel = self.calcVel(best[1],acel)
                ponto = self.calcNextPos(best[1],acel,best[0])
                possiveis.append((ponto,nextVel,self.calcAcel(best[2],acel),self.calcBestHeuristica(ponto)))



