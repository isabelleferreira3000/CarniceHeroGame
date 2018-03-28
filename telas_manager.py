import pygame
from menu import Menu
from dificuldade import Dificuldade
from creditos import Creditos
from game_loop import Loop
from audio import Audio


def game_telas_manager():

    pygame.init()

    tela_menu = Menu()
    tela_dificuldade = Dificuldade()
    tela_creditos = Creditos()
    tela_loop = Loop()

    audio_comeco_jogo = Audio("pickup_3.wav", 0.5)
    audio_menu_fundo = Audio("garotadeipanema.ogg", 0.5)
    audio_menu_fundo.audio.play()

    decisao_menu = "tomar_decisao"
    fechar_jogo = False
    in_loop = True
    while in_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fechar_jogo = True
                in_loop = False

        if decisao_menu == "tomar_decisao":
            decisao_menu = tela_menu.game_menu()

        elif decisao_menu == "fechar_jogo":
            fechar_jogo = True
            in_loop = False

        elif decisao_menu == "menu_iniciar":
            audio_comeco_jogo.audio.play()
            audio_menu_fundo.audio.stop()
            retorno_tela_loop = tela_loop.game_loop()
            if retorno_tela_loop == "fechar_jogo":
                fechar_jogo = True
                in_loop = False

        elif decisao_menu == "menu_dificuldade":
            retorno_tela_dificuldade = tela_dificuldade.game_dificuldade()
            if retorno_tela_dificuldade == "fechar_jogo":
                fechar_jogo = True
                in_loop = False
            elif retorno_tela_dificuldade == "voltar":
                decisao_menu = "tomar_decisao"
            elif retorno_tela_dificuldade == "dificuldade_normal":
                decisao_menu = "menu_iniciar"
            elif retorno_tela_dificuldade == "dificuldade_dificil":
                decisao_menu = "menu_iniciar"

        elif decisao_menu == "menu_creditos":
            retorno_tela_creditos = tela_creditos.game_creditos()
            if retorno_tela_creditos == "fechar_jogo":
                fechar_jogo = True
                in_loop = False
            elif retorno_tela_creditos == "voltar":
                decisao_menu = "tomar_decisao"

    if fechar_jogo:
        return "fechar_jogo"


game_telas_manager()