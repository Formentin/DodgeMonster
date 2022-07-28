import pygame


class Plague_Doctor(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/player.png")
        self.image = pygame.transform.scale(self.image, [60, 128])
        self.rect = pygame.Rect(0, 290, 78, 113)

    def update(self, *args):
        #logica

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            step_player = pygame.mixer.Sound("data/step.wav")
            self.rect.x += 5
        if keys[pygame.K_a]:
            step_player = pygame.mixer.Sound("data/step.wav")
            self.rect.x -= 5
        if keys[pygame.K_w]:
            step_player = pygame.mixer.Sound("data/step.wav")
            self.rect.y -= 4
        if keys[pygame.K_s]:
            step_player = pygame.mixer.Sound("data/step.wav")
            self.rect.y += 4

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 680:
            self.rect.bottom = 680
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 1360:
            self.rect.right = 1360