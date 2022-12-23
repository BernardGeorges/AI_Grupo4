
from algoritmos import algoritmos
from graph import graph
from multiplayer import multiplayer
import time
def main():
    circuito = "./maps/circuitoMultiplayer.txt"
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
    g = graph(partida[0],b,fim)
    algs = algoritmos(g,partida,fim)
    print(g.passagemPossivel((11,2),(16,3),True))
    mp = multiplayer(partida,fim,b)
    paths = mp.run(["A*", "Greedy", "BFS", "DFS"])
    print(b)
    print("passagem é: ", paths)

if __name__ == "__main__":
    main()