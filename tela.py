import pygame

class Tela:
    """ Classe com as informacoes do display do jogo. """
    def __init__(self, largura, altura, titulo, enderecoImagemFundo):
        self.largura = largura
        self.altura = altura
        self.titulo = titulo
        self.imagemFundo = pygame.image.load(enderecoImagemFundo)
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption(self.titulo) 
