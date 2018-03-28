import pygame
from tela import Tela
from relogio import Relogio
from audio import Audio


class Menu:

    def game_menu(self):

        pygame.init()
        tela_menu_iniciar = Tela(620, 360, "CarniceHero", "menu_iniciar.jpg")
        tela_menu_dificuldade = Tela(620, 360, "CarniceHero", "menu_dificuldade.jpg")
        tela_menu_creditos = Tela(620, 360, "CarniceHero", "menu_creditos.jpg")
        audio_menu_navigate = Audio("menu_navigate_0.wav", 1)

        relogio_jogo = Relogio(60)

        fechar_jogo = False
        tela_menu = "menu_iniciar"
        menu = True
        while menu:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    fechar_jogo = True
                    menu = False

                elif event.type == pygame.KEYDOWN:
                    audio_menu_navigate.audio.play()
                    if event.key == 13: # 13 == botao ENTER:
                        menu = False

                    elif tela_menu == "menu_iniciar":
                        if event.key == pygame.K_DOWN:
                            tela_menu = "menu_dificuldade"
                        elif event.key == pygame.K_UP:
                            tela_menu = "menu_creditos"

                    elif tela_menu == "menu_dificuldade":
                        if event.key == pygame.K_DOWN:
                            tela_menu = "menu_creditos"
                        elif event.key == pygame.K_UP:
                            tela_menu = "menu_iniciar"

                    elif tela_menu == "menu_creditos":
                        if event.key == pygame.K_DOWN:
                            tela_menu = "menu_iniciar"
                        elif event.key == pygame.K_UP:
                            tela_menu = "menu_dificuldade"

            if tela_menu == "menu_iniciar":
                tela_menu_iniciar.tela.blit(tela_menu_iniciar.imagemFundo, (0, 0))
            elif tela_menu == "menu_dificuldade":
                tela_menu_dificuldade.tela.blit(tela_menu_dificuldade.imagemFundo, (0, 0))
            elif tela_menu == "menu_creditos":
                tela_menu_creditos.tela.blit(tela_menu_creditos.imagemFundo, (0, 0))

            relogio_jogo.relogio.tick(relogio_jogo.fps)
            pygame.display.update()

        if fechar_jogo:
            return "fechar_jogo"
        else:
            return tela_menu

# tela_menu = Menu()
# print(tela_menu.game_menu())