#Heigo

import pygame

class Narko:
    def __init__(self, PointReward, BarReward, NarkoType, xPos, yPos):
        self.PointReward = PointReward                  #Punkte iga narko eest
        self.BarReward = BarReward                      #Narkolaksu bar
        self.NarkoType = NarkoType                      #Narko tüüp
        self.xPos = xPos                                #Koordinaat ruumis
        self.yPos = yPos
        self.types = ["M", "C", "I", "W", "E", "K" "L", "S"]

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.xPos, self.yPos, 100, 100))

    def

    def NarkoSpecial(self, Mode):
        #1 -> kanep     3 -> speed      5 -> LSD        7 -> Ecstasy
        #2 -> liim      4 -> cocaine    6 -> Shrooms


        if Mode == 0:

        elif Mode == 1:
        elif Mode == 2:
        elif Mode == 3:
        elif Mode == 4:



