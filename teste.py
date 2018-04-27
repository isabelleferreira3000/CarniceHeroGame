import pygame

class Display:
    """ Classe com as informacoes do display do jogo. """
    def _init_(self, width, height, fps, title):
        """ Inicializando um display com largura width, altura height e FPS frames por segundo. """
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title

    def IniciarDisplay(self):
        pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

def main():
    pygame.init()
    displayCarniceHero = Display(1240, 720, 60, "CarniceHero")
    displayCarniceHero.IniciarDisplay()

    sair = False
    while sair != True:
        for event in pygame.event.get():
