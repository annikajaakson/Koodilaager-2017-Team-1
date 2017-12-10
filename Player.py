import pygame

class Player:
	def __init__ (self, x, y, resolution, mapn):
		self.x = x
		self.y = y
		self.resolution = resolution
		self.mapn = mapn
		self.width = self.resolution[0]/len(self.mapn[0])
		self.height = self.resolution[1]/len(self.mapn)
	def draw(self, screen, pos):
		player = pygame.Rect((pos[0]*self.width, pos[1]*self.height, self.width, self.height))
		pygame.draw.rect(screen, [0, 0, 0], player)

	def move(self, inputx, inputy, mapobject):
		canmove = True
		hyporect = pygame.Rect([(self.x + inputx) * self.width, (self.y + inputy) * self.height, self.width, self.height])
		if hyporect in mapobject.walls:
			canmove = False
		for wall in mapobject.outer_walls:
			if hyporect.colliderect(wall):
				canmove = False

		if canmove:
			self.x += inputx
			self.y += inputy
		return [self.x, self.y]


