import pygame
import sys
from algoritmos import algoritmos
import inputbox
import graph
import circuitos

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
select= smallfont.render('Por favor selecione o algoritmo que deseja utilizar', True, white)
aestrela = smallfont.render('A-Estrela', True, white)
greedy = smallfont.render('Greedy', True, white)
bfs = smallfont.render('BFS', True, white)
dfs = smallfont.render('DFS', True, white)
algoritmo= smallfont.render('Escolher outro algoritmo', True, white)
grafo = smallfont.render('Desenhar o Grafo', True, white)
voltar = smallfont.render('Voltar', True, white)
vectorace = bigfont.render('VECTOR RACE', True, red)
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption('VECTOR RACE')
def interagircircuito(screen,g:graph , y, b,partida,fim):
    #screen = pygame.display.get_surface()
    #janela = pygame.display.set_mode((40*30, 15 * 30))
    #circuito = pygame.display.set_mode((40*len(b), 15 * len(b[0])))
    #circuito = pygame.Surface((width/2-280,height/2 - 400))
    circuito = pygame.Surface((600,400))


    g.plot(circuito,600,400)
    flag=True
    while flag:
        for ev in pygame.event.get(): 
            
            if ev.type == pygame.QUIT: 
                pygame.quit() 
            
            #checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN: 

                #if the mouse is clicked on the 
                # button the game is terminated 
                if  width-240 <= mouse[0] <= width-100 and height-140 <= mouse[1] <= height-100: 
                    flag = False
                    screen=pygame.quit()
                    break
                if 218 <= mouse[0] <= 578 and height-140 <= mouse[1] <= height-100: 
                    flag=False
                    break

                #A-Estrela
                if 210 <= mouse[0] <= 420 and height/2 +250 <= mouse[1] <= height/2+330: 
                    screen.fill(dark_theme)
                    pygame.display.update()
                    interagealg(screen,1,g,y,b,partida,fim)

                    
                #Greedy
                if 610 <= mouse[0] <= 820 and height/2 +250 <= mouse[1] <= height/2+330: 
                    screen.fill(dark_theme)
                    pygame.display.update()
                    interagealg(screen,2,g,y,b,partida,fim)


                #BFS
                if 1010 <= mouse[0] <= 1220 and height/2 +250 <= mouse[1] <= height/2+330: 
                    screen.fill(dark_theme)
                    pygame.display.update()
                    interagealg(screen,3,g,y,b,partida,fim)


                #DFS
                if 1410 <= mouse[0] <= 1620 and height/2 +250 <= mouse[1] <= height/2+330: 
                    screen.fill(dark_theme)
                    pygame.display.update()
                    interagealg(screen,4,g,y,b,partida,fim)


                
        if flag:                
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

            #Voltar light shade
            if 218 <= mouse[0] <= 346 and height-140 <= mouse[1] <= height-100:
                pygame.draw.rect(screen,color_light,[218,height-145,128,48])
            #Voltar darker shade
            else:
                pygame.draw.rect(screen,color_dark,[218,height-145,128,48]) 



            #aestrela light shade
            if 210 <= mouse[0] <= 420 and height/2 +250 <= mouse[1] <= height/2+330: 
                pygame.draw.rect(screen,color_light,[210,height/2 +250 ,210,80])

            #aestrela darker shade    
            else: 
                pygame.draw.rect(screen,color_dark,[210,height/2 +250 ,210,80]) 

            #greedy light shade
            if 610 <= mouse[0] <= 820 and height/2 +250 <= mouse[1] <= height/2+330: 
                pygame.draw.rect(screen,color_light,[610,height/2 +250 ,210,80]) 
            #greedy darker shade    
            else: 
                pygame.draw.rect(screen,color_dark,[610,height/2 +250 ,210,80]) 


            #bfs light shade
            if 1010 <= mouse[0] <= 1140 and height/2 +250 <= mouse[1] <= height/2+330: 
                pygame.draw.rect(screen,color_light,[1010,height/2 +250 ,130,80]) 
            #bfs darker shade    
            else: 
                pygame.draw.rect(screen,color_dark,[1010,height/2 +250 ,130,80]) 


            #dfs light shade
            if 1410 <= mouse[0] <= 1540 and height/2+250 <= mouse[1] <= height/2+330: 
                pygame.draw.rect(screen,color_light,[1410,height/2 +250 ,130,80]) 
            #dfs darker shade    
            else: 
                pygame.draw.rect(screen,color_dark,[1410,height/2 +250 ,130,80]) 


            # superimposing the text onto our button 
            screen.blit(vectorace,(width/2-250, 50))
            screen.blit(select, (width/2-380,height/2 - 400))
            screen.blit(quit , (width-230,height-140))
            screen.blit(voltar,(230,height-140))

            screen.blit(aestrela , (230,height/2 +270))
            screen.blit(greedy , (630,height/2 +270))
            screen.blit(bfs , (1030,height/2 +270))
            screen.blit(dfs , (1430,height/2 +270))

            screen.blit(circuito, (width/2-280,height/2-250))




            # updates the frames of the game 
            pygame.display.update() 

