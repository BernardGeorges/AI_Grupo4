import pygame
import sys
from algoritmos import algoritmos
import inputbox
import graph
import circuitos

infores =pygame.display.Info()
mw= (infores.current_w / 1920)
mh = (infores.current_h /1080)
width = 1920* mw
height = 1080* mh
screen = pygame.display.set_mode((width, height))
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
                if  width-240*mw <= mouse[0] <= width-100*mw and height-140*mh <= mouse[1] <= height-100*mh: 
                    flag = False
                    screen=pygame.quit()
                    break
                #Voltar
                if 218*mw <= mouse[0] <= 578*mw and height-140*mh <= mouse[1] <= height-100*mh: 
                    flag=False
                    break

                #A-Estrela
                if 210*mw <= mouse[0] <= 420*mw and height/2 +250*mh <= mouse[1] <= height/2+330*mh: 
                    screen.fill(dark_theme)
                    pygame.display.update()
                    interagealg(screen,1,g,y,b,partida,fim)
                    flag = False
                    break

                    
                #Greedy
                if 610*mw <= mouse[0] <= 820*mw and height/2 +250*mh <= mouse[1] <= height/2+330*mh: 
                    screen.fill(dark_theme)
                    pygame.display.update()
                    interagealg(screen,2,g,y,b,partida,fim)
                    flag = False
                    break


                #BFS
                if 1010*mw <= mouse[0] <= 1220*mw and height/2 +250*mh <= mouse[1] <= height/2+330*mh: 
                    screen.fill(dark_theme)
                    pygame.display.update()
                    interagealg(screen,3,g,y,b,partida,fim)
                    flag = False
                    break


                #DFS
                if 1410*mw <= mouse[0] <= 1620*mw and height/2 +250*mh <= mouse[1] <= height/2+330*mh: 
                    screen.fill(dark_theme)
                    pygame.display.update()
                    interagealg(screen,4,g,y,b,partida,fim)
                    flag = False
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
            if width-240*mw <= mouse[0] <= width-95*mw and height-145*mh <= mouse[1] <= height-97*mh: 
                pygame.draw.rect(screen,color_light,[width-240*mw,height-145*mh,95*mw,48*mw])
            #Sair darker shade
            else:
                pygame.draw.rect(screen,color_dark,[width-240*mw,height-145*mh,95*mw,48*mh]) 

            #Voltar light shade
            if 218*mw <= mouse[0] <= 346*mw and height-140*mh <= mouse[1] <= height-100*mh:
                pygame.draw.rect(screen,color_light,[218*mw,height-145*mh,128*mw,48*mh])
            #Voltar darker shade
            else:
                pygame.draw.rect(screen,color_dark,[218*mw,height-145*mh,128*mw,48*mh]) 



            #aestrela light shade
            if 210*mw <= mouse[0] <= 420*mw and height/2 +250*mh <= mouse[1] <= height/2+330*mh: 
                pygame.draw.rect(screen,color_light,[210*mw,height/2 +250*mh ,210*mw,80*mh])

            #aestrela darker shade    
            else: 
                pygame.draw.rect(screen,color_dark,[210*mw,height/2 +250*mh ,210*mw,80*mh]) 

            #greedy light shade
            if 610*mw <= mouse[0] <= 820*mw and height/2 +250*mh <= mouse[1] <= height/2+330*mh: 
                pygame.draw.rect(screen,color_light,[610*mw,height/2 +250*mh ,210*mw,80*mh]) 
            #greedy darker shade    
            else: 
                pygame.draw.rect(screen,color_dark,[610*mw,height/2 +250*mh ,210*mw,80*mh]) 


            #bfs light shade
            if 1010*mw <= mouse[0] <= 1140*mh and height/2 +250*mw <= mouse[1] <= height/2+330*mh: 
                pygame.draw.rect(screen,color_light,[1010*mw,height/2 +250*mh ,130*mw,80*mh]) 
            #bfs darker shade    
            else: 
                pygame.draw.rect(screen,color_dark,[1010*mw,height/2 +250*mh ,130*mw,80*mh]) 


            #dfs light shade
            if 1410*mw <= mouse[0] <= 1540*mw and height/2+250*mh <= mouse[1] <= height/2+330*mh: 
                pygame.draw.rect(screen,color_light,[1410*mw,height/2 +250*mh ,130*mw,80*mh]) 
            #dfs darker shade    
            else: 
                pygame.draw.rect(screen,color_dark,[1410*mw,height/2 +250*mh ,130*mw,80*mh]) 


            # superimposing the text onto our button 
            screen.blit(vectorace,(width/2-250*mw, 50*mh))
            screen.blit(select, (width/2-380*mw,height/2 - 400*mh))
            screen.blit(quit , (width-230*mw,height-140*mh))
            screen.blit(voltar,(230*mw,height-140*mh))

            screen.blit(aestrela , (230*mw,height/2 +270*mh))
            screen.blit(greedy , (630*mw,height/2 +270*mh))
            screen.blit(bfs , (1030*mw,height/2 +270*mh))
            screen.blit(dfs , (1430*mw,height/2 +270*mh))

            screen.blit(circuito, (width/2-280*mw,height/2-250*mh))




            # updates the frames of the game 
            pygame.display.update() 

