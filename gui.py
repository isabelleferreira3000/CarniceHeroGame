import pygame,delegation,directoryManager,audioManager
from imageManager import *
pygame.font.init()
class Font:
    #font = "Arial"
    def __init__(self,font,size):
        self.font = font
        self.size = int(size)
    Default = pygame.font.SysFont("Verdana", 20)
    Small = pygame.font.SysFont("Verdana", 15)
    Medium = pygame.font.SysFont("Verdana", 40)
    Large = pygame.font.SysFont("Verdana", 60)
class Cor:
    """ Classe com as cores utilizadas no jogo. """
    preto = (0, 0, 0)
    branco = (255, 255, 255)
    rosa = (255, 0, 169)
    amarelo = (255, 192, 0)

class text:
    def __init__(self,text,color,size,x,y,game):
        self.text = text
        self.font = "Verdana"
        self.color = color
        scale = game.getScale()
        self.size = int(size)
        self.x = int(x*scale)
        self.y = int(y*scale)
        self.Font = pygame.font.SysFont(self.font, self.size)
        self.textRender = self.Font.render(self.text, True, self.color)
        self.on = False
        self.change = False
        if self.color == Cor.rosa:
            self.on = True
    def changeText(self,text):
        self.text = text
        self.textRender = self.Font.render(self.text, True, self.color)
    def render(self,game):
        if game.didReScale():
            scale = game.getNewScale()
            self.x = int(self.x*scale)
            self.y = int(self.y*scale)
            self.size = int(self.size*scale)
            self.Font = pygame.font.SysFont(self.font, self.size)
            self.textRender = self.Font.render(self.text, True, self.color)
        elif self.change:
            self.textRender = self.Font.render(self.text, True, self.color)
            self.change = False

        game.addRect(game.getDisplay().blit(self.textRender,(self.x - self.textRender.get_width()/2, 
            self.y - self.textRender.get_height()/2)))
    def getPosX(self):
        return self.x
    def getPosY(self):
        return self.y
    def position(self,x,y):
        self.x = x
        self.y = y
    def changeColor(self,color):
        self.color = color
    def setOn(self):
        self.on = (not self.on)
        self.change = True
        if self.on:
            self.color = Cor.rosa
        else:
            self.color = Cor.branco
    def getWidth(self):
        return self.textRender.get_width()
    def getHeight(self):
        return self.textRender.get_height()
    

class getAValueText(text):
    def __init__(self,text,color,size,x,y,game,scene,getValueFunction):
        self.nonWrittenText = text
        self.valueFunction = getValueFunction
        self.value = getValueFunction()
        text.__init__(self,text,color,size,x,y,game,scene)
    def setGetFunction(self,function):
        self.valueFunction = function
    def update(self,game):
        value = self.valueFunction()
        if not value == self.value:
            self.value = value
            self.changeText(self.nonWrittenText + str(self.value))
        self.render(game)
    def erase(self,game):
        game.removeRenderFunction(self.update)

class setValueText(text):
    def __init__(self,txt,color,size,x,y,game,value = ""):
        self.valueFunction = delegation.delegate()
        self.noValueFunction = delegation.delegate()
        if color== Cor.rosa:
            game.addEventFunction(self.event)
        self.value = value
        text.__init__(self,txt,color,size,x,y,game)
    def addValueFunction(self,function):
        self.valueFunction.add(function)
    def addNoValueFunction(self,function):
        self.noValueFunction.add(function)
    def setValue(self,value):
        self.value = value
    def getValue(self):
        return self.value
    def do(self):
        self.valueFunction.call(self.value)
        self.noValueFunction.call()
    def update(self,game):
        self.render(game)
    def erase(self,game):
        game.removeRenderFunction(self.render)
    def event(self,game):
        evnt = game.getEventList()
        for event in evnt:
            i = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.do()

