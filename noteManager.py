import pygame
from pygame.locals import *
import delegation
from imageManager import *
import audioManager
import directoryManager, databaseManager,gamePointsManager,backgroundManager,gui

class imageNotes:#classe da lista de botões para instanciar as notas, sem ter que armazenar em todos as notas da tela
    def __init__(self,game):
        self.inMakeLevel = False
        self.inDeleteMode = False
        self.display_Height = game.getHeight()
        self.display_Width = game.getWidth()
        self.noteList = []#aqui tem a lista dos tempos que cada nota devera ser pressionada[n-1][0] = tempo da n 
                #[n-1][1] notas em bitwise
        #diz qual é o index da primeira e ultima nota a ser desenhada,para não ter que percorrer toda a buttonList
        directory = directoryManager.directoryManager()
        self.background = backgroundManager.background(directory.getImage() + "\\background.png",game)
        self.indexButtonDraw = [0,0]
        self.Time = 0
        self.difficulty = "Facil"
        self.game = game
        self.musicName = ""
        self.bitList = []
        self.rposX = [[0.105,-0.255],[0.06,-0.130],[0.0,0.0],[-0.06,0.130],[-0.105,0.255]]
        self.menu = None
        self.errorSound = audioManager.sound(directory.getAudio() +"/note_erro.ogg",0)
        self.endGame = None
        self.gameOver = None
    def setVolume(self):
        self.music.setVolume(self.game.getMusicVolume())
    def setDifficulty(self,difficulty):
        self.difficulty = difficulty
        if difficulty == "Facil":
            self.game.setDelayTime(5)
        elif difficulty == "Medio":
            self.game.setDelayTime(3.5)
        elif difficulty == "Dificil":
            self.game.setDelayTime(2.5)
    def setNotes(self,notes):
        self.noteList = notes
    def getNotes(self):
        return self.noteList


    def getDifficulty(self):
        return self.difficulty
    def beginScene(self):
        self.game.time = -5
        self.game.setScaleTime(1)
        self.background.setOn()
        self.indexButtonDraw[0] = 0
        self.indexButtonDraw[1] = 0
    def setLevel(self,musicName,game,playNote,isLevelMaker,menuPause):
        self.errorSound.setVolume(game.getFxMusicVolume())
        self.inMakeLevel = isLevelMaker
        self.musicName = musicName
        self.game.onPause = False
        self.data = databaseManager.dataManager(musicName)
        self.score = gamePointsManager.scoreManager(self.data.getHighScore)
        self.hp = gamePointsManager.hpManager()
        self.music = audioManager.music(musicName)
        self.music.setVolume(self.game.getMusicVolume())
        game.addEventFunction(self.eventPause)
        self.menu = menuPause
        if self.inMakeLevel:
            playNote.setLevelMaker()
            
            game.addEventFunction(self.eventChangeTime)

        else:
            
            playNote.setMusicLevel()

        game.addEventFunction(playNote.events)
        game.addRenderFunction(self.background.render,0)
        game.addRenderFunction(playNote.drawPlayNotes,1)
        game.addRenderFunction(self.updateNotes,2)
        self.beginScene()

        
    def onLevelMaker(self):
        self.inMakeLevel = True
    def isOnLevelMaker(self):
        return self.inMakeLevel
    def changeDeleteMode(self):
        self.inDeleteMode = not self.inDeleteMode
    def isDeleteMode(self):
        return self.inDeleteMode
    def changeTimeOnPause(self,game):
       game.changeTime(self.timeRate)
    def eventChangeTime(self,game):
        evnt = game.getEventList()
        if game.isOnPause():
            for event in evnt:
                i = - 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        game.addEventFunction(self.setChangeTime)
                        game.setScaleTime(-5)
                    elif event.key == pygame.K_RIGHT:
                        game.addEventFunction(self.setChangeTime)
                        game.setScaleTime(5)
                    self.music.setTime(game.getTime())
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        game.setScaleTime(0)
                        game.removeEventFunction(self.setChangeTime)
                    elif event.key == pygame.K_RIGHT:
                        game.setScaleTime(0)
                        game.removeEventFunction(self.setChangeTime)
    def setChangeTime(self,game):
        scale = game.getScaleTime()
        if self.music.isPlaying():
            self.music.setTime(game.getTime())
        else:
            game.setScaleTime(0)



    def eventPause(self,game):
        evnt = game.getEventList()
        for event in evnt:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        game.onPause = not game.onPause
                        print(game.onPause)
                        if game.onPause:
                            self.background.setOn()

                            self.music.pause()
                            game.setScaleTime(0)
                            if not self.inMakeLevel:
                                self.menu()
                        else:
                            if self.inMakeLevel:
                                self.music.setTime(game.getTime())
                            elif self.music.haveStarted():
                                self.music.play()

                            if not self.inMakeLevel:
                                self.menu()
                            game.setScaleTime(1)
                elif event.key == pygame.K_BACKSPACE and game.isOnPause() and self.inMakeLevel:
                    self.menu()
    def loadImages(self,game,local):
        self.Images = []
        i = 0
        for loc in local:
            self.Images.append(image(loc,game))
            i = i + 1
        self.i = i #numero de imagens armazenadas na variavel
    def isometricPositionDraw(self,index,timeNote,game):#transforma a imagem dependendo da posição em que ela aparece,para se mostrar uma vista isometrica,para desenha-la
        
        iniRatio = 0.54
        lastRatio = 0.95
        #showNoteTime = 0.2
        #initialPosY = iniRatio*globalVar.display_Height
        #lastPosY = lastRatio*globalVar.display_Height
        Time = game.getTime()
        delayTime = game.getDelayTime()
        
        r = (Time - timeNote + delayTime)
        if(r < 0.0):
            return
        #print("r é " + str(r))
        posY0 = iniRatio*self.display_Height
        ratio = (r * (lastRatio - iniRatio) / delayTime + iniRatio)/lastRatio
        image = imageManager.scaleImage(self.Images[index].Image,(ratio,ratio))
        posY = ratio*self.display_Height
        posX = self.display_Width*(1+self.rposX[index][0] + ratio*(self.rposX[index][1]- self.rposX[index][0]))/2
        dy = image.get_height()
        r = (posY + (dy>>1) - posY0)/dy
        if(r < 1):
            r = (posY - posY0)/dy
            image = imageManager.cutImage(image,(1.0,r))
            dy = (dy - image.get_height())>>1
            imageManager.drawImage(image,(posX,posY + int(dy)),game)
            return
        if game.didReScale() or (not game.isOnPause()):
            imageManager.drawImage(image,(posX,posY),game)
        else:
            imageManager.drawAsStatic(image,(posX,posY),game)
            
    def renderBackground(self,game):
        self.background.render(game)
    def updateNotes(self,game):
        buttonList = self.noteList
        indexButtonDraw = self.indexButtonDraw
        Time = game.getTime()
        delayTime = game.getDelayTime()
        Notes = self
        if (not game.isOnPause()) and (Time >= 0):
            if not self.music.haveStarted():
                game.time = 0
            self.music.play()
            
        if game.didReScale():
                self.display_Height = game.getHeight()
                self.display_Width = game.getWidth()
                for img in self.Images:
                    scale = game.getNewScale()
                    img.changeImage(imageManager.scaleImage(img.getImage(),(scale,scale)))

        display_Width = self.display_Width
        #global pressNotes
        i = Notes.i - 1
        beginList = indexButtonDraw[0]
        lastList = indexButtonDraw[1]
        if not buttonList:
            return
        if Time - buttonList[indexButtonDraw[0]][0] - 0.2*delayTime > 0:
            indexButtonDraw[0] = indexButtonDraw[0] + 1
            if indexButtonDraw[0] >= len(buttonList):
                indexButtonDraw[0] = len(buttonList)-1
        beginList = indexButtonDraw[0]
            
        i = Notes.i - 1
        #leftLine = display_Width/2 - 2*45
        #flag = 2
        #print('flag' + str(flag))
        #pressNotes.drawPlayNotes()
        j = indexButtonDraw[1]
        
        n = len(buttonList) - j
        while n > 0:
            if buttonList[j][0] - Time > delayTime:
                break
            j = j + 1
            n = n - 1
            indexButtonDraw[1] = j
        firstIndex = indexButtonDraw[0]
        while j > firstIndex:
            j = j - 1
            #drawButton(color,(leftLine + i*45,(Time - buttonList[i][j] - deltaTime )*globalVar.display_Height/deltaTime))
            i = 0
            a = 1
            while i < 5:
                if buttonList[j][1]&a == a:
                    Notes.isometricPositionDraw(i,buttonList[j][0],game)
                a = (a << 1)
                i += 1
        #flag = 3
        #print('flag' + str(flag)) 


