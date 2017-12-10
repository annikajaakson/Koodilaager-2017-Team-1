import pygame

up_img = pygame.image.load("yles.png")
down_img = pygame.image.load("alla.png")
left_img = pygame.image.load("vasak.png")
right_img = pygame.image.load("parem.png")
rotation = {-1: left_img, 1: right_img, -2: up_img, 2: down_img}


class Player:
    def __init__(self, x, y, resolution, mapn):
        self.x = x
        self.y = y
        self.last = 1
        self.resolution = resolution
        self.mapn = mapn
        self.width = self.resolution[0] / len(self.mapn[0])
        self.height = self.resolution[1] / len(self.mapn)

        # data about the characters rotation
        self.roty = 1  # 1 - right, -1 - left, 0 - neither
        self.rotx = 2  # 2 - down, -2 - up, 0 - neither
        self.last = 1  # rotation during the last frame

        self.move_timer = 0  # the player can move only once the timer has reached the cooldown
        self.move_cooldown = 30  # time between steps in milliseconds (heigher means lower speed)

    def pos(self):
        return [self.x, self.y]

    def draw(self, screen):
        if self.rotx:
            screen.blit(rotation[self.rotx], (self.x * self.width - 20, self.y * self.height))
        elif self.roty:
            screen.blit(rotation[self.roty], (self.x * self.width - 20, self.y * self.height))
        else:
            screen.blit(rotation[self.last], (self.x * self.width - 20, self.y * self.height))

    def move(self, inputx, inputy, mapobject, delta):
        canmove = True
        hyporect = pygame.Rect(
            [(self.x + inputx) * self.width, (self.y + inputy) * self.height, self.width, self.height])
        if hyporect in mapobject.walls:
            canmove = False
        for wall in mapobject.outer_walls:
            if hyporect.colliderect(wall):
                canmove = False

        if self.rotx:
            self.last = self.rotx
        elif self.roty:
            self.last = self.roty
        else:
            self.last = 1

        self.rotx = inputx
        self.roty = inputy

        self.move_timer += delta

        # if the player can move, update their position
        if canmove and self.move_timer >= self.move_cooldown:
            self.x += inputx
            self.y += inputy
            self.move_timer = 0
