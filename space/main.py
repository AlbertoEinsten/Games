import pygame
import sys,os,time


def update_laser(laser_list,speed=300):
    for laserRec in laser_list:
        laserRec.y -= round(speed*dt)
        if laserRec.midbottom[1] < 0:
            laser_list.remove(laserRec)

def displayScore(tela,font):
    score_text = str(f"S T A R - GAME {pygame.time.get_ticks()//1000}")
    texto = font.render(score_text, True, (244,164,96))
    recText = texto.get_rect(midleft=(30,15))
    tela.blit(texto, recText)

pygame.init()

width,height = 1200,650
tela = pygame.display.set_mode((width,height))

fundo = pygame.image.load(os.path.join("assets","img","espaco.png")).convert_alpha()
lasersurf = pygame.image.load(os.path.join("assets","img","laser.png")).convert_alpha()
lasersurf = pygame.transform.scale(lasersurf, (4,40))

nave = pygame.image.load(os.path.join("assets","img","ship.png")).convert_alpha()
nave = pygame.transform.scale(nave,(40,40))
navRec = nave.get_rect(center=(500,500))
laser_list = []
laserRec = lasersurf.get_rect(midbottom=navRec.midtop)
print(navRec)
#print(laserRec)

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            laserRec = lasersurf.get_rect(midbottom=navRec.midtop)
            laser_list.append(laserRec)

    laserRec.y -= 1

    tela.fill((0,0,0))
    tela.blit(fundo, (0,0))
    tela.blit(nave, navRec)
    for laserRec in laser_list:
        tela.blit(lasersurf, laserRec)
    
    
    update_laser(laser_list)

    displayScore(tela=tela,font=font)
    
    pygame.display.update()
    end = int(round(time.time()*1000))

    #print(f"{end - start} ms")
    dt = relogio.tick(120)/1000
pygame.quit()