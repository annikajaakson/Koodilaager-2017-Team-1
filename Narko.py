#Heigo

import pygame

seen = pygame.image.load("seen.png")
weed = pygame.image.load("weed.png")
syringe = pygame.image.load("syringe.png")

class Narko:
    def __init__(self, narko):
        self.narko = narko

    def draw(self, screen, player):
        for i in range(len(self.narko)):
            #pygame.draw.rect(screen, self.narko[i][2], self.narko[i][0])
            if self.narko[i][1] == "Mushroom":
                screen.blit(seen, (self.narko[i][0][0]-1, self.narko[i][0][1]+15))
            elif self.narko[i][1] == "Weed":
                screen.blit(weed, (self.narko[i][0][0]-1, self.narko[i][0][1]+15))
            elif self.narko[i][1] == "Syringe":
                screen.blit(syringe, (self.narko[i][0][0]-1, self.narko[i][0][1]+15))
        for i in range(len(self.narko)):
            if self.narko[i][0].colliderect(player):
                b = self.narko[i]
                del self.narko[i]
                return Narko.NarkoSpecial(self, b[1])
        return 0

    def NarkoSpecial(self, Mode):
        #1 -> kanep     3 -> speed      5 -> LSD        7 -> Ecstasy
        #2 -> liim      4 -> cocaine    6 -> Shrooms
        if Mode == "Weed":
            return 50
        elif Mode == "Mushroom":
            return 100
        elif Mode == "Syringe":
            return 150



