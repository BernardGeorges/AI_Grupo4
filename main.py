from graph import graph

# Press Shift+F10 to execute it or replace it with your code.

file = open("circuito2.txt")
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

g = graph(partida,fim,b)
print(b)
print(fim)
print(partida)
print(g.criaGrafo(partida,(0,0),(0,0))) 