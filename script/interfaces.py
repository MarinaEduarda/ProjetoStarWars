import pygame

class TelaInicial:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

    def mostrar(self):
        running = True
        username = ""
        while running:
            self.screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 36)
            text = font.render("Digite seu nome e pressione Enter:", True, (255, 255, 255))
            self.screen.blit(text, (self.width // 4, self.height // 2 - 50))

            # Exibir o texto digitado
            username_text = font.render(username, True, (255, 255, 255))
            self.screen.blit(username_text, (self.width // 4, self.height // 2))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and username:
                        return username
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode


class TelaGameOver:
    def __init__(self, screen, width, height, ranking):
        self.screen = screen
        self.width = width
        self.height = height
        self.ranking = ranking

    def mostrar(self, username, score):
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 36)

            # Mensagem de Game Over
            text = font.render(f"Game Over! Naves destruídas: {score}", True, (255, 0, 0))
            self.screen.blit(text, (self.width // 4, 50))

            # Opções para o jogador
            option1 = font.render("Pressione R para Jogar Novamente", True, (255, 255, 255))
            option2 = font.render("Pressione Q para Encerrar", True, (255, 255, 255))
            self.screen.blit(option1, (self.width // 4, 150))
            self.screen.blit(option2, (self.width // 4, 200))

            # Exibir Ranking
            rank_title = font.render("Ranking:", True, (255, 255, 255))
            self.screen.blit(rank_title, (self.width // 4, 300))

            sorted_ranking = sorted(self.ranking.items(), key=lambda x: x[1], reverse=True)
            y = 350
            for i, (player, player_score) in enumerate(sorted_ranking):
                rank_text = font.render(f"{i + 1}. {player}: {player_score} naves destruídas", True, (255, 255, 255))
                self.screen.blit(rank_text, (self.width // 4, y))
                y += 30

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return True
                    if event.key == pygame.K_q:
                        return False