class setChangeValueText(text):
    def __init__(self,text,color,size,x,y,game,value,minValue,maxValue):
        self.nonWrittenText = text
        self.valueFunction = delegation.delegate()
        self.noValueFunction = delegation.delegate()
        self.value = value
        self.min = minValue
        self.max = maxValue
        self.changedValue = False

        text.__init__(self,text + str(self.value),color,size,x,y,game)
    def addValueFunction(self,function):
        self.valueFunction.add(function)
    def addNoValueFunction(self,function):
        self.noValueFunction.add(function)
    def setValue(self,value):
        self.value = value
    def getValue(self):
        return self.value
    def do(self,game):
        self.valueFunction.call(self.value)
        self.noValueFunction.call()
    def update(self,game):
        if self.changedValue:
            self.changedValue = False
            self.changeText(self.nonWrittenText + str(self.value))
        self.render(game)
    def erase(self,game):
        game.removeRenderFunction(self.render)
    def event(self,game):
        evnt = game.getEventList()
        for event in evnt:
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.value -= 1
                        if self.value < self.min:
                            self.value = self.max
                        self.changedValue = True
                        self.do(game)
                    elif event.key == pygame.K_RIGHT:
                        self.value += 1
                        if self.value > self.max:
                            self.value = self.min
                        self.changedValue = True
                        self.do(game)

        






class toggle:
    def __init__(self,toggleImage,toggleOk,toggleText,size,x,y,game):
        self.toggle = image(toggleImage,game)
        self.ok = image(toggleOk,game)
        self.text = text(toggleText,Cor.branco,size,x,y,game)
        self.on = False
        scale = game.getScale()
        self.onOk = False
        self.do = delegation.delegate()
    def update(self,game):
        if game.didReScale():
                scale = game.getNewScale()
                self.toggle.changeImage(imageManager.scaleImage(self.toggle.getImage(),(scale,scale)))
                if self.onOk:
                    self.ok.changeImage(imageManager.scaleImage(self.ok.getImage(),(scale,scale)))
        self.text.render(game)
        self.toggle.drawImage((self.x + self.text.getWidth()*0.55,self.y),game)
        if self.onOk:
            self.ok.drawImage((self.x + self.text.getWidth()*0.55,self.y),game)
    def setOn(self):
        self.on = (not self.on)
        self.text.setOn()
    def addDo(self,func):
        self.do.add(func)
    def isDo(self):
        if self.do.isEmpty():
            return False
        return True
    def callDo(self):
        if self.isDo():
            self.do.call()
    def event(self,game):
        evnt = game.getEventList()
        if self.on:
            for event in evnt:
                i = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.callDo()


