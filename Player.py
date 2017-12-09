import pygame

class Player:
	def __init__ (self, x, y, resolution):
		self.x = x
		self.y = y
		self.resolution = resolution

	def draw(self, screen, pos, rects):
		width = self.resolution[0]/20
		height = self.resolution[1]/18
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


