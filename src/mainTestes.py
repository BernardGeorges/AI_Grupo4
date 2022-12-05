
from algoritmos import algoritmos
from graph import graph
import time
def main():
    circuito = "./maps/circuito3.txt"
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
                    partida.append((x, y))
                if char == 'F':
                    fim.append((x, y))
                x += 1
        y += 1

    g = graph(partida[0],b)
    algs = algoritmos(g,partida[0],fim)
    print("passagem é: ", g.passagemPossivel((2,3),(1,3),True))
    print(b)
    print("passagem é: ", algs.DFS())

if __name__ == "__main__":
    main()