class menu:
    def __init__(self,game,img,x,y):
        self.game = game
        directory = directoryManager.directoryManager()
        self.sound = audioManager.sound(directory.getAudio() +"/note_erro.ogg",0)
        if img == "":
            self.image = image(img,game)
            self.image.changeImage(pygame.Surface((game.getDisplayWidth(),game.getDisplayHeight())))
        else:
            self.image = image(img,game)
        
        self.x = x
        self.y = y
        self.title = []
        self.previewsMenu = None
        self.list = []#index 0 é a funcionalidade,pode ser text,slide.O dois é o que ela faz
        self.i = 0
        self.lastIndex = -1
        self.firstIndex = 0
        self.textRender = 0
        self.on = False
    def setOn(self,game):
        if self.on:
            self.on = False
            game.removeRenderFunction(self.render)
        else:
            self.on = True
            game.addRenderFunction(self.render)
    def addTitle(self,titleText):
        n = len(self.title)-1
        if n >= 0:
            y = self.title[n].getPosY() + 0.55*self.title[n].getHeight() + 0.55*titleText.getHeight()
            titleText.position(titleText.getPosX(),y)
        
        
        self.title.append(titleText)
    def renderTitle(self,game):
        for x in self.title:
            x.render(game)
    def eventMenu(self,game):
        
        evnt = game.getEventList()
        for event in evnt:
            i = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.sound.play()
                    self.list[self.i].setOn()
                    bIndex = self.firstIndex
                    lIndex = self.lastIndex
                    game.removeEventFunction(self.list[self.i].event)
                    n = len(self.list)
                    self.i -= 1
                    if self.i == bIndex-1:
                        if self.i < 0:
                           self.i = n - 1 
                        if n > 4:
                            self.firstIndex = self.i
                            bIndex = self.i
                            self.lastIndex -= 1
                            self.on = False
                            if self.lastIndex < 0:
                                self.lastIndex = n - 1
                            lIndex = self.lastIndex

                    elif self.i < 0:
                        self.i = n-1
                        #self.firstIndex = self.i
                    game.addEventFunction(self.list[self.i].event)
                    self.list[self.i].setOn()
                    n = len(self.title) - 1
                    y = self.title[n].getPosY() + self.title[n].getHeight()*2
                    if y > (game.getDisplayHeight()*0.4):
                        y = game.getDisplayHeight()*0.4
                    n = len(self.list)-1
                    
                    while not bIndex==lIndex:
                        y += self.list[bIndex].getHeight()*0.55
                        self.list[bIndex].position(self.list[bIndex].getPosX(),y)
                        y = self.list[bIndex].getPosY() + self.list[bIndex].getHeight()*0.55
                        bIndex += 1
                        if bIndex > n:
                            bIndex = 0
                    y += self.list[bIndex].getHeight()*0.55
                    self.list[bIndex].position(self.list[bIndex].getPosX(),y)
                        

                elif event.key == pygame.K_DOWN:
                    self.sound.play()
                    self.list[self.i].setOn()
                    game.removeEventFunction(self.list[self.i].event)
                    n = len(self.list)
                    bIndex = self.firstIndex
                    lIndex = self.lastIndex
                    variacao = 0
                    self.i += 1
                    if self.i == lIndex+1:
                        if self.i >= n:
                           self.i = 0 
                        if n > 4:
                            self.on = False
                            self.lastIndex = self.i
                            lIndex = self.lastIndex
                            self.firstIndex += 1
                            if self.firstIndex >= n:
                                self.firstIndex = 0
                            bIndex = self.firstIndex

                    elif self.i >= n:
                        self.i = 0
                    elif (event.key == pygame.K_RIGHT or event.key == pygame.K_RETURN) or event.key == pygame.K_LEFT:
                        self.sound.play()
                        #self.firstIndex = self.i
                    
                    game.addEventFunction(self.list[self.i].event)
                    self.list[self.i].setOn()
                    n = len(self.title) - 1
                    y = self.title[n].getPosY() + self.title[n].getHeight()*2
                    if y > (game.getDisplayHeight()*0.4):
                        y = game.getDisplayHeight()*0.4
                    n = len(self.list) - 1
                    bIndex = self.firstIndex
                    lIndex = self.lastIndex
                    while not bIndex==lIndex:
                        y += self.list[bIndex].getHeight()*0.55
                        self.list[bIndex].position(self.list[bIndex].getPosX(),y)
                        y = self.list[bIndex].getPosY() + self.list[bIndex].getHeight()*0.55
                        bIndex += 1
                        if bIndex > n:
                            bIndex = 0
                    y += self.list[bIndex].getHeight()*0.55
                    self.list[bIndex].position(self.list[bIndex].getPosX(),y)
                    
            print(self.i)

            """elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    game.setScaleTime(0)
                elif event.key == pygame.K_DOWN:
                    game.setScaleTime(0)"""
    def addPreviewsMenu(self,menu):
        self.previewsMenu = menu
    def render(self,game):
        if game.didReScale():
            scale = game.getNewScale()
            self.x = int(self.x*scale)
            self.y = int(self.y*scale)
            self.image.changeImage(imageManager.scaleImage(self.image.getImage(),(scale,scale)))
            self.image.drawImage((self.x,self.y),game)
        elif not self.on:
            self.image.drawImage((self.x,self.y),game)
            self.on = True
        else:
            self.image.drawAsStatic((self.x,self.y),game)
        self.renderTitle(game)
        n = len(self.list)
        if n == 0:
            return
        bIndex = self.firstIndex
        lIndex = self.lastIndex
        i = 4
        if i >= n:
            i = n - 1
        while not bIndex==lIndex:
            self.list[bIndex].update(game)
            bIndex += 1
            i -= 1
            if bIndex >= n:
                bIndex = 0
        self.list[bIndex].update(game)


    """def callPreviewsMenu(self,menu):
        self.game.removeRenderFunction(self.render)
        if not self.previewsMenu == None
            self.game.addRenderFunction(self.previewsMenu.render(),self.game.getLayer() + 1)
        self = self.previewsMenu"""
    #def menuOn(self):
        #add renders
    def addFunction(self,function):
        game = self.game
        if self.lastIndex < 4:
            self.lastIndex += 1
        n = len(self.list) - 1
        if  n >= 0:
            y = self.list[n].getPosY() + self.list[n].getHeight()*0.55 + function.getHeight()*0.55
            function.position(function.getPosX(),y)
            self.list.append(function)
        else:
            n = len(self.title)-1
            y = self.title[n].getPosY() + self.title[n].getHeight()*2
            if y > (game.getDisplayHeight()*0.4):
                y = game.getDisplayHeight()*0.4
            y += function.getHeight()*0.55
            function.position(function.getPosX(),y)
            self.list.append(function)


        
