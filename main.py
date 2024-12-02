import pygame
from script.jogador import Player
from script.ataque import Enemy
from script.cenas import Fase
from script.interfaces import TelaInicial, TelaGameOver

# Inicialização
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Proteja a Estrela da Morte")

# Controle do jogo
FPS = 60
clock = pygame.time.Clock()

# Variáveis de estado
fase_atual = 1
jogando = True
ranking = {}

# Nome do arquivo onde o ranking será salvo
RANKING_FILE = "ranking.json"

# Inicializar telas e fases
tela_inicial = TelaInicial(screen, WIDTH, HEIGHT)
fase = Fase(screen, WIDTH, HEIGHT)
tela_game_over = TelaGameOver(screen, WIDTH, HEIGHT, RANKING_FILE)

# Loop principal
while True:
    # Exibe a tela inicial e recebe o nome do jogador
    username = tela_inicial.mostrar()
    if not username:  # Sai do jogo se o jogador não inserir um nome
        break

    # Reinicia as variáveis de jogo
    fase_atual = 1
    jogando = True

    # Jogar as fases
    while jogando:
        # Executa a fase atual
        resultado, score = fase.jogar(fase_atual, username)

        if resultado == "proxima_fase":
            fase_atual += 1
            if fase_atual > 3:  # Finaliza o jogo ao passar de todas as fases
                jogando = False
                break

        elif resultado == "game_over":
            # Atualiza o ranking
            if username in ranking:
                ranking[username] = max(ranking[username], score)
            else:
                ranking[username] = score

            # Exibe a tela de Game Over
            jogando = tela_game_over.mostrar(username, score)
            if jogando:
                fase_atual = 1  # Reinicia o jogo se o jogador decidir continuar
                fase = Fase(screen, WIDTH, HEIGHT)

    if not jogando:  # Sai do jogo se o jogador não continuar
        break

pygame.quit()
