#Inteligência Artificial
#2022/23
import pygame

#Importar classe graph
from graph import graph
import time

def main():
    file = open("circuito3.txt")
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
    print("fim: ",fim,"\n")
    print("partida:",partida,"\n")
    #cosntrução de menu
    saida = -1
    while saida != 0:
        print("1-Imprimir Grafo do circuito")
        print("2-Desenhar circuito em VectorRace")
        print("3-Resolver o problema utilizando um algoritmo")
        print("0-Saír")

        saida = int(input("introduza a sua opcao-> "))
        if saida == 0:
            print("saindo.......")
        elif saida == 1:
            #Escrever o grafo como string
            print(g)
            time.sleep(1)
            g.desenha()
            l=input("prima enter para continuar")
        elif saida == 2:
            #Desenhar o grafo de forma gráfica
            janela = pygame.display.set_mode((30*len(b), 30 * len(b[0])))
           # g.plot(janela,path)
            l=input("prima enter para continuar")
            pygame.quit()
        elif saida == 3:
            #Imprimir as chaves do dicionario que representa o grafo
            print("Resposta do Algoritmo AEstrela: " + str(g.AEstrela()))
            l = input("prima enter para continuar")
        else:
            print("Opção inválida...")
            l = input("prima enter para continuar")



if __name__ == "__main__":
    main()
