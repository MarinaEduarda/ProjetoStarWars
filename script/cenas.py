import pygame
from script.jogador import Player
from script.ataque import Enemy, atirar, detectar_colisoes


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
        self.death_star = pygame.image.load("assets/estreladamorte.png").convert_alpha()
        self.death_star = pygame.transform.scale(self.death_star, (300, 300))
        self.death_star_rect = self.death_star.get_rect(center=(150, height // 2))

    def jogar(self, nivel, username):
        running = True
        score = 0
        spawn_rate = {1: 2000, 2: 1500, 3: 1000}[nivel]
        pygame.time.set_timer(pygame.USEREVENT, spawn_rate)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:  # Atira ao pressionar 'T'
                        atirar(self.bullets, self.all_sprites, self.player)
                if event.type == pygame.USEREVENT:
                    enemy = Enemy("resistencia")
                    self.all_sprites.add(enemy)
                    self.enemies.add(enemy)

            self.all_sprites.update()
            score += detectar_colisoes(self.bullets, self.enemies)  # Atualiza o placar com as colisões

            for enemy in self.enemies:
                if enemy.rect.colliderect(self.player.rect) or enemy.rect.colliderect(self.death_star_rect):
                    return "game_over", score

            # Renderizar
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.death_star, self.death_star_rect.topleft)
            self.all_sprites.draw(self.screen)

            # Exibir o placar
            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Score: {score}", True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))

            pygame.display.flip()
            self.clock.tick(60)

        return "proxima_fase", score
