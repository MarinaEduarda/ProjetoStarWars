import pygame
import json
import os

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
    def __init__(self, screen, width, height, ranking_file):
        self.screen = screen
        self.width = width
        self.height = height
        self.ranking_file = ranking_file
        self.ranking = self.carregar_ranking()

    def carregar_ranking(self):
        """
        Carrega o ranking do arquivo JSON, ou retorna um dicionário vazio se o arquivo não existir
        ou estiver vazio/corrompido.
        """
        if not os.path.exists(self.ranking_file):
            return {}

        try:
            with open(self.ranking_file, "r") as file:
                data = file.read().strip()
                if not data:
                    return {}
                return json.loads(data)
        except (json.JSONDecodeError, IOError):
            return {}

    def salvar_ranking(self):
        """
        Salva o ranking no arquivo JSON.
        """
        with open(self.ranking_file, "w") as file:
            json.dump(self.ranking, file, indent=4)

    def mostrar(self, username, score):
        """
        Exibe a tela de Game Over com opções para jogar novamente ou encerrar o jogo.
        """
        # Atualiza o ranking
        if username in self.ranking:
            self.ranking[username] = max(self.ranking[username], score)
        else:
            self.ranking[username] = score

        self.salvar_ranking()

        running = True
        while running:
            self.screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 36)

            # Texto principal
            text = font.render(f"Game Over! Pontuação: {score}", True, (255, 0, 0))
            self.screen.blit(text, (self.width // 4, 50))

            # Opções
            jogar_novamente_text = font.render("Jogar Novamente (J)", True, (255, 255, 255))
            encerrar_text = font.render("Encerrar (E)", True, (255, 255, 255))
            self.screen.blit(jogar_novamente_text, (self.width // 4, 150))
            self.screen.blit(encerrar_text, (self.width // 4, 200))

            # Ranking
            rank_title = font.render("Ranking:", True, (255, 255, 0))
            self.screen.blit(rank_title, (self.width // 4, 300))

            sorted_ranking = sorted(self.ranking.items(), key=lambda x: x[1], reverse=True)
            y = 350
            for i, (player, player_score) in enumerate(sorted_ranking[:10]):  # Exibir Top 10
                rank_text = font.render(f"{i + 1}. {player}: {player_score}", True, (255, 255, 255))
                self.screen.blit(rank_text, (self.width // 4, y))
                y += 30

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_j:  # Jogar novamente
                        return True
                    if event.key == pygame.K_e:  # Encerrar
                        pygame.quit()
                        exit()
