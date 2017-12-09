import pygame

class Player:
    def __init__ (self, x, y, kiirus):
        self.x = x
        self.y = y
        self.kiirus = kiirus

    def draw(self, screen, pos):
        pygame.draw.rect (screen, [0, 0, 0],(pos[0], pos[1], 10, 10))

    def move(self, suund):
        if suund == 0:
            self.x += self.kiirus
        elif suund == 2:
            self.x -= self.kiirus
        elif suund == 1:
            self.y += self.kiirus
        elif suund == 3:
            self.y -= self.kiirus
        return [self.x, self.y]


