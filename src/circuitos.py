import os
import graph
i = 1
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

def logging(visited:set,p, c):
    global i
    path = "logs/logs.txt"
    if not os.path.isfile(path):
        file = open(path, 'x')
    file = open(path,'a')
    file.write("Pedido " + str(i) + ":\n")
    #print(visited)
    #print(p)
    visited.append(str(p))
    #print(visited)
    #print(visited)
    file.write(str(visited) + "\n")
    file.write("Custo: " + str(c)+ "\n")
    file.write('\n')
    i+=1

def loggingmulti(vs, ps, cs):
    global i
    path = "logs/logs.txt"
    if not os.path.isfile(path):
        file = open(path, 'x')
    file = open(path,'a')
    file.write("Pedido " + str(i) + ":\n")
    info = []
    j=1
    for v in vs:
        for p in ps:
            info.append(v+(p,))
            j+=1

    file.write(str(info) + "\n")
    file.write(cs)
    file.write('\n')
    i+=1