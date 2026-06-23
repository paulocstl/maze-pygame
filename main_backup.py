'''Jogo de labirinto'''
import pygame 

pygame.init()
clock = pygame.time.Clock()


resolution = WIDTH, HEIGHT = 800, 600 

screen = pygame.display.set_mode(resolution)
title = pygame.display.set_caption('Maze Escape')

screen_color = pygame.Color("#B24A01")

player_x = 45
player_y = 45

player_size = WIDTH_PLAYER, HEIGHT_PLAYER = 30, 30

player_color = 'dark green'

wall_color = "gray"

TAMANHO_BLOCO = 40

mapa = [
    "11111111111111111111",
    "10000000000000000001",
    "10111111111111111001",
    "10000000000000001001",
    "10111111111111001001",
    "10000000000001000001",
    "11111111111111111111"
]

rodando = True

velocidade = 5

def verificar_parede(x, y):
    linha = y // TAMANHO_BLOCO
    coluna = x // TAMANHO_BLOCO
    
    if mapa[linha][coluna] == '1':
        return True
    
    else:
        return False

while rodando:

    screen.fill(screen_color)
    
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[linha])):

            if mapa[linha][coluna] == "1":

                pygame.draw.rect(
                    screen,
                    wall_color,
                    (
                        coluna * TAMANHO_BLOCO,
                        linha * TAMANHO_BLOCO,
                        TAMANHO_BLOCO,
                        TAMANHO_BLOCO
                    )
                )
    
    pygame.draw.rect(
        screen,
        player_color,
        (player_x, player_y,
         WIDTH_PLAYER, HEIGHT_PLAYER)
    )

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_w]:            
        novo_y = player_y - velocidade

        if not verificar_parede(player_x, novo_y):
            player_y = novo_y
        
    elif teclas[pygame.K_s]:
        novo_y = player_y + velocidade

        if not verificar_parede(player_x, novo_y):
            player_y = novo_y
        
    elif teclas[pygame.K_a]:
        novo_x = player_x - velocidade
            
        if not verificar_parede(novo_x, player_y):
             player_x = novo_x

    elif teclas[pygame.K_d]:
        novo_x = player_x + velocidade

        if not verificar_parede(novo_x, player_y):
            player_x = novo_x
        
        if event.type == pygame.QUIT:
            rodando = False

        if player_x < 0:
            player_x = 0

        if player_x > WIDTH - WIDTH_PLAYER:
            player_x = WIDTH - WIDTH_PLAYER

        if player_y < 0:
            player_y = 0

        if player_y > HEIGHT - HEIGHT_PLAYER:
            player_y = HEIGHT - HEIGHT_PLAYER


    pygame.display.update()
    clock.tick(60)

pygame.quit()