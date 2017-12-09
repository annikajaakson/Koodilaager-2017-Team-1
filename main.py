#Mingi Pede aka Mihkel
import pygame, time, sys, math, Player, Map

resolution = [1400, 900]
pygame.init()
image = pygame.image.load('Narkokorjaja.png')
screen = pygame.display.set_mode(resolution)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
	screen.fill((255, 255, 255))
	screen.blit(image, (264, 120))
	#Code here xd 1

	pygame.time.wait(60)
	pygame.display.update()


