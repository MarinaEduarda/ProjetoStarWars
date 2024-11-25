import pygame, random
from script.jogador import Player
from script.ataque import Enemy

class Fase:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player = Player(100, height // 2)
        self.all_sprites.add(self.player)
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("assets/fundo.png").convert()
        self.background = pygame.transform.scale(self.background, (width, height))

    def jogar(self, nivel, username):
        running = True
        score = 0

        # Configurações de inimigos por nível
        spawn_rate = {1: 2000, 2: 1500, 3: 1000}[nivel]
        inimigo_tipo = {1: ["resistencia"], 2: ["millenium"], 3: ["resistencia", "millenium"]}[nivel]
        pygame.time.set_timer(pygame.USEREVENT, spawn_rate)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return "game_over", score
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.player.shoot(self.bullets)
                if event.type == pygame.USEREVENT:
                    tipo = random.choice(inimigo_tipo)
                    enemy = Enemy(tipo)
                    self.all_sprites.add(enemy)
                    self.enemies.add(enemy)

            # Atualizar
            self.all_sprites.update()
            hits = pygame.sprite.groupcollide(self.enemies, self.bullets, True, True)
            score += len(hits)

            for enemy in self.enemies:
                if enemy.rect.colliderect(self.player.rect):
                    return "game_over", score

            # Renderizar
            self.screen.blit(self.background, (0, 0))
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        return "proxima_fase", score
