#Jako
import pygame

cop_img = pygame.image.load("copdown.png")
class Cop:
    def __init__(self, x, y, resolution, map):
        self.x = x
        self.y = y
        self.resolution = resolution
        self.map = map
        self.mapn = map.mapn
        self.score = 0
        self.width = self.resolution[0] / len(self.mapn[0])
        self.height = self.resolution[1] / len(self.mapn)
        self.move_timer = 0  # the cop can move only once the timer has reached the cooldown
        self.move_cooldown = 100  # time between steps in milliseconds

        self.attack_timer = 0  # the cop can move only once the timer has reached the cooldown
        self.attack_cooldown = 1000  #

        self.rect = pygame.Rect(self.x * self.width,
                                self.y * self.height,
                                self.width, self.height)

        self.search_range = 14  # if the cop is too far form the player
        self.current_target = None  # random search target if the player is far away

    def pos(self):
        return [self.x, self.y]

    def update(self, delta, path):
        self.move_timer += delta
        self.attack_timer += delta

        self.score = 0
        if 2 >= len(path):
            if self.attack_timer >= self.attack_cooldown:
                self.score = 100
                self.attack_timer = 0
        else:
            self.score = 0

        if self.move_timer >= self.move_cooldown:
            # if there is a next tile to move to, move to that tile
            if 2 < len(path) <= self.search_range:
                self.x = path[1][0]
                self.y = path[1][1]
                self.current_target = None

            elif len(path) > self.search_range:
                # if the cop doesn't see the player, move around randomly
                if not self.current_target:
                    self.current_target = self.map.random_pos()
                    print(self.current_target)

                else:
                    path = self.map.path_find(self.pos(), self.current_target)
                    if len(path) < 2:
                        self.current_target = None
                    else:
                        self.x = path[1][0]
                        self.y = path[1][1]

            self.move_timer = 0  # reset the timer

        # uodate the cop's rectangle to the current position
        self.rect.x = self.x * self.width
        self.rect.y = self.y * self.height

    def draw(self, screen):
        color = (0, 255, 0)
        screen.blit(cop_img, (self.rect[0], self.rect[1]))

    def get_score(self):
        return self.score