import math


class graph:
    def __init__(self,partida,fim,matriz):
        self.start = partida
        self.end = fim
        self.matrix = matriz
        self.ac = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]

    def calcBestHeuristica(self, ponto):
        (x1,y1) = ponto
        best = math.inf
        for x2,y2 in self.end:
            tenta = math.sqrt((math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)))
            if(tenta < best):
                best = tenta
        return best

    def calcNextPos(self,vel,ac,posAtual):
        (pL,pC) = posAtual
        (vL,vC) = vel
        (aL,aC) = ac
        retPL = pL + vL + aL
        retPC = pC + vC + aC
        return (retPL,retPC)

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

    def removePossiveis(self,next,possiveis):
        for (nodo, velAtual, acelAtual, heuristica) in possiveis:
            if next == nodo:
                possiveis.remove((nodo, velAtual, acelAtual, heuristica))
        return possiveis

   # def posiçãoPossivel(self,ponto):

    def AEstrela(self):
        #possiveis = [(posição,velocidade,aceleração,heuristica)]
        possiveis = [(self.start,(0,0),(0,0),self.calcBestHeuristica(self.start))]
        path = []
        #best = (posição,velocidade,aceleração,heuristica)
        best = (self.start,(0,0),(0,0),self.calcBestHeuristica(self.start))
        vel = (0,0)
        dontEnd = True
        while dontEnd:
            path.append(best[0])
            if best[0] == self.end:
                dontEnd = False
                break
            for (nodo,velAtual,acelAtual,heuristica) in possiveis:
                if heuristica < best[3]:
                   best = (nodo,velAtual,acelAtual,heuristica)
            possiveis = self.removePossiveis(best[0],possiveis)
            for acel in self.ac:
                nextVel = self.calcVel(best[1],acel)
                ponto = self.calcNextPos(best[1],acel,best[0])
                possiveis.append((ponto,nextVel,self.calcAcel(best[2],acel),self.calcBestHeuristica(ponto)))



