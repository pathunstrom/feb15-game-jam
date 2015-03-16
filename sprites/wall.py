import pygame


class Wall(pygame.sprite.DirtySprite):

    def __init__(self, x, y, h, w):
        super(Wall, self).__init__()
        self.rect = pygame.Rect(x, y, h, w)
        self.image = pygame.Surface((h, w))