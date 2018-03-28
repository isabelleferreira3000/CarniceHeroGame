import pygame
from tela import Tela
from relogio import Relogio
from audio import Audio


class Creditos:

    def game_creditos(self):

        pygame.init()
        tela_creditos = Tela(620, 360, "CarniceHero", "creditos.jpg")
        audio_menu_navigate = Audio("menu_navigate_0.wav", 1)

        relogio_jogo = Relogio(60)

        fechar_jogo = False
        creditos = True
        voltar = False
        while creditos:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fechar_jogo = True
                    creditos = False

                elif event.type == pygame.KEYDOWN:
                    audio_menu_navigate.audio.play()
                    if event.key == pygame.K_BACKSPACE:
                        voltar = True
                        creditos = False

            tela_creditos.tela.blit(tela_creditos.imagemFundo, (0, 0))

            relogio_jogo.relogio.tick(relogio_jogo.fps)
            pygame.display.update()

        if fechar_jogo:
            return "fechar_jogo"
        elif voltar:
            return "voltar"


# tela = Creditos()
# print(tela.game_creditos())