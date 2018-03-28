import pygame

class Relogio:
    """ Classe com as informacoes do relogio do jogo. """
    def __init__(self, fps):
        self.fps = fps
        self.relogio = pygame.time.Clock()
