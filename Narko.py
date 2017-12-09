#Heigo

import pygame

class Narko:
    def __init__(self, PointReward, BarReward, NarkoType, xPos, yPos):
        self.PointReward = PointReward                  #Punkte iga narko eest
        self.BarReward = BarReward                      #Narkolaksu bar
        self.NarkoType = NarkoType                      #Narko tüüp
        self.xPos = xPos                                #Koordinaat ruumis
        self.yPos = yPos

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.xPos, self.yPos, 100, 100))

    def NarkoSpecial(self, Mode):
        #0 -> kanep
        #1 -> liim
        #2 -> speed
        if Mode == 0:

        elif Mode == 1:
        elif Mode == 2:
        elif Mode == 3:
        elif Mode == 4:



