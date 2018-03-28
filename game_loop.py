import pygame
from tela import Tela
from relogio import Relogio


class Loop:

    def game_loop(self):

        pygame.init()
        tela_loop_do_jogo = Tela(620, 360, "CarniceHero", "planoFundo.jpg")

        relogio_jogo = Relogio(60)

        fechar_jogo = False
        pause = False
        in_loop = True
        while in_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fechar_jogo = True
                    in_loop = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == 13:
                        pause = True
                        print("pause")
                #    if event.key == pygame.K_s:
                #    if event.key == pygame.K_d:
                #    if event.key == pygame.K_k:
                #    if event.key == pygame.K_l:

            tela_loop_do_jogo.tela.blit(tela_loop_do_jogo.imagemFundo, (0, 0))
            relogio_jogo.relogio.tick(relogio_jogo.fps)
            pygame.display.update()

        if fechar_jogo:
            return "fechar_jogo"

# game = Loop()
# print(game.game_loop())
