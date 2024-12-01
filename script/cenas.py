import pygame
import random
from script.jogador import Player
from script.ataque import Enemy
from script.ataque import atirar, detectar_colisoes


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
        self.score = 0
        self.enemy_speed = 2  # Inicial speed for enemies

    def _alterar_fase(self):
        """
        Ajusta a dificuldade conforme o número de naves atingidas.
        """
        if self.score >= 20:
            # Quando atingir 20 naves destruídas, aparecem ambas as naves e aumenta a velocidade
            return ["resistencia", "millenium"], 4
        elif self.score >= 10:
            # Quando atingir 10 naves destruídas, muda a nave para 'millenium' e aumenta a velocidade
            return ["millenium"], 3
        else:
            # Fase inicial com a nave 'resistencia'
            return ["resistencia"], 2

    def jogar(self, nivel, username):
        running = True
        pygame.time.set_timer(pygame.USEREVENT, 1500)  # Ajuste o tempo de spawn de inimigos

        while running:
            # Atualizar inimigos e velocidade com base na pontuação
            inimigos_disponiveis, velocidade_inimigos = self._alterar_fase()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:  # Atira ao pressionar 'T'
                        atirar(self.bullets, self.all_sprites, self.player)
                if event.type == pygame.USEREVENT:
                    tipo_inimigo = random.choice(inimigos_disponiveis)
                    enemy = Enemy(tipo_inimigo, velocidade_inimigos)
                    self.all_sprites.add(enemy)
                    self.enemies.add(enemy)

            self.all_sprites.update()
            self.score += detectar_colisoes(self.bullets, self.enemies)  # Atualiza o placar com as colisões

            for enemy in self.enemies:
                if enemy.rect.colliderect(self.player.rect) or enemy.rect.colliderect(self.death_star_rect):
                    return "game_over", self.score

            # Renderizar
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.death_star, self.death_star_rect.topleft)
            self.all_sprites.draw(self.screen)

            # Exibir o placar
            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))

            pygame.display.flip()
            self.clock.tick(60)

        return "proxima_fase", self.score
