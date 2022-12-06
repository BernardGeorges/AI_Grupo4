import graph
def loadcircuit(circuito):
    file = open(circuito)
    y = 0
    b = []
    partida = []
    fim = []
    for line in file:
        x = 0
        b.append([])
        for char in line:
            if char != ' ' and char != '\n':
                b[y].append(char)
                if char == 'P':
                    partida.append((x,y))
                if char == 'F':
                    fim.append((x,y))
                x += 1
        y += 1
    g = graph.graph(partida[0],b,fim)
    return g, b, y,partida,fim
