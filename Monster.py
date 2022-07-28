import random

import pygame
import math

class Monster(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/monster.png")
        self.image = pygame.transform.scale(self.image, [65, 65])
        self.rect = pygame.Rect(0, 0, 65, 65)

        self.rect.x = 1360 + random.randint(20, 100)
        self.rect.y = random.randint(0, 670)
        self.speed = random.randint(2, 6)

    def update(self, *args):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()
