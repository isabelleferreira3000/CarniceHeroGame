import pygame
from pygame.locals import *
import delegation
from imageManager import *
class imageNotes:#classe da lista de botões para instanciar as notas, sem ter que armazenar em todos as notas da tela
    def __init__(self,game):
        self.display_Height = game.getHeight()
        self.display_Width = game.getWidth()
        self.noteList = ([],[],[],[],[])#aqui tem a lista dos tempos que cada nota devera ser pressionada
        self.indexButtonDraw = [0,0,0,0,0]#diz qual é o index da ultima nota a ser desenhada,para não ter que percorrer toda a buttonList

    def loadImages(self,game,local):
        self.Images = []
        i = 0
        for loc in local:
            self.Images.append(image(loc,game))
            i = i + 1
        self.i = i #numero de imagens armazenadas na variavel
    def isometricPositionDraw(self,index,timeNote,game):#transforma a imagem dependendo da posição em que ela aparece,para se mostrar uma vista isometrica,para desenha-la
        iniRatio = 0.20
        lastRatio = 0.95
        showNoteTime = 0.2
        #initialPosY = iniRatio*globalVar.display_Height
        #lastPosY = lastRatio*globalVar.display_Height
        Time = game.getTime()
        delayTime = game.getDelayTime()
        
        r = (Time - timeNote - delayTime)
        if(r <= 0.0):
            return
        #print("r é " + str(r))
        posY0 = iniRatio*self.display_Height
        ratio = (r*(lastRatio-iniRatio)/delayTime + iniRatio)/lastRatio
        image = imageManager.scaleImage(self.Images[index].Image,(ratio,ratio))
        posY = ratio*self.display_Height

        posX = self.display_Width/2 + 1.5*(index-2)*image.get_width()
        dy = image.get_height()/2
        if(posY - posY0 < dy):
            
            image = imageManager.cutImage(image,(0.0,r/showNoteTime))
            dy = dy - image.get_height()/2
            imageManager.drawImage(image,(posX,posY + int(dy)),game)
            return
        imageManager.drawImage(image,(posX,posY),game)
    def updateNotes(self,game):
        buttonList = self.noteList
        indexButtonDraw = self.indexButtonDraw
        Time = game.getTime()
        delayTime = game.getDelayTime()
        Notes = self
        if game.didReScale():
                self.display_Height = game.getHeight()
                self.display_Width = game.getWidth()
                for img in self.Images:
                    scale = game.getNewScale()
                    img.changeImage(imageManager.scaleImage(img.getImage(),(scale,scale)))

        display_Width = self.display_Width
        #global pressNotes
        i = Notes.i - 1
        while i >= 0:
            if buttonList[i]:
                if Time - buttonList[i][0] - delayTime > 1.2*delayTime:
                    del buttonList[i][0]
                    indexButtonDraw[i] = indexButtonDraw[i] - 1
            i = i - 1
        i = Notes.i - 1
        #leftLine = display_Width/2 - 2*45
        #flag = 2
        #print('flag' + str(flag))
        #pressNotes.drawPlayNotes()
        while i >= 0:
            j = indexButtonDraw[i]
            if buttonList[i]:
                n = len(buttonList[i]) - j
                while n > 0:
                    if buttonList[i][j] - Time > delayTime:
                        break
                    j = j + 1
                    n = n - 1
                    indexButtonDraw[i] = j
            while j > 0:
                j = j - 1
                #drawButton(color,(leftLine + i*45,(Time - buttonList[i][j] - deltaTime )*globalVar.display_Height/deltaTime))
                Notes.isometricPositionDraw(i,buttonList[i][j],game)
            i = i-1
        #flag = 3
        #print('flag' + str(flag)) 


