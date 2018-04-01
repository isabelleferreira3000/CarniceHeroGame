import pygame
from pygame.locals import *
import delegation

class gameStateManager:#classe para gerenciar o estado do jogo,como display,fps,se esta em pause entre outras coisas
    def __init__(self,width = 1240,height = 720,fps = 60,scene = 'mainMenu',icon = None,gameName = "Carnice Hero"):
        self.background_surface = pygame.Surface((width, height))
        self.background_surface.fill((0, 0, 0))
        self.nonFullWidth = 0
        self.nonFullHeight = 0
        self.width = width
        self.height = height
        self.baseWidth = width
        self.baseHeight = height
        self.deltaTime = 0
        self.gameExit = False
        self.fps = fps
        self.frame = 0
        self.scene = scene
        self.gameName = gameName
        self.time = 0#variavel de tempo
        self.delayTime = 4.0#diferença de tempo onde começa a ver as notas, para poder pressiona-las
        self.onPause = False
        self.display = pygame.display.set_mode((self.width, self.height),HWSURFACE|DOUBLEBUF|RESIZABLE)
        #self.display = pygame.display.set_mode((self.width, self.height),RESIZABLE)
        self.clock = pygame.time.Clock()
        self.fullScreen = False
        self.icon = icon
        self.renderList = [delegation.delegate()]#quando chamada vai renderizar todas as layers da 0(background)#delegation.delegate
        self.eventList = delegation.delegate()
        self.eventList.add(self.resizeEvent)
        #até o ultimo da lista
        self.lastFrameRect = []
        self.frameRect = []
        self.event = self.getEvent()
        self.reScaled = False
        self.scale = 1.0#Escala em relação a preferencial
        self.newScale = 1.0
        pygame.display.set_caption(self.gameName)
        #pygame.image.load('local')
        #pygame.display.set_icon(pygame.image.load('local'))
    def changeDisplay(self,Width,Height):
        w = self.width
        h = self.height
        self.reScaled = True
        self.width = Width
        self.height = Height
        if w > self.width or h > self.height:
            scale = self.width/w
            if scale > self.height/h:
                scale = self.height/h
        if w < self.width or h < self.height:
            scale = self.width/w
            if scale < self.height/h:
                scale = self.height/h
        self.newScale = scale
        self.scale = self.scale*scale
        self.display = pygame.display.set_mode((self.width, self.height),HWSURFACE|DOUBLEBUF|RESIZABLE)
        self.background_surface = pygame.Surface((self.width, self.height))
        self.background_surface.fill((0, 0, 0))
        #self.display = pygame.display.set_mode((self.width, self.height))
    def resizeEvent(self,game):
        for evt in game.event:
            if evt.type==VIDEORESIZE:
                size = evt.dict['size']
                game.changeDisplay(size[0],size[1])

                del evt

    def didReScale(self):
        return self.reScaled
    def getDisplay(self):
        return self.display
    def changeScene(self,newScene):
        self.scene = newScene
    def getScene(self):
        return self.scene
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def getTime(self):
        return self.time
    def getDeltaTime(self):
        return self.deltaTime
    def getDelayTime(self):
        return self.delayTime
    def getScale(self):
        return self.scale
    def getNewScale(self):
        return self.newScale
    def restartTime(self):
        self.time = 0
    def changeFps(self,FPS):
        self.fps = FPS
    def pause(self):
        self.onPause = True
    def waitFrame(self):#espera um determinado tempo(1/fps)
        return self.clock.tick(self.fps)/1000
    def getEvent(self):
        return pygame.event.get()
    def getEventList(self):
        return self.event
    def quit(self):
        pygame.quit()
    def toFullScreen(self):
        if not self.fullScreen:
            self.nonFullHeight = self.height
            self.nonFullWidth = self.width
            pygame.display.toggle_fullscreen()
            self.fullScreen = True
    def notFullScreen(self):
        if self.fullScreen:
            self.height = self.nonFullHeight
            self.width = self.nonFullWidth
            pygame.display.toggle_fullscreen()
            self.fullScreen = False
    def setIcon(self,local):
        self.icon = local
        if pygame.image.load('local'):
            pygame.display.set_icon(pygame.image.load('local'))

    #se o layer for acima do layer do renderList, vai sempre adcionar apenas uma acima,ou seja a ordem que vc adciona importa
    def addRenderFunction(self,renderFunction,layer):
        if layer >= len(self.renderList):
            layer = len(self.renderList)
            if layer == 0:
                self.renderList = [delegation.delegate()]
            else:
                self.renderList.append(delegation.delegate())
        self.renderList[layer].add(renderFunction)
    def removeRenderFunction(self,renderFunction):
        for func in self.renderList:
            func.remove(renderFunction)
            if func.isEmpty():
                del func
            if not self.renderList[0]:
                self.renderList = [delegation.delegate()]
    def removeAllRender(self):
        self.renderList = [delegation.delegate()]
    def blitRender(self):
        self.frameRect = []
        for listRender in self.renderList:
            listRender.call(self)
    def addRect(self,rect):
        self.frameRect.append(rect)
    def render(self):
        self.background_surface
        self.display.blit(self.background_surface,(0,0))
        self.blitRender()
        v = self.lastFrameRect + self.frameRect
        if self.didReScale():
            pygame.display.flip()
        else:
            pygame.display.update(v)
        #pygame.display.flip()
        self.lastFrameRect = [] + self.frameRect
    def addEventFunction(self,eventFunction):
        self.eventList.add(eventFunction)
    def removeEventFunction(self,eventFunction):
        self.eventList.remove(eventFunction)
    def removeAllEventFunction(self):
        self.eventList = delegation.delegate()
    def setEvent(self):
        self.eventList.call(self)
    def getGameExit(self):
        return self.gameExit
    def setGameExit(self):
        self.gameExit = True
    def update(self):
        dt = self.waitFrame()
        self.deltaTime = dt
        #print('flag' + str(flag))
        
        self.event = self.getEvent()
        for event in self.event:
            if event.type == pygame.QUIT:
                self.gameExit = True
            #elif event.type == pygame.MOUSEBUTTONDOWN:
            #   if event.button == 1: #botão esquerdo
                   #eventos de cick de botão 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.onPause:
                        self.onPause = False
                    elif not self.onPause:
                        self.onPause = True
        self.setEvent()
        #elif event.type == pygame.KEYUP:
             #   break
        #flag = 5
        #print('flag' + str(flag))
        #drawScene()
        #pressNotes.events(evt)
        #flag = 6
        #print('flag' + str(flag))
        self.render()
        if self.onPause == False:
            self.frame = self.frame + 1
            self.time = self.time + dt
            if self.frame % 120 == 0:
                print(self.time)
                print("Frame: " + " " + str(self.frame))
        if self.reScaled:
            self.reScaled = False

