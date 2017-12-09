#Jako
import pygame
class Cop:
	def __init__(self, x, y, resolution):
		self.x = x
		self.y = y
		self.resolution = resolution
	def pos(self):
		return [self.x, self.y]
	def draw(self, screen, path):
		width = self.resolution[0]/20
		height = self.resolution[1]/18
		if len(path) >= 2:
			cop = pygame.Rect(width*path[1][0], height*path[1][1], width-2, height-2)
		else:
			cop = pygame.Rect(self.x*width, self.y*height, width-2, height-2)
		print(path)
		pygame.draw.rect(screen, (0, 255, 0), cop)