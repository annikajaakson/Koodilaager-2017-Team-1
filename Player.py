#Karu

import pygame, time, math, main

x = 10
y = 10

class Player:
    def __init__ (self, x, y, kiirus):
        self.x = x
        self.y = y
        self.kiirus = kiirus

    def move(self, suund):
        if suund == 0:
            self.x += self.kiirus
        elif suund == 2:
            self.x -= self.kiirus
        elif suund == 1:
            self.y += self.kiirus
        elif suund == 3:
            self.y -= self.kiirus
pygame.draw.rect (screen, [0, 0, 0],(x, y, 10, 10))


