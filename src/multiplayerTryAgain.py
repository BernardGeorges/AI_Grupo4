from graph import graph as g

class multiplayer:

    def __init__(self, partida, fim, graph):
        self.start = partida
        self.end = fim
        self.numOfPlayers = len(partida)
        self.estado = []
        self.playerHasEnded = []
        self.graph = graph
        for nodo in partida:
            self.estado.append([(nodo,(0,0)), [(nodo,(0,0))]])
            self.playerHasEnded.append(False)
        print(self.estado)

    def copyEstado(self,estado):
        ret = []
        for nodo, path in estado:
            retPath = []
            for estado in path:
                retPath.append(estado)
            ret.append([nodo,retPath])
        return ret

    def avaliar(self, estado, player):
        placing = []
        for players in range(self.numOfPlayers):
            placing.append((players, self.graph.calcBestHeuristica([estado[players][0]], self.end, False)))
        placing.sort(key=lambda a: a[1])
        #i = 0
        #while placing[i][0] != player and i < self.numOfPlayers:
        #    i += 1
        return placing

    #retorna o estado resultante, o standings do estado final
    def minimax(self,estado, player, profundidade):
        print(profundidade)
        if profundidade == 0 or estado[player][0][0] in self.end:
            standings = self.avaliar(estado, player)
            return (estado, standings)
        else:
            import math
            best = [((-1, -1), (0, 0)),math.inf, math.inf,[]]
            aceleracoes = self.graph.getAC()
            for acel in aceleracoes:
                oldEstado = estado
                nextPos, nextVel = self.graph.calcNextPos(oldEstado[player][0][0],oldEstado[player][0][1],acel), self.graph.calcVel(oldEstado[player][0][1],acel)
               # print("nextPos: ", nextPos, "old estado: ", oldEstado)
               # print(("estado possivel: ",self.graph.estadoPossivel(nextPos)))
               # print("passagem possivel: ", self.graph.passagemPossivel(oldEstado[player][0][0], nextPos, True))
                if self.graph.estadoPossivel(nextPos) and self.graph.passagemPossivel(oldEstado[player][0][0], nextPos, True):
                    estado[player][0] = (nextPos, nextVel)
                    estado[player][1].append((nextPos,nextVel))
                    player = ((player + 1) % self.numOfPlayers)
                    estado, standings = self.minimax(estado, player, (profundidade - 1))
                    i = 1
                    for players, heuristica in standings:
                        if players == player:
                            if best[1] > i or (best[1] == i and heuristica < best[2]):
                                best = ((nextPos,nextVel), i, heuristica,standings)
                                break
                    estado = oldEstado
            return best[0],best[3]

    def turnoPlayer(self, player):
        copyEstado = self.copyEstado(self.estado)
        print("passou aqui")
        movimento, standings = self.minimax(self.estado, player,self.numOfPlayers)
        if movimento in self.end:
            self.playerHasEnded[player] = True
        copyEstado[player][0] = movimento
        copyEstado[player][1].append(movimento)
        self.estado = copyEstado

    def run(self):
        player = 0
        while False in self.playerHasEnded:
                self.turnoPlayer(player)
                player = ((player + 1) % self.numOfPlayers)
        return self.estado
