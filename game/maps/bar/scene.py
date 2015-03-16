import pygame
from pygame.locals import KEYUP, K_ESCAPE, QUIT


def run(display, players, debug=False, **kwargs):
    if debug: print('game.maps.bar.loop.run started')

    running = True
    clock = pygame.time.Clock()

    while running:
        delta = clock.tick()
        print delta

        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
                pygame.event.post(pygame.event.Event(QUIT))
        display.fill((0, 0, 0))
        pygame.display.update()

    return None, players, None