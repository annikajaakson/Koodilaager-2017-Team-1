#Raiko
import pygame, math
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


"""fail = open("image.txt").read().split("\n")
mapn = []
for i in fail:
	a = "["
	for j in i:
		a += j + ","
	exec("mapn.append(%s)"%(a[0:-1] + "]"))"""

'''mapn = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	   [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
	   [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
	   [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
	   [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
	   [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
	   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	   [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
	   [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
	   [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
	   [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
	   [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
	   [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
	   [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
	   [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
	   [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
	   [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
	   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]'''

class map1:
	def __init__(self, resolution):
		self.resolution = resolution
		fail = open("image.txt").read().split("\n")
		self.mapn = []

		for i in fail:
			a = "["
			for j in i:
				a += j + ","
			exec("self.mapn.append(%s)" % (a[0:-1] + "]"))

		self.x = len(self.mapn[1])
		self.y = len(self.mapn)
		width = self.resolution[0] / self.x
		height = self.resolution[1] / self.y
		self.walls = []
		self.outer_walls = [pygame.Rect([0, -200, self.resolution[0], 200]),
					  pygame.Rect([0, self.resolution[1], self.resolution[0], 200]),
					  pygame.Rect([self.resolution[0], 0, 200, self.resolution[1]]),
					  pygame.Rect([-200, 0, 200, resolution[1]])
					  ]

		for i in range(len(self.mapn)):
			for j in range(len(self.mapn[i])):
				if self.mapn[i][j] == 1:
					self.walls.append(pygame.Rect((j*width, i*height, self.resolution[0]/self.x, self.resolution[1]/self.y)))

	def draw(self, screen):
		for i in self.walls:
			pygame.draw.rect(screen, (160, 95, 49), i)
		return self.walls


	def path_find(self, cop, player, mapm):
		grid = Grid(matrix=mapm)

		start = grid.node(cop[0], cop[1])
		end = grid.node(player[0], player[1])

		path, runs = AStarFinder().find_path(start, end, grid)	
		return path	

