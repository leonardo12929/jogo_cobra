import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

fundo = pygame.image.load('grama.png')

colisao = pygame.mixer.Sound('smw_stomp_no_damage.wav')
colisao2 = pygame.mixer.Sound('smw_swimming.wav')

LARGURA = 640
ALTURA = 480
x_cobra = int(LARGURA / 2)
y_cobra = int(ALTURA / 2)

velocidade = 0.9
x_controle = velocidade
y_controle = 0

x_maca = randint(40,600)
y_maca = randint(50,430)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("leozinho")   

    
lista_cobra = []
comprimento_inicial = 5
morreu = False

def Morreu():
    fonte2 = pygame.font.SysFont('arial',20,True,True)
    mensagem = 'Game over! R para reiniciar'
    texto_formatado = fonte2.render(mensagem, True, (0,0,0))
    morreu = True
    while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
                        return
            tela.blit(texto_formatado,(200,200))
            pygame.display.update()

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela,(0,176,240),(XeY[0], XeY[1],20,20))

def reiniciar_jogo():
    global  comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca , morreu
    comprimento_inicial = 5
    x_cobra = int(LARGURA / 2)
    y_cobra = int(ALTURA / 2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40,600)
    y_maca = randint(50,430) 
    morreu = False   

while True:
    tela.fill((255,255,255))
    tela.blit(fundo,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
    x_cobra += x_controle
    y_cobra += y_controle
    cobra = pygame.draw.rect(tela,(0, 0, 255), (x_cobra,y_cobra, 20,20))
    maca = pygame.Rect(x_maca, y_maca, 20, 20)
    pygame.draw.circle(tela, (255, 0, 0), maca.center, 10)
    
    if cobra.colliderect(maca):
        x_maca = randint(40,600)
        y_maca = randint(50,430)
        colisao2.play()
        comprimento_inicial += 1000
    lista_cabeca = []   
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)
    
    if lista_cobra.count(lista_cabeca ) > 1:
        colisao.play()
        Morreu()


    if x_cobra > LARGURA:
        colisao.play()
        Morreu()
    if x_cobra < 0:
        colisao.play()
        Morreu()
    if y_cobra < 0:
        colisao.play()
        Morreu()
    if y_cobra > ALTURA:
        colisao.play()
        Morreu()
        
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)
    pygame.display.update()