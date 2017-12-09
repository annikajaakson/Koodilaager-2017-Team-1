#Jako
import pygame
class Cop:
	def __init__(self, x, y, resolution, mapn):
		self.x = x
		self.y = y
		self.resolution = resolution
		self.mapn = mapn
	def pos(self):
		return [self.x, self.y]
	def draw(self, screen, path):
		width = self.resolution[0]/len(self.mapn[0])
		height = self.resolution[1]/len(self.mapn)
		if len(path) >= 2:
			self.x = path[1][0]
			self.y = path[1][1]
		cop = pygame.Rect(self.x*width, self.y*height, width-2, height-2)
		print(path)
		pygame.draw.rect(screen, (0, 255, 0), cop)