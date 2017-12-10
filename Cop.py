#Jako
import pygame

class Cop:
    def __init__(self, x, y, resolution, mapn):
        self.x = x
        self.y = y
        self.resolution = resolution
        self.mapn = mapn
        self.width = self.resolution[0] / len(self.mapn[0])
        self.height = self.resolution[1] / len(self.mapn)
        self.move_timer = 0  # the cop can move only once the timer has reached the cooldown
        self.move_cooldown = 100  # time between steps in milliseconds

        self.rect = pygame.Rect(self.x * self.width,
                                self.y * self.height,
                                self.width, self.height)

    def pos(self):
        return [self.x, self.y]

    def update(self, delta, path):
        self.move_timer += delta

        if self.move_timer >= self.move_cooldown:
            # if there is a next tile to move to, move to that tile
            if len(path) > 2:
                self.x = path[1][0]
                self.y = path[1][1]

            self.move_timer = 0  # reset the timer

        # uodate the cop's rectangle to the current position
        self.rect.x = self.x * self.width
        self.rect.y = self.y * self.height

    def draw(self, screen, ):
        color = (0, 255, 0)
        pygame.draw.rect(screen, color, self.rect)