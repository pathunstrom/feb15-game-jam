import unittest

import pygame
from pygame.locals import K_w, K_a, K_s, K_d

from sprites import player, wall


def attack_one(target):
    return 1, target


def attack_two(target):
    return 2, target


class TestPlayerInstantiation(unittest.TestCase):

    def test_with_no_skills(self):
        player.Player([])

    def test_with_too_many_skills(self):
        self.assertRaises(Exception, player.Player, [attack_one, attack_one, attack_one, attack_one, attack_one])


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.pc = player.Player([attack_one, attack_two])

        def keys():
            return {K_w: 1, K_a: 0, K_s: 0, K_d: 0}
        player.pygame.key.get_pressed = keys

    def test_update_no_collide(self):
        self.pc.update(1)

        self.assertEqual(self.pc.y, 0)
        self.assertEqual(self.pc.x, 50)

    def test_update_with_collide_at_30(self):
        self.setUp()
        collide_group = pygame.sprite.Group()
        wall.Wall(50, -55, 50, 50).add(collide_group)
        self.pc.collidables = collide_group
        self.pc.update(1)
        self.assertEqual(self.pc.y, 25)

    def test_attack(self):
        self.setUp()
        self.assertEqual(1, self.pc.attack(0, 'target')[0])
        self.assertEqual(2, self.pc.attack(1, 'target')[0])
        self.pc.mod()
        self.assertIsNone(self.pc.attack(0, 'target'))
        self.assertIsNone(self.pc.attack(1, 'target'))

    def test_no_attack(self):
        self.assertIsNone(self.pc.no_attack())

    def test_mod(self):
        self.setUp()
        self.assertFalse(self.pc.skill_mod)
        self.pc.mod()
        self.assertTrue(self.pc.skill_mod)

if __name__ == '__main__':
    unittest.main()