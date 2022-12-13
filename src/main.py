#Inteligência Artificial
#2022/23
import pygame
import sys
import inputbox

#Importar classe graph
from graph import graph
import time
import funcaux
import circuitos

def main():

    pygame.init()
    infores =pygame.display.Info()
    pygame.mixer.music.load("./music/bandolero.mp3")
    pygame.mixer.music.play()
    mw= (infores.current_w / 1920)
    mh = (infores.current_h /1080)
    width = 1920* mw
    height = 1080* mh
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

    #Tentar fazer com 70
    smallfont = pygame.font.SysFont('Arial',int(40*mw*mh))
    #Tentar fazer com 50
    smallerfont = pygame.font.SysFont('Arial',int(25*mw*mh)) 
    #Tentar fazer com 120
    bigfont= pygame.font.SysFont('Arial',int(80*mw*mh)) 
    quit = smallfont.render('Sair' , True , white)
    select= smallfont.render('Por favor selecione o circuito que deseja utilizar', True, white)
    circuito1 = smallfont.render('Circuito 1', True, white)
    enunciado = smallerfont.render('   (enunciado)', True, white )
    circuito2 = smallfont.render('Circuito 2', True, white)
    circuito3 = smallfont.render('Circuito 3', True, white)
    circuito4 = smallfont.render('Circuito 4', True, white)
    circuitoopcional = smallfont.render('Adicionar circuito', True, white)
    inputbox1= inputbox.InputBox(580*mw,height-145*mh,300,45, "maps/circuito1.txt")
    defaultinput = "maps/circuito1.txt"
    vectorace = bigfont.render('VECTOR RACE', True, red)
    DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    pygame.display.set_caption('VECTOR RACE')
    flag = True
    while flag:
        for ev in pygame.event.get(): 

            if ev.type == pygame.QUIT: 
                pygame.quit() 

            #checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                #InputBox Adicionar circuito
                if 580*mw <= mouse[0] <= 880*mw and height-145*mh <= mouse[1] <= height-100*mh: 
                    inputbox1.handle_event(ev)
                else:
                    inputbox1.deactivate()
                #if the mouse is clicked on the 
                # button the game is terminated 
                if  width-240*mw <= mouse[0] <= width-100*mw and height-140*mh <= mouse[1] <= height-100*mh: 
                    flag = False
                    screen=pygame.quit()
                    break
                
                #Adicionar circuito
                if 218*mw <= mouse[0] <= 578*mw and height-140*mh <= mouse[1] <= height-100*mh: 
                    g, y, b,partida,fim = circuitos.loadcircuit(defaultinput)
                    screen.fill(dark_theme)
                    pygame.display.update()
                    funcaux.interagircircuito(screen, g, y , b,partida,fim)
                    break
                    
                #Circuito 1
                if 210*mw <= mouse[0] <= 420 *mw and height/2-20*mh <= mouse[1] <= height/2+95*mh: 
                    g, y, b,partida,fim = circuitos.loadcircuit("maps/circuito1.txt")
                    screen.fill(dark_theme)
                    pygame.display.update()
                    funcaux.interagircircuito(screen, g, y , b,partida,fim)
                    break
                
                #Circuito 2
                if 610*mw <= mouse[0] <= 820*mw and height/2-20*mh <= mouse[1] <= height/2+60*mh: 
                    g, y, b,partida,fim = circuitos.loadcircuit("maps/circuito2.txt")
                    screen.fill(dark_theme)
                    pygame.display.update()
                    funcaux.interagircircuito(screen, g, y , b,partida,fim)
                    break

                #Circuito 3
                if 1010*mw <= mouse[0] <= 1220*mw and height/2-20*mh<= mouse[1] <= height/2+60*mh: 
                    g, y, b,partida,fim = circuitos.loadcircuit("maps/circuito3.txt")
                    screen.fill(dark_theme)
                    pygame.display.update()
                    funcaux.interagircircuito(screen, g, y , b,partida,fim)
                    break

                #Circuito 4
                if 1410*mw <= mouse[0] <= 1620*mw and height/2-20*mh <= mouse[1] <= height/2+60*mh: 
                    g, y, b,partida,fim = circuitos.loadcircuit("maps/circuito4.txt")
                    screen.fill(dark_theme)
                    pygame.display.update()
                    funcaux.interagircircuito(screen, g, y , b,partida,fim)
                    break
            if ev.type ==pygame.KEYDOWN:
                if inputbox1.active:
                    inputbox1.handle_event(ev)
                    inputbox1.update()

                defaultinput=inputbox1.text
                if ev.key == pygame.K_RETURN:
                    inputbox1.deactivate()

                    g, y, b,partida,fim = circuitos.loadcircuit(defaultinput)
                    screen.fill(dark_theme)
                    pygame.display.update()
                    funcaux.interagircircuito(screen, g, y , b,partida,fim)
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


            #Circuito opcional light shade
            if 215*mw <= mouse[0] <= 580*mw and height-140*mh <= mouse[1] <= height-100*mh: 
                pygame.draw.rect(screen,color_light,[215*mw,height-145*mh,330*mw,48*mh])
            #Circuito opcional darker shade
            else:
                pygame.draw.rect(screen,color_dark,[218*mw,height-145*mh,328*mw,48*mh]) 


            #Circuito1 light shade
            if 210*mw <= mouse[0] <= 420*mw and height/2-20*mh <= mouse[1] <= height/2+95*mh: 
                pygame.draw.rect(screen,color_light,[210*mw,height/2 - 20*mh ,210*mw,115*mh]) 
            #Circuito1 darker shade    
            else: 
                pygame.draw.rect(screen,color_dark,[210*mw,height/2 - 20*mh ,210*mw,115*mh]) 

            #Circuito2 light shade
            if 610*mw <= mouse[0] <= 820*mw and height/2-20*mh <= mouse[1] <= height/2+60*mh: 
                pygame.draw.rect(screen,color_light,[610*mw,height/2 - 20*mh ,210*mw,80*mh]) 
            #Circuito2 darker shade    
            else: 
                pygame.draw.rect(screen,color_dark,[610*mw,height/2 - 20*mh ,210*mw,80*mh]) 


            #Circuito3 light shade
            if 1010*mw <= mouse[0] <= 1220*mw and height/2-20*mh <= mouse[1] <= height/2+60*mh: 
                pygame.draw.rect(screen,color_light,[1010*mw,height/2 - 20*mh ,210*mw,80*mh]) 
            #Circuito3 darker shade    
            else: 
                pygame.draw.rect(screen,color_dark,[1010*mw,height/2 - 20*mh ,210*mw,80*mh]) 


            #Circuito4 light shade
            if 1410*mw <= mouse[0] <= 1620*mw and height/2-20*mh <= mouse[1] <= height/2+60*mh: 
                pygame.draw.rect(screen,color_light,[1410*mw,height/2 - 20*mh,210*mw,80*mh]) 
            #Circuito4 darker shade    
            else: 
                pygame.draw.rect(screen,color_dark,[1410*mw,height/2 - 20*mh ,210*mw,80*mh]) 


            # superimposing the text onto our button 
            screen.blit(vectorace,(width/2-250*mw, 50*mh))
            screen.blit(select, (width/2-380*mw,height/2 - 240*mh))
            screen.blit(quit , (width-230*mw,height-140*mh))

            screen.blit(circuitoopcional,(230*mw,height-140*mh))
            inputbox1.draw(screen)

            screen.blit(circuito1 , (230*mw,height/2))
            screen.blit(enunciado , (230*mw,height/2+50*mh))

            screen.blit(circuito2 , (630*mw,height/2))
            screen.blit(circuito3 , (1030*mw,height/2))
            screen.blit(circuito4 , (1430*mw,height/2))

            # updates the frames of the game 
            pygame.display.update() 


if __name__ == "__main__":
    main()
