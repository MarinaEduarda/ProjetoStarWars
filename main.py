import pygame
from script.jogador import Player
from script.ataque import Bullet, Enemy
from script.cenas import Fase
from script.interfaces import TelaInicial, TelaGameOver, TelaRanking

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
ranking = []

# Inicializar telas e fases
tela_inicial = TelaInicial(screen, WIDTH, HEIGHT)
fase = Fase(screen, WIDTH, HEIGHT)
tela_game_over = TelaGameOver(screen, WIDTH, HEIGHT)
tela_ranking = TelaRanking(screen, WIDTH, HEIGHT, ranking)

# Loop principal
while True:
    # Tela inicial
    username = tela_inicial.mostrar()
    if not username:
        break

    # Jogar as fases
    while jogando:
        resultado, score = fase.jogar(fase_atual, username)
        if resultado == "proxima_fase":
            fase_atual += 1
            if fase_atual > 3:
                break
        elif resultado == "game_over":
            ranking.append((username, score))
            jogando = tela_game_over.mostrar(score)
            fase_atual = 1 if jogando else fase_atual

    # Tela de ranking
    tela_ranking.mostrar()
    jogando = False  # Reinicia o ciclo após o ranking
