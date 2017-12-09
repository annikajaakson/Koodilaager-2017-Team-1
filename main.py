#Mingi Pede aka Mihkel
import pygame, time, sys, math, Map
import Player

resolution = [1400, 900]
pygame.init()
image = pygame.image.load('Narkokorjaja.png')
screen = pygame.display.set_mode(resolution)

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
    screen.fill((255, 255, 255))
    screen.blit(image, (282, 120))
    player.draw(screen, player.move(0))
    pygame.draw.rect(screen, [0, 255, 0], (500, 600, 400, 150))
    #Code here xd 1

    pygame.time.wait(60)
    pygame.display.update()