def interagealg(screen,alg,g:graph.graph, y, b, partida,fim):
    algs = algoritmos(g,partida[0],fim)
    circuito = pygame.Surface((600,400))
    match alg:
        case 1:
            path = algs.AEstrela()
        case 2:
            path = algs.Greedy()
        case 3:
            path = algs.BFS()
        case 4:
            path = algs.DFS()
        case _:
            print("ERRO")

    g.plotpath(circuito,path,600,400)
    flag=True
    while flag:
        for ev in pygame.event.get(): 
            
            if ev.type == pygame.QUIT: 
                screen=pygame.quit()
            
            #checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN: 

                #if the mouse is clicked on the 
                # button the game is terminated 
                if  width-240 <= mouse[0] <= width-100 and height-140 <= mouse[1] <= height-100: 
                    flag = False
                    pygame.quit()
                    flag=False
                    break
                if 218 <= mouse[0] <= 578 and height-140 <= mouse[1] <= height-100: 
                    circuitoop = inputbox.screen()

                #Mostrar Grafo
                if 350 <= mouse[0] <= 560 and height/2 +250 <= mouse[1] <= height/2+330: 
                    g.desenha()
                    pygame.display.update()

                #Usar outro algoritmo
                if 1310 <= mouse[0] <= 1760 and height/2+250 <= mouse[1] <= height/2+330: 
                    screen.fill(dark_theme)
                    pygame.display.update()
                    flag=False
                    interagircircuito(screen, g, y , b,partida,fim)
                    break


                
        if flag:                
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


            #grafo light shade
            if 350 <= mouse[0] <= 560 and height/2 +250 <= mouse[1] <= height/2+330: 
                pygame.draw.rect(screen,color_light,[210,height/2 +250 ,350,80])
                
            #grafo darker shade    
            else: 
                pygame.draw.rect(screen,color_dark,[210,height/2 +250 ,350,80]) 


            #algoritmo light shade
            if 1310 <= mouse[0] <= 1760 and height/2+250 <= mouse[1] <= height/2+330: 
                pygame.draw.rect(screen,color_light,[1310,height/2 +250 ,450,80]) 
            #algoritmo darker shade    
            else: 
                pygame.draw.rect(screen,color_dark,[1310,height/2 +250 ,450,80]) 


            # superimposing the text onto our button 
            screen.blit(vectorace,(width/2-250, 50))
            screen.blit(quit , (width-230,height-140))

            screen.blit(grafo , (230,height/2 +270))
            screen.blit(algoritmo , (1330,height/2 +270))

            screen.blit(circuito, (width/2-280,height/2-250))




            # updates the frames of the game 
            pygame.display.update() 