#Mingi Pede aka Mihkel
import pygame, time, sys, math
import Player, Map, Cop

resolution = [1400, 900]
pygame.init()
image = pygame.image.load('Narkokorjaja.png')
screen = pygame.display.set_mode(resolution)

clicked = False
narcotypes = {2:['LSD', (255, 255, 0)], 3:['Mushroom', (0, 255, 255)]}

map1 = Map.map1(resolution, narcotypes)
cop = Cop.Cop(1, 1, resolution, map1.mapn)
player = Player.Player(1, 1, resolution, map1.mapn)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()


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
	Keys = pygame.key.get_pressed()

	if clicked == True:
		screen.fill((255, 255, 255))
		walls = map1.draw(screen)
		player_Pos = player.move(Keys[pygame.K_RIGHT]-Keys[pygame.K_LEFT], Keys[pygame.K_DOWN]-Keys[pygame.K_UP],map1)
		player.draw(screen, player_Pos, Keys[pygame.K_RIGHT]-Keys[pygame.K_LEFT], Keys[pygame.K_DOWN]-Keys[pygame.K_UP])
		cop.draw(screen, map1.path_find(cop.pos(), player_Pos))

	pygame.time.wait(20)
	pygame.display.update()
