import pygame


def run(display, player, debug=False, **kwargs):
    if debug: print('game.maps.test.run started')

    running = True
    clock = pygame.time.Clock()
    play_area = display.get_rect()
    door = pygame.Rect(0, 0, 100, 50)

    while running:
