import pygame
from pygame.locals import KEYUP, QUIT, MOUSEBUTTONUP, K_ESCAPE, K_RETURN, K_t
import maps.bar.scene as bar
import maps.test.scene as test


def run(screen, debug=False, **kwargs):
    if debug:
        print "game.menu.loop started"
    font = pygame.font.Font('freesansbold.ttf', 20)
    message = font.render('Start', True, (255, 255, 255))
    m_rect = message.get_rect()
    screen_rect = screen.get_rect()

    m_rect.center = screen_rect.center
    screen.blit(message, m_rect)
    running = True
    scene = None
    while running:
        running, scene = handle_events(screen, debug)
        screen.blit(message, m_rect)
        pygame.display.update()
    if debug:
        print "game.menu.loop ended"
    return scene, None, None


def handle_events(screen, debug):
    for event in pygame.event.get():
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                return False, None
            elif event.key == K_RETURN:
                return False, bar
            elif event.key == K_t:
                return False, test
        elif event.type == MOUSEBUTTONUP:
            return False, bar
        elif event.type == QUIT:
            return False, None

    return True, None