import pygame


class Audio:
    """ Classe com as informacoes dos audios do jogo. """
    def __init__(self, endereco, volume):
        self.audio = pygame.mixer.Sound(endereco)
        self.audio.set_volume(volume)

    def play(self):
        self.audio.play()
    def stop(self):
        self.audio.stop()