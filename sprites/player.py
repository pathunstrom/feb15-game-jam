import pygame
from pygame.locals import K_w, K_a, K_s, K_d

from vector import Vector2


class Player(pygame.sprite.DirtySprite):

    def __init__(self, skills):
        pygame.sprite.DirtySprite.__init__(self)
        surface = pygame.Surface((50, 50))
        pygame.draw.circle(surface, (0, 0, 255), (25, 25), 25)
        self.image = surface
        self.rect = self.image.get_rect()

        self.skill_mod = False
        self.skill_list = [
                          [self.no_attack, self.no_attack],
                          [self.no_attack, self.no_attack]]
        if len(skills) > 4:
            raise Exception
        for index, skill in enumerate(skills):
            self.skill_list[index / 2][index % 2] = skill
        self.x = 50
        self.y = 50
        self.rect.center = self.x, self.y
        self.current_speed = 50
        self.collidables = pygame.sprite.Group()

        hp = 100  # At some point this will be hp - time

    def update(self, td):
        keys = pygame.key.get_pressed()
        x = -keys[K_a] + keys[K_d]
        y = -keys[K_w] + keys[K_s]
        move = Vector2(x, y).normalize()
        move *= self.current_speed * td
        old = self.rect.copy()
        self.rect.center = self.x + move['x'], self.y + move['y']
        colliding = pygame.sprite.spritecollideany(self, self.collidables)
        while colliding:
            move *= .5
            self.rect = old.copy()
            self.rect.center = self.x + move['x'], self.y + move['y']
            colliding = pygame.sprite.spritecollideany(self, self.collidables)
        self.x += move['x']
        self.y += move['y']

    def attack(self, mouse, *args):
        return self.skill_list[self.skill_mod][mouse](*args)

    def mod(self):
        self.skill_mod = not self.skill_mod

    def no_attack(self, *args):
        return None


class LengthError(BaseException):
    pass

# ----------------------------------------------------------------------------
# Notes and testing functions.
# ----------------------------------------------------------------------------
"""
#Write function attack(toggle keypress):
	def attack(self, mouse):
		mousebutton1, mousebutton2 = 0, 0

		if self.skill_mod == 0:
			mousebutton1 = self.skill_list[0][0]
			bousebutton2 = self.skill_list[0][1]
		elif self.skill_mod == 1:
			mousebutton1 = self.skill_list[1][0]
			mousebutton2 = self.skill_list[1][1]

		return mousebutton1, mousebutton2"""

"""non-combat area loop
combat area loop

character model gets passed around

set all of this up in an init function:
player module:
	player sprite (and relevant update functions)
		don't worry about update function for right now


movement
toggles on the character - need to know if we're going in DIRECTION
1 skill mod - True or False* - Primary 2 buttons or alternate 2 buttons
Each different Skill - 4 skill slots


draw function:
surface - Dirty Sprite

Things to track:
Each Direction - is it moving
Skill modifier (toggle button for mouse click functionality)
4 individual skills - will all be initializers - either a function or a class (will be a sprite that has its own behaviors)


(In Player Module)"""