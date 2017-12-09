#Mingi Pede aka Mihkel
import pygame, time, sys, math
import Player, Map

resolution = [1400, 900]
pygame.init()
image = pygame.image.load('Narkokorjaja.png')
screen = pygame.display.set_mode(resolution)
suund = None
clicked = False
map1 = Map.map1(resolution)
player = Player.Player(10, 10, 5)
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				suund = 0
			elif event.key == pygame.K_DOWN:
				suund = 1
			elif event.key == pygame.K_LEFT:
				suund = 2
			elif event.key == pygame.K_UP:
				suund = 3
		else:
			suund = None
	if clicked == False:
		screen.fill((255, 255, 255))
		screen.blit(image, (282, 120))
		mouse = pygame.mouse.get_pos()
		if 900 > mouse[0] > 500 and 750 > mouse[1] > 600:
			pygame.draw.rect(screen, [0, 255, 0], (500, 600, 400, 150))
		else:
			pygame.draw.rect(screen, [0, 200, 0], (500, 600, 400, 150))
		leftclick = pygame.mouse.get_pressed()
		if leftclick == (1, 0, 0) and 900 > mouse[0] > 500 and 750 > mouse[1] > 600:
			clicked = True
	if clicked == True:
		screen.fill((255, 255, 255))
		rects = map1.draw(screen)
		player.draw(screen, player.move(suund), rects)

	#Code here xd 1 876

	pygame.time.wait(0)
	pygame.display.update()
