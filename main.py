'''Jogo de labirinto: Maze Escape'''

import pygame
import random

pygame.init()

clock = pygame.time.Clock()

# Janela de resolução do jogo

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Maze Escape")

# Imagens do jogo

jogador_img = pygame.image.load("PyGame/imagens/jogador.png")
parede_img = pygame.image.load("PyGame/imagens/parede.png")
piso_img = pygame.image.load("PyGame/imagens/piso.png")
chave_img = pygame.image.load("PyGame/imagens/chave.png")
porta_img = pygame.image.load("PyGame/imagens/porta.png")

jogador_img = pygame.transform.scale(jogador_img, (30, 30))

parede_img = pygame.transform.scale(parede_img, (55, 55))

piso_img = pygame.transform.scale(piso_img, (55, 55))

chave_img = pygame.transform.scale(chave_img, (25, 25))

porta_img = pygame.transform.scale(porta_img, (40, 40))

#tamanho do jogador, blocos e mapas

player_x = 45
player_y = 45

WIDTH_PLAYER = 30
HEIGHT_PLAYER = 30

velocidade = 4

TAMANHO_BLOCO = 40

mapa1 = [
    "11111111111111111111",
    "10000000000000000001",
    "10111111111111111001",
    "10000000000000001001",
    "10111111111111001001",
    "10000000000001000001",
    "10111111111101111001",
    "10000000000100000001",
    "10111111110111111001",
    "10000000010000000001",
    "10111111011111111001",
    "10000001000000001001",
    "10111101111111001001",
    "10000000000000000001",
    "11111111111111111111"
]

mapa2 = [
    "11111111111111111111",
    "10000010000000000001",
    "10111010111111111001",
    "10001010000000001001",
    "10111011111111001001",
    "10000000000001000001",
    "11111111110111111001",
    "10000000010000000001",
    "10111111011111111001",
    "10000001000000001001",
    "10111101111111001001",
    "10000000000001000001",
    "10111111111101111001",
    "10000000000000000001",
    "11111111111111111111"
]

mapa3 = [
    "11111111111111111111",
    "10000000001000000001",
    "10111111101011111001",
    "10000000100000001001",
    "10111110111111001001",
    "10000000000001000001",
    "10111111111101111001",
    "10000000000100000001",
    "10111111110111111001",
    "10000001000000000001",
    "10111101111111111001",
    "10000000000000001001",
    "10111111111111001001",
    "10000000000000000001",
    "11111111111111111111"
]

mapa4 = [
    "11111111111111111111",
    "10000000000000000001",
    "10111111101111111001",
    "10000000100000001001",
    "10111110111111001001",
    "10000000000001000001",
    "10111111111101111001",
    "10000000000100000001",
    "10111111110111111001",
    "10000001000000000001",
    "10111101111111111001",
    "10000000000000001001",
    "10111111111111001001",
    "10000000000000000001",
    "11111111111111111111"
]

mapa5 = [
    "11111111111111111111",
    "10000000000000000001",
    "10111111111101111001",
    "10000000000100001001",
    "10111111110111001001",
    "10000000000000000001",
    "10111111111111111001",
    "10000000000000000001",
    "10111111110111111001",
    "10000001000000000001",
    "10111101111111111001",
    "10000000000000001001",
    "10111111111111001001",
    "10000000000000000001",
    "11111111111111111111"
]

lista_mapas = [
    mapa1,
    mapa2,
    mapa3,
    mapa4,
    mapa5
]

mapa = random.choice(lista_mapas)

def verificar_parede(x, y):

    esquerda = x // TAMANHO_BLOCO

    direita = (
        x + WIDTH_PLAYER - 1
    ) // TAMANHO_BLOCO

    topo = y // TAMANHO_BLOCO

    baixo = (
        y + HEIGHT_PLAYER - 1
    ) // TAMANHO_BLOCO

    if (
        mapa[topo][esquerda] == "1"
        or mapa[topo][direita] == "1"
        or mapa[baixo][esquerda] == "1"
        or mapa[baixo][direita] == "1"
    ):
        return True

    return False

def gerar_posicao():

    while True:

        coluna = random.randint(
            1,
            len(mapa[0]) - 2
        )

        linha = random.randint(
            1,
            len(mapa) - 2
        )

        if mapa[linha][coluna] == "0":

            return (
                coluna * TAMANHO_BLOCO + 5,
                linha * TAMANHO_BLOCO + 5
            )

tem_chave = False

venceu = False

fonte = pygame.font.SysFont(
    "arial",
    40
)

chave_x, chave_y = gerar_posicao()

porta_x, porta_y = gerar_posicao()

while (
    abs(chave_x - porta_x) < TAMANHO_BLOCO
    and
    abs(chave_y - porta_y) < TAMANHO_BLOCO
):

    porta_x, porta_y = gerar_posicao()

rodando = True


while rodando:

    screen.fill("black")

    for linha in range(len(mapa)):

        for coluna in range(len(mapa[linha])):

            x = coluna * TAMANHO_BLOCO

            y = linha * TAMANHO_BLOCO

            screen.blit(
                piso_img,
                (x, y)
            )

            if mapa[linha][coluna] == "1":

                screen.blit(
                    parede_img,
                    (x, y)
                )

    if not tem_chave:

        screen.blit(
            chave_img,
            (chave_x, chave_y)
        )

    screen.blit(
        porta_img,
        (porta_x, porta_y)
    )

    screen.blit(
        jogador_img,
        (player_x, player_y)
    )
    
    screen.blit(
        jogador_img,
        (player_x, player_y)
    )

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            rodando = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:

                if venceu:

                    mapa = random.choice(lista_mapas)

                    player_x = 45
                    player_y = 45

                    tem_chave = False

                    venceu = False

                    chave_x, chave_y = gerar_posicao()

                    porta_x, porta_y = gerar_posicao()

                    while (
                        chave_x == porta_x
                        and
                        chave_y == porta_y
                    ):

                        porta_x, porta_y = gerar_posicao()

    #movimentação wasd

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_w]:

        novo_y = player_y - velocidade

        if not verificar_parede(
            player_x,
            novo_y
        ):

            player_y = novo_y

    elif teclas[pygame.K_s]:

        novo_y = player_y + velocidade

        if not verificar_parede(
            player_x,
            novo_y
        ):

            player_y = novo_y

    elif teclas[pygame.K_a]:

        novo_x = player_x - velocidade

        if not verificar_parede(
            novo_x,
            player_y
        ):

            player_x = novo_x

    elif teclas[pygame.K_d]:

        novo_x = player_x + velocidade

        if not verificar_parede(
            novo_x,
            player_y
        ):

            player_x = novo_x

    if not tem_chave:

            if (
                player_x < chave_x + 25
                and player_x + WIDTH_PLAYER > chave_x
                and player_y < chave_y + 25
                and player_y + HEIGHT_PLAYER > chave_y
            ):

                tem_chave = True

    if tem_chave:

            if (
                player_x < porta_x + 40
                and player_x + WIDTH_PLAYER > porta_x
                and player_y < porta_y + 40
                and player_y + HEIGHT_PLAYER > porta_y
            ):

                venceu = True
        
    if venceu:

        texto = fonte.render(
            "VOCE VENCEU!",
            True,
            "yellow"
        )

        texto2 = fonte.render(
            "Pressione R",
            True,
            "white"
        )

        screen.blit(
            texto,
            (220, 220)
        )

        screen.blit(
            texto2,
            (250, 290)
        )        
            

    pygame.display.update()

    clock.tick(60)

pygame.quit()   
