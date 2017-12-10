#Raiko
import pygame, math
from random import randint
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

class map1:
    def __init__(self, resolution, narcotypes):
        self.resolution = resolution
        self.narko = []
        self.narcotypes = narcotypes

        map1.get_map(self)

        self.x = len(self.mapn[1])
        self.y = len(self.mapn)
        self.width = self.resolution[0] / self.x
        self.height = self.resolution[1] / self.y

        self.walls = []
        self.outer_walls = [pygame.Rect([0, -200, self.resolution[0], 200]),
                      pygame.Rect([0, self.resolution[1], self.resolution[0], 200]),
                      pygame.Rect([self.resolution[0], 0, 200, self.resolution[1]]),
                      pygame.Rect([-200, 0, 200, resolution[1]])]

        for i in range(len(self.mapn)):
            for j in range(len(self.mapn[i])):
                if self.mapn[i][j] == 0:
                    self.walls.append(pygame.Rect((j*self.width, i*self.height, self.width, self.height)))


    def draw(self, screen):
        for i in self.walls:
            pygame.draw.rect(screen, (160, 95, 49), i)
        return self.walls

    def path_find(self, start, end):
        grid = Grid(matrix=self.mapn)

        start_node = grid.node(start[0], start[1])
        end_node = grid.node(end[0], end[1])

        path, runs = AStarFinder(diagonal_movement=DiagonalMovement.never).find_path(start_node, end_node, grid)
        return path 

    def random_pos(self):
        pos = [randint(0, self.x-1), randint(0, self.y-1)]

        while self.mapn[pos[1]][pos[0]] == 0:
            pos = [randint(0, self.x-1), randint(0, self.y-1)]

        return pos

    def get_map(self):
        fail = open("image.txt").read().split("\n")
        self.mapn = []
        for i in fail:
            a = "["
            for j in i:
                if j == "1":
                    if randint(0, 100) == 0:
                        j = randint(2, 3)
                a += str(j) + ","

            exec("self.mapn.append(%s)" % (a[0:-1] + "]"))

    def narko_generate(self):
        map1.get_map(self)
        for i in range(len(self.mapn)):
            for j in range(len(self.mapn[i])):
                if self.mapn[i][j] >= 2:
                    self.narko.append([pygame.Rect(j*self.width, i*self.height, self.width, self.height), self.narcotypes[self.mapn[i][j]][0], self.narcotypes[self.mapn[i][j]][1]])
