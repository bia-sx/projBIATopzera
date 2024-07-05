import pygame
import sys
 
pygame.init()

# Configurações da tela
LARGURA_TELA = 900
ALTURA_TELA = 900
LINHA_LARGURA = 20
WIN_LINE_WIDTH = 60
TILE_SIZE = 300
CIRCLE_RADIUS = TILE_SIZE // 3
CIRCLE_WIDTH = 25
CROSS_WIDTH = 40
SPACE = TILE_SIZE // 5
 
# Cores
BRANCO = (0, 0, 0)
PRETO = (255, 255, 255)
ROXO = (255, 191, 0)
VERDE = (244, 0, 161)
 
# Configurações da tela
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('Jogo da Velha')
tela.fill(BRANCO)
 
# Tabuleiro
tabuleiro = [[0 for x in range(3)] for y in range(3)]
 
# Desenhar linhas do tabuleiro
def desenhar_linhas():
    # Linhas horizontais
    pygame.draw.line(tela, PRETO, (0, TILE_SIZE), (LARGURA_TELA, TILE_SIZE), LINHA_LARGURA)
    pygame.draw.line(tela, PRETO, (0, 2 * TILE_SIZE), (LARGURA_TELA, 2 * TILE_SIZE), LINHA_LARGURA)
    # Linhas verticais
    pygame.draw.line(tela, PRETO, (TILE_SIZE, 0), (TILE_SIZE, ALTURA_TELA), LINHA_LARGURA)
    pygame.draw.line(tela, PRETO, (2 * TILE_SIZE, 0), (2 * TILE_SIZE, ALTURA_TELA), LINHA_LARGURA)
 
# Desenhar símbolos
def desenhar_simbolos():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == 1:
                pygame.draw.circle(tela, ROXO, (int(coluna * TILE_SIZE + TILE_SIZE // 2), int(linha * TILE_SIZE + TILE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif tabuleiro[linha][coluna] == 2:
                pygame.draw.line(tela, VERDE, (coluna * TILE_SIZE + SPACE, linha * TILE_SIZE + TILE_SIZE - SPACE), (coluna * TILE_SIZE + TILE_SIZE - SPACE, linha * TILE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(tela, VERDE, (coluna * TILE_SIZE + SPACE, linha * TILE_SIZE + SPACE), (coluna * TILE_SIZE + TILE_SIZE - SPACE, linha * TILE_SIZE + TILE_SIZE - SPACE), CROSS_WIDTH)
 
# Verificar vitória
def verificar_vitoria(player):
    # Verificar linhas
    for linha in range(3):
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] == player:
            desenhar_linha_vitoria(linha, 0, linha, 2)
            return True
 
    # Verificar colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == player:
            desenhar_linha_vitoria(0, coluna, 2, coluna)
            return True
 
    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == player:
        desenhar_linha_vitoria(0, 0, 2, 2)
        return True
 
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == player:
        desenhar_linha_vitoria(0, 2, 2, 0)
        return True
 
    return False
 
# Desenhar linha da vitória
def desenhar_linha_vitoria(linha1, coluna1, linha2, coluna2):
    x1 = coluna1 * TILE_SIZE + TILE_SIZE // 2
    y1 = linha1 * TILE_SIZE + TILE_SIZE // 2
    x2 = coluna2 * TILE_SIZE + TILE_SIZE // 2
    y2 = linha2 * TILE_SIZE + TILE_SIZE // 2
    pygame.draw.line(tela, PRETO, (x1, y1), (x2, y2), WIN_LINE_WIDTH)
 
# Verificar empate
def verificar_empate():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == 0:
                return False
    return True
 
# Reiniciar o jogo
def reiniciar_jogo():
    tela.fill(BRANCO)
    desenhar_linhas()
    for linha in range(3):
        for coluna in range(3):
            tabuleiro[linha][coluna] = 0
 
desenhar_linhas()
 
# Loop principal do jogo
executando = True
player = 1
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            mouseX = evento.pos[0]  # x
            mouseY = evento.pos[1]  # y
 
            clicked_row = int(mouseY // TILE_SIZE)
            clicked_col = int(mouseX // TILE_SIZE)
 
            if tabuleiro[clicked_row][clicked_col] == 0:
                tabuleiro[clicked_row][clicked_col] = player
                if verificar_vitoria(player):
                    print(f"Jogador {player} venceu!")
                    reiniciar_jogo()
                elif verificar_empate():
                    print("Empate!")
                    reiniciar_jogo()
                player = 3 - player
 
    desenhar_simbolos()
    pygame.display.update()
 
pygame.quit()
sys.exit()