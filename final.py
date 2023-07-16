import pygame
from pygame.locals import *
from pygame import mixer
import random
import math
#Running Game/Display Setup
pygame.init()


screen=pygame.display.set_mode((857,483))

pygame.display.set_caption("RETRO Racing")
icon=pygame.image.load('Icon.png')
pygame.display.set_icon(icon)

#Background
background=pygame.image.load('road2.jpeg')
background2 = pygame.image.load('road2.jpeg')
mixer.music.load('backrace.wav')
mixer.music.play(-1)
k=0
l=-483

#Player
user=pygame.image.load('player_car.png')
PlayerX=380
PlayerY=400
Xchange=0
Ychange=0

#enemy
en=[]
enemyX=[]
enemyY=[]

eYchange=[]
i=0
n=350
for i in range(n):
    en.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(200,610))
    enemyY.append(-150*i)

    eYchange.append(0.5)

#Score Diplay
textX=10
textY=10
score=0
game=True

#Font Setup
font=pygame.font.Font('freesansbold.ttf',32)
over_font=pygame.font.Font('freesansbold.ttf',64)
restart_font=pygame.font.Font('freesansbold.ttf',54)
mute_font=pygame.font.Font('freesansbold.ttf',16)

#Function Defining
def score1(x,y):
    global score
    score=font.render("Score: "+str(score),True,"red")
    screen.blit(score,(x,y))
def player(x,y):
    screen.blit(user,(x,y))
def enemy(x,y,i):
    screen.blit(en[i],(x,y))
def collision(enemyX,enemyY,PlayerX,PlayerY):
    distance=math.sqrt(((enemyX-PlayerX)**2)+((enemyY-PlayerY)**2))
    if distance<=50:
        return True
    else:
        return False
def game_text():
    game_over = over_font.render("GAME OVER", True, "red")
    screen.blit(game_over, (230, 250))
def restart_text():
    restart_game=restart_font.render("Press R to Restart",True,"Green")
    screen.blit(restart_game,(190,320))
def mute_text():
    mute_game=mute_font.render("M/U to Mute/Unmute",True,"Red")
    screen.blit(mute_game,(5,420))
#Game Window
running=True
while running:
    if game:
        score=0
#Quit Game
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

#Key assigning to move player car
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    Xchange-=1.0
                if event.key==pygame.K_RIGHT:
                    Xchange+=1.0
                if event.key==pygame.K_UP:
                    Ychange-=1.0
                if event.key==pygame.K_DOWN:
                    Ychange+=1.0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    Ychange=0
                    Xchange=0
#Screen Fill/Picture Loop

        screen.blit(background,(0,k))
        screen.blit(background2,(0,l))
        k+=1
        l += 1
        if k ==483:
            k = -483
        if l == 483:
            l = -483

#Restricting Car Not To Move Outside Road
        if PlayerX<=180:
            PlayerX=180
        elif PlayerX>=600:
            PlayerX=600
        if PlayerY<=0:
            PlayerY=0
        elif PlayerY>=410:
            PlayerY=410
        PlayerX += Xchange
        PlayerY += Ychange

#Enemy Loop
        for i in range (n):
            enemyY[i] +=1.35

#Collision And Restarting Game
            coll=collision(enemyX[i], enemyY[i], PlayerX, PlayerY)
            if coll:
                crash_sound=mixer.Sound('crash.wav')
                crash_sound.play()

                enemyX[i] = 2000
                enemyY[i] = 2000
                game_text()

                user = pygame.image.load('blast.png')
                Xchange = 0
                Ychange = 0

                game=False
            enemy(enemyX[i], enemyY[i], i)
#Score Counting
            if PlayerY<enemyY[i]-80:
                score +=1
        player(PlayerX,PlayerY)
        score1(textX,textY)
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
#To Restart Game
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_r:
                    game=True
                    user = pygame.image.load('player_car.png')
                    PlayerX = 380
                    PlayerY = 400
                    for i in range(n):
                        en[i]=pygame.image.load('enemy.png')
                        enemyX[i]=random.randint(200, 610)
                        enemyY[i]=-150 * i
#Game Over Text Display
        game_text()
        restart_text()
    mute_text()
#Final Display
    pygame.display.update()
