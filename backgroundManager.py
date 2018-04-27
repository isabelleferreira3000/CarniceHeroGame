from imageManager import *
import gui

class background:
    def __init__(self,imgDir,game):
        self.img = image(imgDir,game)
        self.on = False
    def setOn(self):
        if self.on:
            self.on = False
    def render(self,game):
        if game.didReScale() :
            scale = game.getNewScale()
            self.img.changeImage(imageManager.scaleImage(self.img.getImage(),(scale,scale)))
            self.img.drawImage(((game.getDisplayWidth()>>1),(game.getDisplayHeight()>>1)),game)
        elif not self.on:
            scale = game.getScale()
            self.img.changeImage(imageManager.scaleImage(self.img.getImage(),(scale,scale)))
            self.img.drawImage(((game.getDisplayWidth()>>1),(game.getDisplayHeight()>>1)),game)
            self.on = True
        else:
            self.img.drawAsStatic(((game.getDisplayWidth()>>1),(game.getDisplayHeight()>>1)),game)