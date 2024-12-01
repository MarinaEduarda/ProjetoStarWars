import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, tipo, speed):
        """
        Cria um inimigo com base no tipo e na velocidade.
        """
        super().__init__()
        self.image = pygame.image.load(f"assets/{tipo}.png").convert_alpha()
        
        # Se for uma nave millenium, dobra seu tamanho
        if tipo == "millenium":
            self.image = pygame.transform.scale(self.image, (100, 100))  # Tamanho dobrado (100x100)
        else:
            self.image = pygame.transform.scale(self.image, (50, 50))  # Tamanho padrão (50x50)
        
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = random.randint(50, 550)
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()



class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        Inicializa a bala na posição do jogador.
        """
        super().__init__()
        self.image = pygame.image.load("assets/laser.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 30))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > 800:
            self.kill()


def atirar(bullet_group, all_sprites, player):
    """
    Adiciona uma bala ao grupo de tiros.
    """
    bullet = Bullet(player.rect.centerx + 30, player.rect.centery)
    bullet_group.add(bullet)
    all_sprites.add(bullet)


def detectar_colisoes(bullets, enemies):
    """
    Detecta e gerencia colisões entre balas e inimigos.
    """
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    return len(hits)
