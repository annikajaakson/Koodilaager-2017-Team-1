#Heigo

import pygame

class Narko:
    def __init__(self, narko):
        self.narko = narko

    def draw(self, screen, player):
        for i in range(len(self.narko)):
            if self.narko[i][0].colliderect(player):
                del self.narko[i]
                return Narko.NarkoSpecial(self, self.narko[i][1])
            pygame.draw.rect(screen, self.narko[i][2], self.narko[i][0])

    def NarkoSpecial(self, Mode):
        #1 -> kanep     3 -> speed      5 -> LSD        7 -> Ecstasy
        #2 -> liim      4 -> cocaine    6 -> Shrooms
        if Mode == "LSD":
            return "LSD (Koomas)"
        elif Mode == "Mushroom":
            return "Mushroom (Pilves)"



