#Inteligência Artificial
#2022/23
import pygame

#Importar classe graph
from graph import graph
import time

def main():
    circuito = "circuito1.txt"
    print("Escolha o circuito que pretende usar:\n")
    cont = -1
    while cont < 0:
        print("1 - Circuito 1 (Igual ao do enunciado)")
        print("2 - Circuito 2")
        print("3 - Circuito 3\n")

        cont = int(input("Introduza a sua opção -> "))

        if cont == 1:
            circuito = "circuito1.txt"
        elif cont == 2:
            circuito = "circuito2.txt"
        elif cont == 3:
            circuito = "circuito3.txt"
        else:
            print("Opção inválida...")
            l = input("Prima enter para continuar")

    print(" L O A D I N G . . .")
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

    g = graph(partida,fim,b)
    # print(b)
    print("Partida:", partida, "\n")
    print("Fim: ", fim, "\n")
    path = g.AEstrela()
    #cosntrução de menu
    saida = -1
    while saida != 0:
        print("1 - Imprimir Grafo do circuito")
        print("2 - Desenhar circuito em VectorRace")
        print("3 - Resolver o problema utilizando um algoritmo")
        print("0 - Saír")

        saida = int(input("Introduza a sua opção -> "))
        if saida == 0:
            print("Saindo.......")
        elif saida == 1:
            #Escrever o grafo como string
            print(g)
            time.sleep(1)
            g.desenha()
            l=input("Prima enter para continuar")
        elif saida == 2:
            #Desenhar o grafo de forma gráfica
            janela = pygame.display.set_mode((40*len(b), 15 * len(b[0])))
            g.plot(janela,path)
            l=input("Prima enter para continuar")
            pygame.quit()
        elif saida == 3:
            #Imprimir as chaves do dicionario que representa o grafo
            print("Resposta do Algoritmo AEstrela: " + str(g.AEstrela()))
            l = input("Prima enter para continuar")
        else:
            print("Opção inválida...")
            l = input("Prima enter para continuar")



if __name__ == "__main__":
    main()
