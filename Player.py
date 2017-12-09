import pygame

class Player:
	def __init__ (self, x, y, resolution, mapn):
		self.x = x
		self.y = y
		self.resolution = resolution
		self.mapn = mapn

	def draw(self, screen, pos, rects):
		width = self.resolution[0]/len(self.mapn[0])
		height = self.resolution[1]/len(self.mapn)
		player = pygame.Rect((pos[0]*width, pos[1]*height, width-2, height-2))
		pygame.draw.rect (screen, [0, 0, 0], player)

	def move(self, suund):
		if suund == 0:
			self.x += 1
		elif suund == 2:
			self.x -= 1
		elif suund == 1:
			self.y += 1
		elif suund == 3:
			self.y -= 1
		return [self.x, self.y]

	def collide(self, rect, rects):
		for i in rects:
			if rect.colliderect(i):
				return True
		return False    	


