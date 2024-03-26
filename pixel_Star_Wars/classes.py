import pygame
import time
import os
absolute_path = os.path.dirname(__file__)
relative_path = "Assets"
full_path = os.path.join(absolute_path, relative_path)

class Player:
    def __init__(self, type, x, y, speed):
        self.type = type
        self.x = x
        self.y = y
        self.speed_bonus = 0
        self.speed = speed
        self.image = pygame.image.load(full_path + "/Players/ship_" + str(self.type) + ".png")
        self.number_of_bullets = 1

    def move(self):
        self.x += self.speed + self.speed_bonus
        if self.x <= 0:
            self.x = 0
        if self.x >= 768:
            self.x = 768

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
class Enemy:
    def __init__(self, type, x, y, speed):
        self.alive = True
        self.type = type
        self.x = x
        self.y = y
        self.speed_bonus = 0
        self.speed = speed
        self.image = pygame.image.load(full_path + "/Enemies/enemy_" + str(self.type) + ".png")
        self.time = time.time()

    def move(self):
        self.x += self.speed + self.speed_bonus
        if self.x <= 0:
            self.x = 0
        if self.x >= 768:
            self.x = 768

    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, (self.x, self.y))
        
class Laser:
    def __init__(self, type, x, y, speed_x, speed_y):
        self.alive = True
        self.type = type
        self.x = x
        self.y = y
        self.speed_bonus = 0
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.image = pygame.image.load(full_path + "/Lasers/laser_" + str(self.type) + ".png")

    def move(self):
        self.x += self.speed_x
        self.y -= self.speed_y + self.speed_bonus

    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, (self.x, self.y))

class Text:
    def __init__(self, x, y, value1):
        self.x = x
        self.y = y
        self.value1 = value1
        self.value2 = 1
        self.font = pygame.font.Font('freesansbold.ttf', 18)

    def update(self, value2):
        self.value2 = value2

    def draw(self, screen):
        string = self.font.render(str(self.value1) + str(self.value2), True, (255, 255, 255))
        screen.blit(string, (self.x, self.y))

class Level:
    def __init__(self):
        self.number = 1
        self.timer = time.time() + 10
        self.enemies_killed = 0
        self.enemy_number = 1
        self.player_type = 1
        self.player_number_of_bullets = 1
        self.enemy_type = 1
        self.laser_type = 1
        self.background_type = 1

    def update(self, number):
        self.number = number
        self.timer = time.time() + 10
        if self.number % 3 == 0:
            self.enemy_number += 1
        if self.number % 10 == 0:
            self.background_type += 1
        if self.number % 6 == 0:
            self.player_number_of_bullets += 1
        if self.enemies_killed % 20 == 0:
            self.player_type += 1

    def draw(self, screen):
        pass