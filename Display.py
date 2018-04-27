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
        # clock = pygame.time.Clock()
        # background_surface = pygame.Surface((display_Width, display_Height))
        # background_surface.fill((0, 0, 0))
        # pygame.display.set_caption(Name)
        # global clock
        # clock = pygame.time.Clock()
        # global FPS
        # FPS = fps
        # return

def main():
    pygame.init()
    displayCarniceHero = Display(1240, 720, 60, "CarniceHero")
    displayCarniceHero.IniciarDisplay()


main()