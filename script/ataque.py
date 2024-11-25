import pygame
import random

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/laser.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (15, 30))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_x = 10

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left > 800:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, tipo):
        super().__init__()
        if tipo == "resistencia":
            self.image = pygame.image.load("assets/naveresistencia.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (50, 35))
        elif tipo == "millenium":
            self.image = pygame.image.load("assets/millenium.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (70, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(800, 1000)
        self.rect.y = random.randint(0, 600 - self.rect.height)
        self.speed_x = random.randint(3, 7)

    def update(self):
        self.rect.x -= self.speed_x
        if self.rect.right < 0:
            self.kill()
