#Inteligência Artificial
#2022/23
import pygame
import sys
import inputbox

#Importar classe graph
from graph import graph
import time
import aux
from screeninfo import get_monitors
import circuitos

def main():
    pygame.init()
    #m = get_monitors()
    #print(str(m))
    #for m in get_monitors:
    #    s = str(m).split()
    #    if s[7]==True:
    #        width=s[2]
    #        heigth=s[3]
    width = 1920
    height = 1080
    res=(width,height)
    # opens up a window 
    screen = pygame.display.set_mode(res) 
    # white color 
    white = (255,255,255) 
    
    # light shade of the button 
    color_light = (170,170,170) 
    
    # dark shade of the button 
    color_dark = (100,100,100) 
    
    red = (255,0,0)

    #dark theme colors
    blue = (0,122,204)
    dark_theme = (62,62,66)
    darker_theme = (45,45,48)
    darkerer_theme = (37,37,38)
    darkest_theme = (30,30,30)

    smallfont = pygame.font.SysFont('Arial',40) 
    smallerfont = pygame.font.SysFont('Arial',25) 
    bigfont= pygame.font.SysFont('Arial',80) 
    quit = smallfont.render('Sair' , True , white)
    select= smallfont.render('Por favor selecione o circuito que deseja utilizar', True, white)
    circuito1 = smallfont.render('Circuito 1', True, white)
    enunciado = smallerfont.render('   (enunciado)', True, white )
    circuito2 = smallfont.render('Circuito 2', True, white)
    circuito3 = smallfont.render('Circuito 3', True, white)
    circuito4 = smallfont.render('Circuito 4', True, white)
    circuitoopcional = smallfont.render('Adicionar circuito', True, white)
    vectorace = bigfont.render('VECTOR RACE', True, red)
    DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    pygame.display.set_caption('VECTOR RACE')
    while True:
        for ev in pygame.event.get(): 
            
            if ev.type == pygame.QUIT: 
                pygame.quit() 
            
            #checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN: 

                #if the mouse is clicked on the 
                # button the game is terminated 
                if  width-240 <= mouse[0] <= width-100 and height-140 <= mouse[1] <= height-100: 
                    pygame.quit()
                if 218 <= mouse[0] <= 578 and height-140 <= mouse[1] <= height-100: 
                    circuitoop = inputbox.screen()
                if 210 <= mouse[0] <= 420 and height/2-20 <= mouse[1] <= height/2+95: 
                    g,path, y, b = circuitos.loadcircuit("circuito1.txt")
                    screen.fill(dark_theme)
                    screen= pygame.display.update()
                    aux.interagircircuito(screen, g, path, y , b)
                    
                if 610 <= mouse[0] <= 820 and height/2-20 <= mouse[1] <= height/2+60: 
                    g,path = circuitos.loadcircuit("circuito2.txt")
                    screen.fill(dark_theme)
                if 1010 <= mouse[0] <= 1220 and height/2-20 <= mouse[1] <= height/2+60: 
                    g,path = circuitos.loadcircuit("circuito3.txt")
                    screen.fill(dark_theme)
                if 1410 <= mouse[0] <= 1620 and height/2-20 <= mouse[1] <= height/2+60: 
                    g,path = circuitos.loadcircuit("circuito1.txt")
                    screen.fill(dark_theme)

                

                
        # fills the screen with a color 
        screen.fill(dark_theme) 

        # stores the (x,y) coordinates into 
        # the variable as a tuple 
        mouse = pygame.mouse.get_pos() 

        # if mouse is hovered on a button it 
        # changes to lighter shade 

        #Sair light shade
        if width-240 <= mouse[0] <= width-95 and height-145 <= mouse[1] <= height-97: 
            pygame.draw.rect(screen,color_light,[width-240,height-145,95,48])
        #Sair darker shade
        else:
            pygame.draw.rect(screen,color_dark,[width-240,height-145,95,48]) 


        #Circuito opcional light shade
        if 218 <= mouse[0] <= 578 and height-140 <= mouse[1] <= height-100: 
            pygame.draw.rect(screen,color_light,[218,height-145,328,48])
        #Circuito opcional darker shade
        else:
            pygame.draw.rect(screen,color_dark,[218,height-145,328,48]) 


        #Circuito1 light shade
        if 210 <= mouse[0] <= 420 and height/2-20 <= mouse[1] <= height/2+95: 
            pygame.draw.rect(screen,color_light,[210,height/2 - 20 ,210,115]) 
        #Circuito1 darker shade    
        else: 
            pygame.draw.rect(screen,color_dark,[210,height/2 - 20 ,210,115]) 

        #Circuito2 light shade
        if 610 <= mouse[0] <= 820 and height/2-20 <= mouse[1] <= height/2+60: 
            pygame.draw.rect(screen,color_light,[610,height/2 - 20 ,210,80]) 
        #Circuito2 darker shade    
        else: 
            pygame.draw.rect(screen,color_dark,[610,height/2 - 20 ,210,80]) 


        #Circuito3 light shade
        if 1010 <= mouse[0] <= 1220 and height/2-20 <= mouse[1] <= height/2+60: 
            pygame.draw.rect(screen,color_light,[1010,height/2 - 20 ,210,80]) 
        #Circuito3 darker shade    
        else: 
            pygame.draw.rect(screen,color_dark,[1010,height/2 - 20 ,210,80]) 


        #Circuito4 light shade
        if 1410 <= mouse[0] <= 1620 and height/2-20 <= mouse[1] <= height/2+60: 
            pygame.draw.rect(screen,color_light,[1410,height/2 - 20 ,210,80]) 
        #Circuito4 darker shade    
        else: 
            pygame.draw.rect(screen,color_dark,[1410,height/2 - 20 ,210,80]) 


        # superimposing the text onto our button 
        screen.blit(vectorace,(width/2-250, 50))
        screen.blit(select, (width/2-380,height/2 - 240))
        screen.blit(quit , (width-230,height-140))
        screen.blit(circuitoopcional,(230,height-140))

        screen.blit(circuito1 , (230,height/2))
        screen.blit(enunciado , (230,height/2+50))

        screen.blit(circuito2 , (630,height/2))
        screen.blit(circuito3 , (1030,height/2))
        screen.blit(circuito4 , (1430,height/2))


        

        # updates the frames of the game 
        pygame.display.update() 
        
    circuito = None
    file = None
    print("Escolha o circuito que pretende usar:\n")
    cont = -1
    while file == None:
        print("1 - Circuito 1 (Igual ao do enunciado)")
        print("2 - Circuito 2")
        print("3 - Circuito 3")
        print("4 - Circuito 4")
        print("5 - Adicionar circuito\n")

        cont = int(input("Introduza a sua opção -> "))

        if cont == 1:
            circuito = "circuito1.txt"
        elif cont == 2:
            circuito = "circuito2.txt"
        elif cont == 3:
            circuito = "circuito4.txt"
        elif cont == 4:
            circuito = "circuitoBasic.txt"
        elif cont == 5:
            print("Por favor introduza o path do circuito")
            circuito = input()
        else:
            print("Opção inválida...")
            l = input("Prima enter para continuar")
        try: 
            file = open(circuito)
        except:
            print("\nFICHEIRO INVÁLIDO")
            print("Por favor introduza corretamente")
            l = input("Prima enter para continuar")

    print(" L O A D I N G . . .")
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
