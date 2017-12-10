import pygame

up_img = pygame.image.load("yles.png")
down_img = pygame.image.load("alla.png")
left_img = pygame.image.load("vasak.png")
right_img = pygame.image.load("parem.png")
rotation = {-1:left_img, 1:right_img, -2:up_img, 2:down_img}
class Player:
	def __init__ (self, x, y, resolution, mapn):
		self.x = x
		self.y = y
		self.last = 1
		self.resolution = resolution
		self.mapn = mapn
		self.width = self.resolution[0]/len(self.mapn[0])
		self.height = self.resolution[1]/len(self.mapn)
	def draw(self, screen, pos, rotx, roty):
		roty = roty*2
		if rotx:
			screen.blit(rotation[rotx], (pos[0]*self.width, pos[1]*self.height))
			self.last = rotx
		elif roty:
			screen.blit(rotation[roty], (pos[0]*self.width, pos[1]*self.height))
			self.last = roty
		else:
			screen.blit(rotation[self.last], (pos[0]*self.width, pos[1]*self.height))
		#player = pygame.Rect((0, 0, self.width, self.height))
		#pygame.draw.rect(screen, [0, 0, 0], player)

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