class playNote():
    def __init__(self,nomallocal,pressDir,rightDir,game,Notes):
        display_Height = game.getHeight()
        display_Width = game.getWidth()
        self.posY = 0.95*display_Height
        self.posX = []
        self.notes = Notes

        
        self.Images = []#imagem a ser desenhada
        self.NormalStateImage = []#imagem a ser desenhada quando os botões para pressionar as notas não forem ativados
        self.pressedImages = []#imagem a ser ativada quando os botões forem ativados e errarem
        self.rightImages = []#imagem a ser ativada quando as notas forem pressionadas corretamente
        i = 0
        for loc in nomallocal:
            self.NormalStateImage.append(image(loc,game))
            self.Images.append(image(loc,game))
            i = i + 1
        for loc in pressDir:
            self.pressedImages.append(image(loc,game))
        for loc in rightDir:
            self.rightImages.append(image(loc,game))
        self.i = i #numero de imagens armazenadas na variavel
        for i in range(0,5):
            self.posX.append(display_Width/2 + 1.5*(i-2)*self.Images[i].getWidth())
    def notePressed(self,i,game):
        buttonList = self.notes.noteList
        deltaTime = game.getDelayTime()
        time = game.getTime()
        imprecisionTimeUp = 0.3#intervalo de tempo em que o jogador pode ser impreciso
        imprecisionTimeDown = 0.05#intervalo de tempo em que o jogador pode ser impreciso
        indexButtonDraw = self.notes.indexButtonDraw
        if i == -1 :
            return
        if not buttonList[i]:
            self.Images[i] = self.pressedImages[i]
            return

        t = time - buttonList[i][0] - 2*deltaTime
        t = imprecisionTimeDown*2#garante que entra no porximo loop
        n = indexButtonDraw[i]
        j = -1
        while t >= imprecisionTimeDown and  j < n:
            j = j + 1
            t = time - buttonList[i][j] - 2*deltaTime
        if t < imprecisionTimeDown and t > -imprecisionTimeUp:
            self.Images[i] =  self.rightImages[i]#troca a imagem a ser desenhada
            del buttonList[i][j]
            indexButtonDraw[i] = indexButtonDraw[i] - 1
            print('adcionar pontos')#adciona os pontos por ter acertado a nota
        else:
            self.Images[i] = self.pressedImages[i]
            print('Ativa o som do erro')#Ativa o som do erro
    def noteUnpress(self,i):
        if i == -1:
            return
        self.Images[i] =  self.NormalStateImage[i]
        print('desativa nota')

    def drawPlayNotes(self,game):
        i = 0
        if game.didReScale():
            display_Height = game.getHeight()
            display_Width = game.getWidth()
            self.posY = 0.95*display_Height
            self.posX = []
            Notes = self.notes

            for i in range(0,5):
                scale = game.getNewScale()
                img = self.Images[i]
                self.Images[i].changeImage(imageManager.scaleImage(img.getImage(),(scale,scale)))
                img = self.NormalStateImage[i]
                self.NormalStateImage[i].changeImage(imageManager.scaleImage(img.getImage(),(scale,scale)))
                img = self.pressedImages[i]
                self.pressedImages[i].changeImage(imageManager.scaleImage(img.getImage(),(scale,scale)))
                img = self.rightImages[i]
                self.rightImages[i].changeImage(imageManager.scaleImage(img.getImage(),(scale,scale)))
                self.posX.append(display_Width/2 + 1.5*(i-2)*self.Images[i].getWidth())
                

        while i < 5:
            pos = (self.posX[i],self.posY)
            imageManager.drawImage(self.Images[i].getImage(),(self.posX[i],self.posY),game)
            i = i + 1

    def events(self,game):
        evt = game.getEventList()
        Time = game.getTime()
        i = 0
        for event in evt:
            i = - 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    i = 0
                elif event.key == pygame.K_s:
                    i = 1
                elif event.key == pygame.K_d:
                    i = 2
                elif event.key == pygame.K_j:
                    i = 3
                elif event.key == pygame.K_k:
                    i = 4
                self.notePressed(i,game)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    i = 0
                elif event.key == pygame.K_s:
                    i = 1
                elif event.key == pygame.K_d:
                    i = 2
                elif event.key == pygame.K_j:
                    i = 3
                elif event.key == pygame.K_k:
                    i = 4
                self.noteUnpress(i)
