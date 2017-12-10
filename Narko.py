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
            if self.narko[i][1] == "mushroom":
                screen.blit(seen, (self.narko[i][0][0]-1, self.narko[i][0][1]+15))
            elif self.narko[i][1] == "weed":
                screen.blit(weed, (self.narko[i][0][0]-1, self.narko[i][0][1]+15))
            elif self.narko[i][1] == "syringe":
                screen.blit(syringe, (self.narko[i][0][0]-1, self.narko[i][0][1]+15))

        for i in range(len(self.narko)):
            if self.narko[i][0].colliderect(player):
                b = self.narko[i]
                del self.narko[i]
                return Narko.NarkoSpecial(self, b[1])
        return 0

    def NarkoSpecial(self, Mode):
        if Mode == "weed":
            return 50
        elif Mode == "mushroom":
            return 100
        elif Mode == "syringe":
            return 150



