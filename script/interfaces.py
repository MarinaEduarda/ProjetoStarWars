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
            self.screen.blit(text, (self.width // 4, self.height // 2))
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
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

    def mostrar(self, score):
        font = pygame.font.Font(None, 64)
        text = font.render(f"Game Over! Score: {score}", True, (255, 0, 0))
        self.screen.blit(text, (self.width // 4, self.height // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        return True

class TelaRanking:
    def __init__(self, screen, width, height, ranking):
        self.screen = screen
        self.width = width
        self.height = height
        self.ranking = ranking

    def mostrar(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("Ranking Final:", True, (255, 255, 255))
        self.screen.blit(text, (self.width // 4, 50))

        y = 100
        for i, (username, score) in enumerate(sorted(self.ranking, key=lambda x: x[1], reverse=True)):
            rank_text = font.render(f"{i+1}. {username}: {score}", True, (255, 255, 255))
            self.screen.blit(rank_text, (self.width // 4, y))
            y += 40

        pygame.display.flip()
        pygame.time.wait(5000)
