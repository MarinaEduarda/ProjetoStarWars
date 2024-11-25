import pygame
from script.ataque import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/jogador.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 40))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_y = 0

    def update(self):
        keys = pygame.key.get_pressed()
        self.speed_y = 0
        if keys[pygame.K_UP]:
            self.speed_y = -5
        if keys[pygame.K_DOWN]:
            self.speed_y = 5
        self.rect.y += self.speed_y
        self.rect.y = max(0, min(600 - self.rect.height, self.rect.y))

    def shoot(self, bullets):
        from ataque import Bullet
        bullet = Bullet(self.rect.right, self.rect.centery)
        bullets.add(bullet)
