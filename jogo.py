import pygame

class Tela:
    """ Classe com as informacoes do display do jogo. """
    def __init__(self, width, height, title):
        """ Inicializando um display com largura width, altura height e FPS frames por segundo. """
        self.width = width
        self.height = height
        self.title = title

    def IniciarTela(self):
        self.tela = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

class Cor:
    """ Classe com as cores utilizadas no jogo. """
    preto = (0, 0, 0)
    branco = (255, 255, 255)
    rosa = (255, 0, 169)
    amarelo = (255, 192, 0)

class Relogio:
    """ Classe com as informacoes do relogio do jogo. """
    def __init__(self, fps):
        """ Inicializando um relogio"""
        self.fps = fps
        self.relogio = pygame.time.Clock()

# class Apresentacao:
    # """ Classe com as notas da musica do jogo. """
    
    

def main():
    pygame.init()
    telaJogo = Tela(1240, 720, "CarniceHero")
    telaJogo.IniciarTela()
    corFundo = Cor()
    relogioJogo = Relogio(60)
    superficie = pygame.Surface((telaJogo.width-20, telaJogo.height-20))
    superficie.fill(corFundo.preto)

    sair = False
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
        relogioJogo.relogio.tick(relogioJogo.fps)
        telaJogo.tela.fill(corFundo.rosa)
        telaJogo.tela.blit(superficie, [10, 10])
        pygame.display.update()

    pygame.quit()


main()
