import pygame
import random
import time
import math
import os
from pygame.locals import *
from classes import Player, Enemy, Laser, Text, Level
absolute_path = os.path.dirname(__file__)
relative_path = "Assets"
full_path = os.path.join(absolute_path, relative_path)

#initializare joc
pygame.init()

#initializare ecran
screen = pygame.display.set_mode((800, 600))

#ecran
pygame.display.set_caption("pixelStarWars")
icon = pygame.image.load(full_path + "/rsz_1icon.png")
pygame.display.set_icon(icon)

#desenare frame
def draw():
    screen.blit(bg, (0, 0))
    player.draw(screen)  
    for x in enemy:
        x.draw(screen)
    for x in laser:
        x.draw(screen)
    #text_frame.draw(screen)
    text_score.draw(screen)
    text_level.draw(screen)
    text_timer.draw(screen)
    
#distanta doua puncte
def distance(laser, enemy):
    dist = math.sqrt(math.pow(enemy.x - laser.x, 2) + math.pow(enemy.y - laser.y, 2))
    if dist < 50:
        enemy.alive = False

#initializare
level = Level()
timer = time.time()
clock = pygame.time.Clock()
text_score = Text(700, 10, "Score : ")
text_frame = Text(10, 10, "FPS : ")
text_level = Text(10, 570, "LVL ")
text_timer = Text(730, 570, "")
text_game_start = Text(350, 270, "Game start in 5 seconds")
text_game_over = Text(350, 270, "GAME OVER!\nLVL :")

player = Player(1, 370, 480, 0)
enemy = []
laser = []

# timer += 4
# text_game_start.update("")
# while timer > time.time():
#     text_game_start.draw(screen)
#     pygame.display.update()

#jocul
running = 1
while running == 1:
    if level.timer < time.time():
        running = 2

    #schimbare nivel
    if(len(enemy) == 0):
        bg = pygame.image.load(full_path + "/BG/bg_" + str(level.background_type) + ".png")
        player = Player(level.player_type, player.x, player.y, player.speed)
        player.number_of_bullets = level.player_number_of_bullets
        for i in range(0, level.enemy_number):
            enemy.append(Enemy(level.enemy_type, random.randint(0, 800), 32, 0))

    for event in pygame.event.get():
        
        #exit
        if event.type == pygame.QUIT:
            running = 0
        
        #input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.speed = -0.1
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.speed = 0.1
            elif event.key == pygame.K_SPACE:
                if player.number_of_bullets == 1:
                    laser.append(Laser(level.laser_type, player.x, player.y, player.speed, 0.3))
                elif player.number_of_bullets == 2:
                    laser.append(Laser(level.laser_type, player.x - 6, player.y, player.speed, 0.3))
                    laser.append(Laser(level.laser_type, player.x + 6, player.y, player.speed, 0.3))
                elif player.number_of_bullets == 3:
                    laser.append(Laser(level.laser_type, player.x, player.y, player.speed, 0.3))
                    laser.append(Laser(level.laser_type, player.x - 6, player.y, player.speed, 0.3))
                    laser.append(Laser(level.laser_type, player.x + 6, player.y, player.speed, 0.3))
        
        #oprire nava
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed = 0

    #miscare inamic
    for x in enemy:
        if time.time() - x.time > 1:
            if x.alive == False:
                enemy.remove(x)
                level.enemies_killed += 1
            x.speed = random.choice([-0.1, 0.1])
            x.time = time.time()
    
    #update
    player.move()
    for i in enemy:
        i.move()
    for i in laser:
        if i.y < 0:
            laser.remove(i)
    for i in laser:
        i.move()
        for j in enemy:
            distance(i, j)
#    if len(enemy) == 0:
#        level.update(level.number + 1)
    if(len(enemy) == 0):
        level.update(level.number + 1)
    text_score.update(level.enemies_killed)
    text_frame.update(clock.get_fps())
    text_level.update(level.number)
    text_timer.update(int(level.timer - time.time()))
    draw()
    pygame.display.update()  

# text_game_over.update(level.number)
# for i in enemy:
#     enemy.remove(i)
# for i in laser:
    # laser.remove(i)

# while running == 2:
#     text_game_over.draw(screen)