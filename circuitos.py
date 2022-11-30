import graph
def loadcircuit(circuito, alg=1):
    file = open(circuito)
    y = 0
    b = []
    partida = (0,0)
    fim = []
    for line in file:
        x = 0
        b.append([])
        for char in line:
            if char != ' ' and char != '\n':
                b[y].append(char)
                if char == 'P':
                    partida = (x,y)
                if char == 'F':
                    fim.append((x,y))
                x += 1
        y += 1

    g = graph.graph(partida,fim,b)
    if alg==1:
        path = g.AEstrela()
    else:
        print("algoritmo inválido")

    return g,path , b, y
