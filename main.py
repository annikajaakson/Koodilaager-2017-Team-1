#Mingi Pede aka Mihkel
import pygame, time, sys, math, Player, Map

resolution = [1440, 900]
pygame.init()
screen = pygame.display.set_mode(resolution)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	screen.fill((0, 0, 0))

	#Code here

	pygame.time.wait(60)
	pygame.display.update()