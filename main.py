# Mingi Pede aka Mihkel
import pygame, time, sys, math
import Player, Map, Cop, Narko

resolution = [1400, 900]
fps_cap = 30
clicked = False
narcotypes = {2:['LSD', (255, 255, 0)], 3:['Mushroom', (0, 255, 255)]}
score = 0

map1 = Map.map1(resolution, narcotypes)
cops_list = []
player = Player.Player(map1.x-2, map1.y-2, resolution, map1.mapn)
narko = Narko.Narko(map1.narko)

# update the locations of objects on the screen
def update(delta):
    for cop in cops_list:
        cop.update(delta, map1.path_find(cop.pos(), player.pos()))

    keys = pygame.key.get_pressed()
    player.move(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT],
                             keys[pygame.K_DOWN] - keys[pygame.K_UP], map1, delta)


# draw everything on the screen
def draw(screen):
    global score
    screen.fill((255, 255, 255))
    map1.draw(screen)

    for cop in cops_list:
        cop.draw(screen)
        score -= cop.get_score()

    if score < 0:
        screen.blit(pygame.font.SysFont("comicsansms", 200).render("BUSTED", 1, (0,0,0)), (100, 200))

    if len(narko.narko) == 0:
        map1.narko_generate()
        cops_list.append(Cop.Cop(1, 1, resolution, map1))

    player.draw(screen)
    score += narko.draw(screen, player.rect())
    screen.blit(font.render("Score: %s" % score, 1, (255,255,255)), (10, 10))


if __name__ == "__main__":
    pygame.init()
    image = pygame.image.load('Narkokorjaja.png')
    screen = pygame.display.set_mode(resolution)
    font = pygame.font.SysFont("comicsansms", 40)

    clock = pygame.time.Clock()
    delta = clock.tick()

    while True:
        delta = clock.tick()  # time in milliseconds since the last frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if not clicked:
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

        if clicked and not score < 0:
            update(delta)
            draw(screen)

        pygame.display.update()