class playNote():
    def __init__(self,nomallocal,pressDir,rightDir,game,Notes):
        display_Height = game.getHeight()
        display_Width = game.getWidth()
        self.posY = 0.95*display_Height
        self.posX = []
        self.notes = Notes
        self.deleteOnMaker = False
        self.judgeTime = 0.05
        self.timeToJudge = self.judgeTime
        self.canJudge = False
        self.pressed = False
        self.sumNote = 0
        self.notSumFinal = 0
        self.notePressFunction = None
        rposX = [-0.255,-0.130,0.0,0.130,0.255]
        
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
            self.posX.append((display_Width*(1 + rposX[i])/2))
    def setLevelMaker(self):
        self.notePressFunction = self.notePressJudgeOnLevelMaker
    def setMusicLevel(self):
        self.notePressFunction = self.notePressJudge
    def notePressed(self,i):
        if i == -1:
            return
        self.Images[i] = self.pressedImages[i]
    def judgeNote(self,game):
        if self.pressed:
            self.timeToJudge -= game.getDeltaTime()
            if (not self.canJudge) and self.timeToJudge <= 0:
                self.canJudge = True
                self.notePressFunction(game)
    def notePressJudge(self,game):
        buttonList = self.notes.noteList
        deltaTime = game.getDelayTime()
        time = game.getTime() + self.timeToJudge - self.judgeTime
        imprecisionTimeUp = 0.5#intervalo de tempo em que o jogador pode ser impreciso
        imprecisionTimeDown = 0.05#intervalo de tempo em que o jogador pode ser impreciso
        indexButtonDraw = self.notes.indexButtonDraw
        if not buttonList:
            return
        """if not buttonList[i]:
            self.Images[i] = self.pressedImages[i]
            return"""

        t = imprecisionTimeDown*2#garante que entra no porximo loop
        n = indexButtonDraw[1]
        j = indexButtonDraw[0] - 1
        while t >= imprecisionTimeDown and  j < n:
            j = j + 1
            t = time - buttonList[j][0]
        if t < imprecisionTimeDown and t > -imprecisionTimeUp and self.notSumFinal == buttonList[j][1]:
            i = 0
            a = 1
            score = 10
            while i < 5:
                f = a << i
                if(self.notSumFinal&f == f):
                    if self.sumNote&f == f:
                        self.Images[i] =  self.rightImages[i]#troca a imagem a ser desenhada
                        print(a)
                    self.notes.score.addScore(score)
                    score = score >> 1


                i += 1
            self.notes.score.addRow()
            del buttonList[j]
            indexButtonDraw[1] = indexButtonDraw[1] - 1
            self.notes.score.addScore(10)
            self.notes.hp.addHp(8)
            print('adcionar pontos')#adciona os pontos por ter acertado a nota
        else:
            self.notes.score.gotWrong()
            self.notes.hp.addHp(-5)
            i = 0
            a = 1
            """while i < 5:
                                                    a << i
                                                    if(self.notSumFinal&a == a):
                                                        self.Images[i] = self.pressedImages[i]
                                                    i += 1"""
            self.notes.errorSound.play()
            print('Ativa o som do erro')#Ativa o som do erro
    def notePressJudgeOnLevelMaker(self,game):
        buttonList = self.notes.noteList
        deltaTime = game.getDelayTime()
        time = game.getTime() + self.timeToJudge - self.judgeTime
        imprecisionTimeUp = 0.3#intervalo de tempo em que o jogador pode ser impreciso
        imprecisionTimeDown = 0.05#intervalo de tempo em que o jogador pode ser impreciso
        indexButtonDraw = self.notes.indexButtonDraw
        
        """if not buttonList[i]:
            self.Images[i] = self.pressedImages[i]
            return"""

        t = imprecisionTimeDown*2#garante que entra no porximo loop
        n = indexButtonDraw[1]
        j = indexButtonDraw[0] - 1
        tamanhoLista = len(buttonList)
        #começa por aqui
        while t >= imprecisionTimeDown and  j < n:
            j = j + 1
            if buttonList and j < tamanhoLista:
                t = time - buttonList[j][0]
            else:
                t = time
        if t < imprecisionTimeDown and t > -imprecisionTimeUp and buttonList:
            if (not self.deleteOnMaker) and j < tamanhoLista :
                buttonList[j][0] = (buttonList[j][0] + time)/2
                buttonList[j][1] = self.notSumFinal
            elif j < tamanhoLista:
                del buttonList[j]
                indexButtonDraw[1] -= 1

        else:
            t = time
            insertion = []
            insertion.append(t)
            insertion.append(self.notSumFinal)
            last = indexButtonDraw[1]
            ini = indexButtonDraw[0]
            end = len(buttonList)
            index = ini
            if not index >= end:
                while index < last and buttonList[index][0] < t:
                    index = index + 1
            if index >= end:
                buttonList.append(insertion)
            elif index == last and buttonList[index] > t:
                buttonList.insert(index,insertion)
            else:
                buttonList.insert(index+1,insertion)
                #coloca entre index e index-1
    def noteUnpress(self,i):
        if i == -1:
            return
        self.Images[i] =  self.NormalStateImage[i]

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
            if game.didReScale() or (not game.isOnPause()):
                self.Images[i].drawImage((self.posX[i],self.posY),game)
            else:
                self.Images[i].drawAsStatic((self.posX[i],self.posY),game)
            i = i + 1

    def events(self,game):
        evt = game.getEventList()
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
                elif event.key == pygame.K_z and game.isOnPause():
                    self.deleteOnMaker = not self.deleteOnMaker

                if i >= 0:
                    self.pressed = True
                    a = (1 << i)
                    self.sumNote = self.sumNote|a
                    self.notSumFinal = self.notSumFinal|a
                self.notePressed(i)
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
                if i >= 0 and i <= 4:
                    a = (1 << i)
                    self.sumNote = (self.sumNote|a)^a
                    print(self.sumNote)
                    if not self.canJudge:
                            self.notePressFunction(game)
                    self.pressed = False
                    self.notSumFinal = 0
                    self.timeToJudge = self.judgeTime
                    self.canJudge = False
                self.noteUnpress(i)

        self.judgeNote(game)
        
