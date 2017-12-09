#Heigo

import pygame

class Narko:
    def __init__(self, PointReward, BarReward, NarkoType, Mode, xPos, yPos):
        self.PointReward = PointReward                  #Punkte iga narko eest
        self.BarReward = BarReward                      #Narkolaksu bar
        self.NarkoType = NarkoType                      #Narko tüüp
        self.Mode = Mode                                #Praegune narko objekti olukord
        self.xPos = xPos                                #Koordinaat ruumis
        self.yPos = yPos

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.xPos, self.yPos, 100, 100))






