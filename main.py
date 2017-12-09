#Mingi Pede aka Mihkel XD
import pygame, time, sys, math
import Player, Map

resolution = [1400, 900]
pygame.init()
image = pygame.image.load('Narkokorjaja.png')
screen = pygame.display.set_mode(resolution)

map1 = Map.map1(resolution)
player = Player.Player(10, 10, 1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    #rects = map1.draw(screen)
    screen.fill((255, 255, 255))
    screen.blit(image, (282, 120))
    #player.draw(screen, player.move(0), rects)
    mouse = pygame.mouse.get_pos()
    if 900 > mouse[0] > 500 and 750 > mouse[1] > 600:
        pygame.draw.rect(screen, [0, 255, 0], (500, 600, 400, 150))
    else:
        pygame.draw.rect(screen, [0, 200, 0], (500, 600, 400, 150))
    #Code here xd 1 876

    pygame.time.wait(60)
    pygame.display.update()
