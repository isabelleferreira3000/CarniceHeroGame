import pygame
from tela import Tela
from relogio import Relogio
from audio import Audio


class Dificuldade:

    def game_dificuldade(self):

        pygame.init()
        tela_dificuldade_normal = Tela(620, 360, "CarniceHero", "dificuldade_normal.jpg")
        tela_dificuldade_dificil = Tela(620, 360, "CarniceHero", "dificuldade_dificil.jpg")
        audio_menu_navigate = Audio("menu_navigate_0.wav", 1)

        relogio_jogo = Relogio(60)

        fechar_jogo = False
        voltar = False
        tela_dificuldade = "dificuldade_normal"
        dificuldade = True
        while dificuldade:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fechar_jogo = True
                    dificuldade = False

                elif event.type == pygame.KEYDOWN:
                    audio_menu_navigate.audio.play()
                    if tela_dificuldade == "dificuldade_normal":
                        if event.key == pygame.K_DOWN:
                            tela_dificuldade = "dificuldade_dificil"
                        elif event.key == pygame.K_UP:
                            tela_dificuldade = "dificuldade_dificil"

                    elif tela_dificuldade == "dificuldade_dificil":
                        if event.key == pygame.K_DOWN:
                            tela_dificuldade = "dificuldade_normal"
                        elif event.key == pygame.K_UP:
                            tela_dificuldade = "dificuldade_normal"

                    if event.key == 13: # 13 == botao ENTER:
                        dificuldade = False
                    elif event.key == pygame.K_BACKSPACE:
                        voltar = True
                        dificuldade = False

            if tela_dificuldade == "dificuldade_normal":
                tela_dificuldade_normal.tela.blit(tela_dificuldade_normal.imagemFundo, (0, 0))
            elif tela_dificuldade == "dificuldade_dificil":
                tela_dificuldade_dificil.tela.blit(tela_dificuldade_dificil.imagemFundo, (0, 0))

            relogio_jogo.relogio.tick(relogio_jogo.fps)
            pygame.display.update()

        if fechar_jogo:
            return "fechar_jogo"
        elif voltar:
            return "voltar"
        else:
            return tela_dificuldade

# dificuldade = Dificuldade()
# print(dificuldade.game_dificuldade())