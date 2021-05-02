import pygame
import time
import random

#Definiciones globales
pygame.init()

pancho = 1000
papitas = 1000

areajuego = pygame.display.set_mode((pancho,papitas))
pygame.display.set_caption('Invaders Must Die')

black = (0,0,0)
white = (255,255,255)
rojo = (255,0,0)

jancho = 80
jalto = 80

eancho = 200 
ealto = 80

bloquey = 100
bloque2y = 300
bloque3y = 500
bloque4y = 700

bloquex = [100,300,500,700]
bloque2x = [100,300,500,700]
bloque3x = [100,300,500,700]
bloque4x = [100,300,500,700]


LaserImg = pygame.image.load('lasersilotocomequema.png')
e01 = pygame.image.load('hotelcalifornia01.png')
invader1 = pygame.image.load('invader01.png')

florderelos = pygame.time.Clock()

def text_objects(text,font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text,x,y):
    largetext = pygame.font.Font('freesansbold.ttf',40)
    TextSurf, TextRect = text_objects(text, largetext)
    TextRect.center = (x,y)
    areajuego.blit(TextSurf, TextRect)


def game_loop():
    ciclos = 0
    jposx = 460
    jposy = 920

    jmovx = 0

    b1movx = 2
    b2movx = -2

    jtiritox = 100
    jtiritoy = 920

    e1 = True
    e1x = 200
    e1v = 15
    e2 = True
    e2x = 420
    e2v = 15
    e3 = True
    e3x = 640
    e3v = 15

    ey = 820

#PINTAR FONDO
    areajuego.fill(black)