def interagealg(screen,alg,g:graph.graph, y, b, partida,fim):
    algs = algoritmos(g,partida[0],fim)
    circuito = pygame.Surface((600*mw,400*mh))
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

    g.plotpath(circuito,path,600*mw,400*mh)
    flag=True
    while flag:
        for ev in pygame.event.get(): 
            
            if ev.type == pygame.QUIT: 
                pygame.quit()
            
            #checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN: 

                #if the mouse is clicked on the 
                # button the game is terminated 
                if  width-240*mw <= mouse[0] <= width-100*mw and height-140*mh <= mouse[1] <= height-100*mh: 
                    flag=False
                    pygame.quit()
                    break

                #Mostrar Grafo
                if 350*mw <= mouse[0] <= 560*mw and height/2 +250*mh <= mouse[1] <= height/2+330*mh: 
                    g.desenha()
                    pygame.display.update()
                    

                #Usar outro algoritmo
                if 1310*mw <= mouse[0] <= 1760*mw and height/2+250*mh <= mouse[1] <= height/2+330*mh: 
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
            if width-240*mw <= mouse[0] <= width-95*mw and height-145*mh <= mouse[1] <= height-97*mh: 
                pygame.draw.rect(screen,color_light,[width-240*mw,height-145*mh,95*mw,48*mh])
            #Sair darker shade
            else:
                pygame.draw.rect(screen,color_dark,[width-240*mw,height-145*mh,95*mw,48*mh]) 


            #grafo light shade
            if 350*mw <= mouse[0] <= 560*mw and height/2 +250*mh <= mouse[1] <= height/2+330*mh: 
                pygame.draw.rect(screen,color_light,[210*mw,height/2 +250*mh ,350*mw,80*mh])
                
            #grafo darker shade    
            else: 
                pygame.draw.rect(screen,color_dark,[210*mw,height/2 +250*mh ,350*mw,80*mh]) 


            #algoritmo light shade
            if 1310*mw <= mouse[0] <= 1760*mw and height/2+250*mh <= mouse[1] <= height/2+330*mh: 
                pygame.draw.rect(screen,color_light,[1310*mw,height/2 +250*mh ,450*mw,80*mh]) 
            #algoritmo darker shade    
            else: 
                pygame.draw.rect(screen,color_dark,[1310*mw,height/2 +250*mh ,450*mw,80*mh]) 


            # superimposing the text onto our button 
            screen.blit(vectorace,(width/2-250*mw, 50*mh))
            screen.blit(quit , (width-230*mw,height-140*mh))

            screen.blit(grafo , (230*mw,height/2 +270*mh))
            screen.blit(algoritmo , (1330*mw,height/2 +270*mh))

            screen.blit(circuito, (width/2-280*mw,height/2-250*mh))




            # updates the frames of the game 
            pygame.display.update() 