import pygame
import sys,os,time

pygame.init()

width,height = 1200,650
tela = pygame.display.set_mode((width,height))

fundo = pygame.image.load(os.path.join("assets","img","espaco.png")).convert_alpha()
laser = pygame.image.load(os.path.join("assets","img","laser.png")).convert_alpha()
lasRec = laser.get_rect(center=(500,500))

nave = pygame.image.load(os.path.join("assets","img","ship.png")).convert_alpha()
nave = pygame.transform.scale(nave,(40,40))
navRec = nave.get_rect(center=(500,500))
print(navRec)

bg1 = pygame.image.load(os.path.join("assets","img","espaco.png")).convert_alpha()

bgR1= bg1.get_rect(center=((width/2,(height/2))))

font = pygame.font.Font(os.path.join("assets","Font","Sigmar","Sigmar-Regular.ttf"),16)
texto = font.render('S T A R - GAME', True, (244,164,96))
recText = texto.get_rect(center=(100,10))

pygame.display.set_caption("Space Kombat")
loop = True
relogio = pygame.time.Clock()

while loop:
    start = int(round(time.time()*1000))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            navRec.center = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            print(f"Tiro {event.pos}")

    tela.fill((0,0,0))
    tela.blit(fundo, (0,0))
    tela.blit(laser, lasRec)
    tela.blit(nave, navRec)
    tela.blit(texto, recText)
 
    
    pygame.display.update()
    end = int(round(time.time()*1000))

    #print(f"{end - start} ms")
    relogio.tick(120)
pygame.quit()