#PINTAR Marco


    termino = False
    eliminado = False

    tirito = False
    tiritoe1 = False
    tiritoe2 = False
    tiritoe3 = False
    tiritoe4 = False
    ciclot1 = 20
    ciclot2 = 70
    ciclot3 = 300
    ciclot4 = 150

    tiritoe1x = 0
    tiritoe1y = 0
    tiritoe2x = 0
    tiritoe2y = 0
    tiritoe3x = 0
    tiritoe3y = 0
    tiritoe4x = 0
    tiritoe4y = 0

    while not termino:
        #pygame.draw.rect(areajuego, black, [jposx, jposy, jancho, jalto])
        areajuego.fill(black)
        for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_0:
                            termino = True
                        if event.key == pygame.K_LEFT:
                            jmovx = -8
                            #print("A la izquierda")
                        elif event.key == pygame.K_RIGHT:
                            jmovx = 8
                            #print("A la derecha")
                        if event.key == pygame.K_SPACE:
                            if not tirito:
                                jtiritox = (jposx+40)
                                jtiritoy = 920
                                tirito = True
        
        #Bloque de Colisiones
        #Que el jugador no salga de la pantalla
        if (jmovx < 0):
            if (jposx + jmovx) > 1:
                jposx = jposx + jmovx
        else:
            if (jposx + jmovx) < 920:
                jposx = jposx + jmovx
        #Que los enemigos no salgan de la pantalla
        if bloquex:
            if (b1movx < 0):
                if (bloquex[0]) < 3:
                    b1movx = 2
            elif (b1movx > 0):
                if (bloquex[-1] + 100) > 997:
                    b1movx = -2
        if bloque2x:
            if (b2movx < 0):
                if (bloque2x[0]) < 3:
                    b2movx = 2
            elif (b2movx > 0):
                if (bloque2x[-1] + 100) > 997:
                    b2movx = -2
        if bloque3x:
            if (b1movx < 0):
                if (bloque3x[0]) < 3:
                    b1movx = 2
            elif (b1movx > 0):
                if (bloque3x[-1] + 100) > 997:
                    b1movx = -2
        if bloque4x:
            if (b2movx < 0):
                if (bloque4x[0]) < 3:
                    b2movx = 2
            elif (b2movx > 0):
                if (bloque4x[-1] + 100) > 997:
                    b2movx = -2

        #Que el tirito no salga de la pantalla o le pegue a un enemigo
        if tirito:
            if jtiritoy < 10:
                tirito = False
            if jtiritoy <= (bloquey+20):
                if jtiritoy >= bloquey:
                    for enemigo in bloquex:
                        if ((jtiritox+10) >= enemigo) and (jtiritox <= (enemigo+100)):
                            bloquex.remove(enemigo)
                            tirito = False
            elif jtiritoy <= (bloque2y+20):
                if jtiritoy >= bloque2y:
                    for enemigo in bloque2x:
                        if ((jtiritox+10) >= enemigo) and (jtiritox <= (enemigo+100)):
                            bloque2x.remove(enemigo)
                            tirito = False
            elif jtiritoy <= (bloque3y+20):
                if jtiritoy >= bloque3y:
                    for enemigo in bloque3x:
                        if ((jtiritox+10) >= enemigo) and (jtiritox <= (enemigo+100)):
                            bloque3x.remove(enemigo)
                            tirito = False
            elif jtiritoy <= (bloque4y+20):
                if jtiritoy >= bloque4y:
                    for enemigo in bloque4x:
                        if ((jtiritox+10) >= enemigo) and (jtiritox <= (enemigo+100)):
                            bloque4x.remove(enemigo)
                            tirito = False
            if e1:
                if (jtiritoy <= (ey+80)) and ((jtiritoy+20) >= ey):
                    if ((jtiritox+10) >= e1x) and (jtiritox <= (e1x+160)):
                        tirito = False
                        if e1v <= 0:
                            e1 = False
                        else:
                            e1v = (e1v - 1)
            if e2:
                if (jtiritoy <= (ey+80)) and ((jtiritoy+20) >= ey):
                    if ((jtiritox+10) >= e2x) and (jtiritox <= (e2x+160)):
                        tirito = False
                        if e2v <= 0:
                            e2 = False
                        else:
                            e2v = (e2v - 1)
            if e3:
                if (jtiritoy <= (ey+80)) and ((jtiritoy+20) >= ey):
                    if ((jtiritox+10) >= e3x) and (jtiritox <= (e3x+160)):
                        tirito = False
                        if e3v <= 0:
                            e3 = False
                        else:
                            e3v = (e3v - 1)

        #Si los tiritos enemigos salieron de la pantalla o nos eliminaron
        if tiritoe1:
            if (tiritoe1y > 989):
                tiritoe1 = False
                ciclot1 = ciclos + (random.randrange(1,200,10))
            if e1:
                if ((tiritoe1y+20) >= ey) and (tiritoe1y < (ey+80)):
                    if (((tiritoe1x+10) >= e1x) and (tiritoe1x <= (e1x+160))):
                        tiritoe1 = False
                        if e1v <= 0:
                            e1 = False
                        else:
                            e1v = (e1v - 1)
            if e2:
                if ((tiritoe1y+20) >= ey) and (tiritoe1y < (ey+80)):
                    if (((tiritoe1x+10) >= e2x) and (tiritoe1x <= (e2x+160))):
                        tiritoe1 = False
                        if e2v <= 0:
                            e2 = False
                        else:
                            e2v = (e2v - 1)
            if e3:
                if ((tiritoe1y+20) >= ey) and (tiritoe1y < (ey+80)):
                    if (((tiritoe1x+10) >= e3x) and (tiritoe1x <= (e3x+160))):
                        tiritoe1 = False
                        if e3v <= 0:
                            e3 = False
                        else:
                            e3v = (e3v - 1)
            if ((tiritoe1y+20) >= jposy) and (tiritoe1y < (jposy+jalto)):
                if (((tiritoe1x+10) >= jposx) and (tiritoe1x <= (jposx+jancho))):
                    tiritoe1 = False
                    termino = True
                    eliminado = True
        if tiritoe2:
            if (tiritoe2y > 989):
                tiritoe2 = False
                ciclot2 = ciclos + (random.randrange(1,200,10))
            if e1:
                if ((tiritoe2y+20) >= ey) and (tiritoe2y < (ey+80)):
                    if (((tiritoe2x+10) >= e1x) and (tiritoe2x <= (e1x+160))):
                        tiritoe2 = False
                        if e1v <= 0:
                            e1 = False
                        else:
                            e1v = (e1v - 1)
            if e2:
                if ((tiritoe2y+20) >= ey) and (tiritoe2y < (ey+80)):
                    if (((tiritoe2x+10) >= e2x) and (tiritoe2x <= (e2x+160))):
                        tiritoe2 = False
                        if e2v <= 0:
                            e2 = False
                        else:
                            e2v = (e2v - 1)
            if e3:
                if ((tiritoe2y+20) >= ey) and (tiritoe2y < (ey+80)):
                    if (((tiritoe2x+10) >= e3x) and (tiritoe2x <= (e3x+160))):
                        tiritoe2 = False
                        if e3v <= 0:
                            e3 = False
                        else:
                            e3v = (e3v - 1)
            if ((tiritoe2y+20) >= jposy) and (tiritoe2y < (jposy+jalto)):
                if (((tiritoe2x+10) >= jposx) and (tiritoe2x <= (jposx+jancho))):
                    tiritoe2 = False
                    termino = True
                    eliminado = True
        if tiritoe3:
            if (tiritoe3y > 989):
                tiritoe3 = False
                ciclot3 = ciclos + (random.randrange(1,200,10))
            if e1:
                if ((tiritoe3y+20) >= ey) and (tiritoe3y < (ey+80)):
                    if (((tiritoe3x+10) >= e1x) and (tiritoe3x <= (e1x+160))):
                        tiritoe3 = False
                        if e1v <= 0:
                            e1 = False
                        else:
                            e1v = (e1v - 1)
            if e2:
                if ((tiritoe3y+20) >= ey) and (tiritoe3y < (ey+80)):
                    if (((tiritoe3x+10) >= e2x) and (tiritoe3x <= (e2x+160))):
                        tiritoe3 = False
                        if e2v <= 0:
                            e2 = False
                        else:
                            e2v = (e2v - 1)
            if e3:
                if ((tiritoe3y+20) >= ey) and (tiritoe3y < (ey+80)):
                    if (((tiritoe3x+10) >= e3x) and (tiritoe3x <= (e3x+160))):
                        tiritoe3 = False
                        if e3v <= 0:
                            e3 = False
                        else:
                            e3v = (e3v - 1)
            if ((tiritoe3y+20) >= jposy) and (tiritoe3y < (jposy+jalto)):
                if (((tiritoe3x+10) >= jposx) and (tiritoe3x <= (jposx+jancho))):
                    tiritoe3 = False
                    termino = True
                    eliminado = True
        if tiritoe4:
            if (tiritoe4y > 989):
                tiritoe4 = False
                ciclot4 = ciclos + (random.randrange(1,200,10))
            if e1:
                if ((tiritoe4y+20) >= ey) and (tiritoe4y < (ey+80)):
                    if (((tiritoe4x+10) >= e1x) and (tiritoe4x <= (e1x+160))):
                        tiritoe4 = False
                        if e1v <= 0:
                            e1 = False
                        else:
                            e1v = (e1v - 1)
            if e2:
                if ((tiritoe4y+20) >= ey) and (tiritoe4y < (ey+80)):
                    if (((tiritoe4x+10) >= e2x) and (tiritoe4x <= (e2x+160))):
                        tiritoe4 = False
                        if e2v <= 0:
                            e2 = False
                        else:
                            e2v = (e2v - 1)
            if e3:
                if ((tiritoe4y+20) >= ey) and (tiritoe4y < (ey+80)):
                    if (((tiritoe4x+10) >= e3x) and (tiritoe4x <= (e3x+160))):
                        tiritoe4 = False
                        if e3v <= 0:
                            e3 = False
                        else:
                            e3v = (e3v - 1)
            if ((tiritoe4y+20) >= jposy) and (tiritoe4y < (jposy+jalto)):
                if (((tiritoe4x+10) >= jposx) and (tiritoe4x <= (jposx+jancho))):
                    tiritoe4 = False
                    termino = True
                    eliminado = True


        #Bloque de Movimientos
        if tirito:
            jtiritoy = (jtiritoy-10)
        if tiritoe1:
            tiritoe1y = (tiritoe1y+10)
        if tiritoe2:
            tiritoe2y = (tiritoe2y+10)
        if tiritoe3:
            tiritoe3y = (tiritoe3y+10)
        if tiritoe4:
            tiritoe4y = (tiritoe4y+10)

        if bloquex:
            for x in range(0,len(bloquex)):
                bloquex[x] = (bloquex[x] + b1movx)
        if bloque2x:
            for x in range(0,len(bloque2x)):
                bloque2x[x] = (bloque2x[x] + b2movx)
        if bloque3x:
            for x in range(0,len(bloque3x)):
                bloque3x[x] = (bloque3x[x] + b1movx)
        if bloque4x:
            for x in range(0,len(bloque4x)):
                bloque4x[x] = (bloque4x[x] + b2movx)

        #Edificios?
        if e1:
            areajuego.blit(e01,(e1x,ey))
        if e2:
            areajuego.blit(e01,(e2x,ey))
        if e3:
            areajuego.blit(e01,(e3x,ey))

        #Los Invaders
        for b in bloquex:
            areajuego.blit(invader1,(b,bloquey))

        for b2 in bloque2x:
            areajuego.blit(invader1,(b2,bloque2y))

        for b3 in bloque3x:
            areajuego.blit(invader1,(b3,bloque3y))

        for b4 in bloque4x:
            areajuego.blit(invader1,(b4,bloque4y))

        if bloquex:
            if not tiritoe1:
                if ciclos > ciclot1:
                    tiritoe1 = True
                    if len(bloquex) >= 2:
                        tiritoe1x = (bloquex[random.randrange(0,(len(bloquex)-1),1)] + 50)
                    else:
                        tiritoex = bloquex[-1]
                    tiritoe1y = bloquey
        if bloque2x:
            if not tiritoe2:
                if ciclos > ciclot2:
                    tiritoe2 = True
                    if len(bloque2x) >= 2:
                        tiritoe2x = (bloque2x[random.randrange(0,(len(bloque2x)-1),1)] + 50)
                    else:
                        tiritoe2x = bloque2x[-1]
                    tiritoe2y = bloque2y
        if bloque3x:
            if not tiritoe3:
                if ciclos > ciclot3:
                    tiritoe3 = True
                    if len(bloque3x) >= 2:
                        tiritoe3x = (bloque3x[random.randrange(0,(len(bloque3x)-1),1)] + 50)
                    else:
                        tiritoe3x = bloque3x[-1]
                    tiritoe3y = bloque3y
        if bloque4x:
            if not tiritoe4:
                if ciclos > ciclot4:
                    tiritoe4 = True
                    if len(bloque4x) >= 2:
                        tiritoe4x = (bloque4x[random.randrange(0,(len(bloque4x)-1),1)] + 50)
                    else:
                        tiritoe4x = bloque4x[-1]
                    tiritoe4y = bloque4y
                    

        #El Rasho Laser
        #pygame.draw.rect(areajuego, white, [jposx, jposy, jancho, jalto])
        areajuego.blit(LaserImg,(jposx,jposy))

        #Los tiros del Jugador
        if tirito:
            pygame.draw.rect(areajuego, rojo, [jtiritox, jtiritoy, 10, 20])

        #Los tiritos de los enemigos
        if tiritoe1:
            pygame.draw.rect(areajuego, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), [tiritoe1x, tiritoe1y, 10, 20])
        if tiritoe2:
            pygame.draw.rect(areajuego, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), [tiritoe2x, tiritoe2y, 10, 20])
        if tiritoe3:
            pygame.draw.rect(areajuego, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), [tiritoe3x, tiritoe3y, 10, 20])
        if tiritoe4:
            pygame.draw.rect(areajuego, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), [tiritoe4x, tiritoe4y, 10, 20])
        
        #Mostrar Score arriba
        message_display("Ciclos utilizados: "+str(ciclos),400,20)

        #Mostrar todo
        pygame.display.update()
        florderelos.tick(60)
        ciclos = ciclos+1

        if not bloquex and not bloque2x and not bloque3x and not bloque4x:
            termino = True
    if eliminado:
        ciclos = -1

    return ciclos


def main():

    #Cuerpo del programa que llama al juego
    areajuego.fill(black)
    score = game_loop()
    time.sleep(2)
    if (score == -1):
        mensaje = "GAME OVER: GANARON LOS INVASORES!!!!"
        areajuego.fill(black)
        message_display(mensaje,500,500)
    else:
        mensaje = "GANASTE!!! ELIMINASTE A LOS INVASORES!!"
        mensaje2 = "EN "+str(score)+" CICLOS"
        areajuego.fill(black)
        message_display(mensaje,500,300)
        message_display(mensaje2,500,700)
    pygame.display.update()
    print(score)
    time.sleep(4)
    pygame.quit()
    quit()



if __name__ == "__main__":
    main()