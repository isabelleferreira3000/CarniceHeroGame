import pygame
from imagem import Imagem


class Rafa(Imagem):
    def __init__(self, tela_loop_do_jogo, endereco_imagem):
        rafa_size = int(tela_loop_do_jogo.altura / 3)
        # posicao =
        super(Rafa, self).__init__(rafa_size, rafa_size,
                                   endereco_imagem,
                                   (int(tela_loop_do_jogo.largura / 2 - (int(tela_loop_do_jogo.altura / 3)) / 2),
                                    int(0.4 * tela_loop_do_jogo.altura - 0.94 * (int(tela_loop_do_jogo.altura / 3)))))

# class Rafa(Imagem):
#     def __init__(self, largura, altura, endereco_imagem, posicao):
#         super(Rafa, self).__init__(largura, altura, endereco_imagem, posicao)
#         self.size = int(tela_loop_do_jogo.altura / 3)
#         self.posicao = (int(tela_loop_do_jogo.largura / 2 - self.size / 2),
#                         int(0.4 * tela_loop_do_jogo.altura - 0.94 * self.size))
