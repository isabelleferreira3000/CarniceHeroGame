import pygame
from pygame.locals import *
import delegation

class image:#classe de imagens feito para desenhar,escalar imagem,e cortar imagem
    def __init__(self,local,game):
        self.Local = local
        scale = game.getScale()
        self.Image = imageManager.scaleImage(pygame.image.load(local),(2.0*scale,2.0*scale)).convert_alpha()
        self.Rect =  self.Image.get_rect()
    def drawImage(self,pos = (0.0,0.0),game = None):
        rect = self.Rect
        image = self.Image
        game.addRect(game.getDisplay().blit(image, (int(pos[0] - rect.center[0]),int(pos[1] - rect.center[1]))))
        #game.getDisplay().blit(image, (int(pos[0] - rect.center[0]),int(pos[1] - rect.center[1])))
    def changeImage(self,image):
        self.Image = image
        self.Rect = self.Image.get_rect()
    def getImage(self):
        return self.Image
    def getRect(self):
        return self.Rect
    def getWidth(self):
        return self.Image.get_width()
    def getHeight(self):
        return self.Image.get_height()
    
class imageManager:
    
    def scaleImage(image ,scale = (1.0,1.0)):
        ScaledImage = pygame.transform.smoothscale(image,(int(scale[0]*image.get_width()),int(scale[1]*image.get_height())))
        return ScaledImage
    def cutImage(image ,shown = (1.0,1.0)):
        CutImage = pygame.transform.chop(image, (0.0, 0.0, shown[0]*image.get_width(), shown[1]*image.get_height()))
        return CutImage
    def drawImage(image , pos = (0.0,0.0),game = None):
        rect = image.get_rect()
        game.addRect(game.getDisplay().blit(image, (int(pos[0] - rect.center[0]),int(pos[1] - rect.center[1]))))
        #game.getDisplay().blit(image, (int(pos[0] - rect.center[0]),int(pos[1] - rect.center[1])))