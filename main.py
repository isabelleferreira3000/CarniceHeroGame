from gui import *
from audioManager import *
import gameStateManager,directoryManager,databaseManager,noteManager,delegation
class mainMenu:
    def __init__(self,game,noteLevel,notePlay):
        self.game = game
        self.level = noteLevel
        self.notePlay = notePlay
        self.center = [game.getDisplayWidth,game.getDisplayHeight]
        center = self.center
        self.Menu = menu(game,"",(center[0]()>>1),(center[1]()>>1))
        self.difficulty = ""
        self.sizeTitle = 120
        self.sizeText = 30
        self.buildMain()
        self.levelMaker = False
        self.lastBuild = delegation.delegate()
    def buildMain(self):
        self.levelMaker = False
        game = self.game
        center = self.center
        self.Menu = menu(game,"",(center[0]()>>1),(center[1]()>>1))
        menuMain = self.Menu
        game.removeAllRender()
        game.removeAllEventFunction()

        menuMain.addTitle(text('Carnice',Cor.branco,self.sizeTitle,center[0]()>>1,center[1]()*0.1,game))
        menuMain.addTitle(text('Hero',Cor.rosa,self.sizeTitle,center[0]()>>1,center[1]()*0.3,game))
        textoFuncao = setValueText("Jogar",Cor.rosa,self.sizeText,center[0]()>>1,center[1]()*0.3,game,value = "")
        textoFuncao.addNoValueFunction(self.buildDifficulty)
        menuMain.addFunction(textoFuncao)
        textoFuncao = setValueText("Criar Level",Cor.branco,self.sizeText,center[0]()>>1,center[1]()*0.3,game,value = "")
        textoFuncao.addNoValueFunction(self.buildDifficulty)
        textoFuncao.addNoValueFunction(self.setOnLevelMaker)
        menuMain.addFunction(textoFuncao)
        textoFuncao = setValueText("Opções",Cor.branco,self.sizeText,center[0]()>>1,center[1]()*0.3,game,value = "")
        textoFuncao.addNoValueFunction(self.opcoes)
        menuMain.addFunction(textoFuncao)
        textoFuncao = setValueText("Sair",Cor.branco,self.sizeText,center[0]()>>1,center[1]()*0.3,game,value = "")
        textoFuncao.addNoValueFunction(game.setGameExit)
        menuMain.addFunction(textoFuncao)
        game.addEventFunction(menuMain.eventMenu)
        game.addRenderFunction(menuMain.render,0)
    def backSpaceEvent(self,game):
        evnt = game.getEventList()
        for event in evnt:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        a = self.lastBuild.pop()
                        if not(a == None):
                            a()
                        else:
                            self.buildMain()


                        
    """def removeEventFunction(self,eventFunction):
        self.eventList.remove(eventFunction)
    def removeAllEventFunction(self):
        self.eventList = delegation.delegate()"""
    """addRenderFunction(self,renderFunction,layer):
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
            listRender.call(self)"""
    def setOnLevelMaker(self):
        self.levelMaker = True
    def buildDifficulty(self):
        game = self.game
        self.lastBuild.add(self.buildDifficulty)
        self.lastBuild.add(self.buildMain)
        game.removeAllRender()
        game.removeAllEventFunction()
        center = self.center
        
        self.Menu = menu(game,"",(center[0]()>>1),(center[1]()>>1))
        menuMain = self.Menu
        menuMain.addTitle(text('Dificuldade',Cor.rosa,self.sizeTitle,center[0]()>>1,center[1]()*0.1,game))
        textoFuncao = setValueText("Facil",Cor.rosa,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,value = "Facil")
        textoFuncao.addValueFunction(self.changeDifficulty)
        menuMain.addFunction(textoFuncao)
        textoFuncao = setValueText("Medio",Cor.branco,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,value = "Medio")
        textoFuncao.addValueFunction(self.changeDifficulty)
        menuMain.addFunction(textoFuncao)
        textoFuncao = setValueText("Dificil",Cor.branco,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,value = "Dificil")
        textoFuncao.addValueFunction(self.changeDifficulty)
        menuMain.addFunction(textoFuncao)
        
        game.addEventFunction(self.backSpaceEvent)
        game.addEventFunction(menuMain.eventMenu)
        game.addRenderFunction(menuMain.render,0)
    def changeDifficulty(self,difficulty):
        game = self.game
        game.removeAllRender()
        game.removeAllEventFunction()
        center = self.center
        
        self.Menu = menu(game,"",(center[0]()>>1),(center[1]()>>1))
        menuMain = self.Menu
        menuMain.addTitle(text('Musicas',Cor.rosa,self.sizeTitle,center[0]()>>1,center[1]()*0.1,game))
        self.difficulty = difficulty
        directory = directoryManager.directoryManager()
        if self.levelMaker:
            lista = directory.getNoAdded()
            if lista:
                textoFuncao = setValueText(lista[0],Cor.rosa,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,
                    value = directory.getAddedDir() + '\\' + lista[0])
                del lista[0]
                textoFuncao.addValueFunction(self.getMusicNotes)
                menuMain.addFunction(textoFuncao)
            for item in lista:
                textoFuncao = setValueText(item,Cor.branco,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,
                    value = directory.getAddedDir() + '\\' + item)
                textoFuncao.addValueFunction(self.getMusicNotes)
                menuMain.addFunction(textoFuncao)
        else:
            lista = directory.getMusicList(difficulty)
            n = len(lista)
            if lista:
                textoFuncao = setValueText(lista[0],Cor.rosa,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,
                    value = directory.getMusic() + '\\' + lista[0])
                del lista[0]
                textoFuncao.addValueFunction(self.getMusicNotes)
                menuMain.addFunction(textoFuncao)
            for item in lista:
                textoFuncao = setValueText(item,Cor.branco,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,
                    value = directory.getMusic() + '\\' + item)
                textoFuncao.addValueFunction(self.getMusicNotes)
                menuMain.addFunction(textoFuncao)
            lista = directory.getAdded(difficulty)
            if n == 0:
                textoFuncao = setValueText(lista[0],Cor.rosa,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,
                    value = directory.getAddedDir() + '\\' + lista[0])
                del lista[0]
                textoFuncao.addValueFunction(self.getMusicNotes)
                menuMain.addFunction(textoFuncao)

            for item in lista:
                textoFuncao = setValueText(item,Cor.branco,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,
                    value = directory.getAddedDir() + '\\' + item)
                textoFuncao.addValueFunction(self.getMusicNotes)
                menuMain.addFunction(textoFuncao)

        game.addEventFunction(self.backSpaceEvent)
        game.addEventFunction(menuMain.eventMenu)
        game.addRenderFunction(menuMain.render,0)
    def getMusicNotes(self,musicName):
        game = self.game
        difficulty = self.difficulty
        playNotes = self.notePlay
        noteLevel = self.level
        cena = songLevel(game,noteLevel,playNotes)
        if self.levelMaker:
            menuPause =  cena.returnToMenuOnLevelMaker
        else:
            menuPause = cena.buildMenuPause

        
        game.removeAllRender()
        game.removeAllEventFunction()
        data = databaseManager.dataManager(musicName)
        notes = data.takeNotes(difficulty)
        noteLevel.setDifficulty(difficulty)
        noteLevel.setNotes(notes)
        noteLevel.setLevel(musicName,game,playNotes,self.levelMaker,menuPause)
        noteLevel.gameOver = cena.gameOver
        noteLevel.endGame = cena.endGame
        self = cena
    def opcoes(self):
        self.lastBuild.add(self.opcoes)
        direc = directoryManager.directoryManager()
        center = self.center
        self.Menu = menu(game,"",(center[0]()>>1),(center[1]()>>1))
        menuMain = self.Menu
        game = self.game
        game.removeAllRender()
        game.removeAllEventFunction()
        game.addEventFunction(self.notePlay.eventPause)
        menuMain.addTitle(text('Opções',Cor.branco,int(self.sizeTitle*0.7),center[0]()>>1,center[1]()*0.1,game))
        textoFuncao = setChangeValueText("Volume: ",Color.rosa,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,
            game.getMusicVolume(),1,10)
        textoFuncao.addValueFunction(game.setMusicVolume)
        menuMain.addFunction(textoFuncao)
        textoFuncao = setChangeValueText("Volume: ",Color.branco,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,
            game.getFxMusicVolume(),1,10)
        textoFuncao.addValueFunction(game.setFxMusicVolume)
        menuMain.addFunction(textoFuncao)
        game.addEventFunction(self.backSpaceEvent)
        game.addEventFunction(menuMain.eventMenu)
        game.addRenderFunction(menuMain.render,0)

class songLevel:
    def __init__(self,game,noteLevel,notePlay):
        self.game = game
        self.notePlay = notePlay
        self.noteLevel = noteLevel
        self.center = [game.getDisplayWidth,game.getDisplayHeight]
        self.lastBuild = delegation.delegate()
        self.lastBuild.add(self.returnGame)
        self.on = False
        self.sizeTitle = 120
        self.sizeText = 30
    def backSpaceEvent(self,game):
        evnt = game.getEventList()
        for event in evnt:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        a = self.lastBuild.pop()
                        a = self.lastBuild.top()
                        if not(a == None):
                            a()
    def buildMenuPause(self):        
        self.lastBuild.add(self.buildMenuPause)
        game = self.game
        playNote = self.notePlay
        noteLevel = self.noteLevel
        if not self.on:
            self.on = True
            direc = directoryManager.directoryManager()
            center = self.center
            self.Menu = menu(game,"",(center[0]()>>1),(center[1]()>>1))
            menuMain = self.Menu
            game.removeAllRender()
            game.removeAllEventFunction()
            game.addEventFunction(noteLevel.eventPause)
            menuMain.addTitle(text('Pause',Cor.rosa,self.sizeTitle,center[0]()>>1,center[1]()*0.1,game))
            textoFuncao = setValueText("Retornar",Cor.rosa,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,value = "")
            textoFuncao.addNoValueFunction(self.returnGame)
            menuMain.addFunction(textoFuncao)
            textoFuncao = setValueText("Recomeçar",Cor.branco,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,value = "")
            textoFuncao.addNoValueFunction(self.restart)
            menuMain.addFunction(textoFuncao)
            textoFuncao = setValueText("Menu Principal",Cor.branco,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,value = "")
            textoFuncao.addNoValueFunction(self.returnToMenu)
            menuMain.addFunction(textoFuncao)
            textoFuncao = setValueText("Opções",Cor.branco,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,value = "")
            textoFuncao.addNoValueFunction(self.returnToMenu)
            menuMain.addFunction(textoFuncao)
            game.addEventFunction(self.backSpaceEvent)
            game.addEventFunction(menuMain.eventMenu)
            game.addRenderFunction(menuMain.render,0)
        else:
            self.returnGame()
            """game.removeAllRender()
                                                game.removeAllEventFunction()
                                                game.addEventFunction(noteLevel.eventPause)
                                                game.addEventFunction(playNote.events)
                                                game.addRenderFunction(noteLevel.background.render,0)
                                                game.addRenderFunction(noteLevel.updateNotes,1)
                                                game.addRenderFunction(playNote.drawPlayNotes,2)
                                                if noteLevel.music.haveStarted():
                                                    noteLevel.music.play()
                                                self.on = False"""

    def returnGame(self):
        self.lastBuild = delegation.delegate()
        self.lastBuild.add(self.returnGame)
        game = self.game
        playNote = self.notePlay
        noteLevel = self.noteLevel
        game.removeAllRender()
        game.removeAllEventFunction()
        game.addEventFunction(noteLevel.eventPause)
        game.addEventFunction(playNote.events)
        game.addRenderFunction(noteLevel.background.render,0)
        game.addRenderFunction(playNote.drawPlayNotes,1)
        game.addRenderFunction(noteLevel.updateNotes,2)
        if noteLevel.music.haveStarted():
            noteLevel.music.play()
        game.setScaleTime(1)
        self.on = False
        game.onPause = False
    def restart(self):
        self.lastBuild = delegation.delegate()
        self.lastBuild.add(self.returnGame)
        self.on = False
        game = self.game
        playNote = self.notePlay
        noteLevel = self.noteLevel
        game.removeAllRender()
        game.removeAllEventFunction()
        data = databaseManager.dataManager(noteLevel.musicName)
        notes = data.takeNotes(noteLevel.difficulty)
        noteLevel.setNotes(notes)
        menu = songLevel(game,noteLevel,playNote)
        noteLevel.setLevel(noteLevel.musicName,game,playNote,noteLevel.inMakeLevel,menu.buildMenuPause)
    def returnToMenu(self):
        game = self.game
        playNote = self.notePlay
        noteLevel = self.noteLevel
        menu = mainMenu(game,noteLevel,playNote)
        menu.buildMain()
        self.on = False
        game.onPause = False
        self = menu
    def returnToMenuOnLevelMaker(self):
        game = self.game
        playNote = self.notePlay
        noteLevel = self.noteLevel
        data = databaseManager.dataManager(noteLevel.musicName)
        data.writeNotes(noteLevel.getNotes(),noteLevel.difficulty)
        notes = data.takeNotes(noteLevel.difficulty)
        menu = mainMenu(game,noteLevel,playNote)
        menu.buildMain()
        self.on = False
        game.onPause = False
        self = menu
    def endGame(self):
        self.lastBuild = delegation.delegate()
        self.lastBuild.add(self.endGame)
        direc = directoryManager.directoryManager()
        center = self.center
        self.Menu = menu(game,"",(center[0]()>>1),(center[1]()>>1))
        menuMain = self.Menu
        noteLevel = self.noteLevel
        game.removeAllRender()
        game.removeAllEventFunction()

        game.addEventFunction(self.notePlay.eventPause)
        menuMain.addTitle(text('Score:',Cor.branco,self.sizeTitle,center[0]()>>1,center[1]()*0.1,game))
        menuMain.addTitle(text(str(noteLevel.score.getScore()),Cor.rosa,self.sizeTitle>>1,center[0]()>>1,center[1]()*0.1,game))
        menuMain.addTitle(text('In a Row:'+str(noteLevel.score.getMaxInARow()),Cor.rosa,self.sizeTitle>>1,center[0]()>>1,center[1]()*0.1,game))
        textoFuncao = setValueText("Recomeçar",Cor.rosa,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,value = "")
        textoFuncao.addNoValueFunction(self.restart)
        menuMain.addFunction(textoFuncao)
        textoFuncao = setValueText("Menu Principal",Cor.branco,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,value = "")
        textoFuncao.addValueFunction(self.returnToMenu)
        menuMain.addFunction(textoFuncao)
        textoFuncao = setValueText("Opções",Cor.branco,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,value = "")
        textoFuncao.addValueFunction(self.returnToMenu)
        menuMain.addFunction(textoFuncao)
        game.addEventFunction(self.backSpaceEvent)
        game.addEventFunction(menuMain.eventMenu)
        game.addRenderFunction(menuMain.render,0)
    def gameOver(self):
        self.lastBuild = delegation.delegate()
        self.lastBuild.add(self.gameOver)
        direc = directoryManager.directoryManager()
        center = self.center
        self.Menu = menu(game,"",(center[0]()>>1),(center[1]()>>1))
        menuMain = self.Menu
        game.removeAllRender()
        game.removeAllEventFunction()
        game.addEventFunction(self.notePlay.eventPause)
        menuMain.addTitle(text('Game',Cor.branco,int(self.sizeTitle*0.7),center[0]()>>1,center[1]()*0.1,game))
        menuMain.addTitle(text('Over',Cor.rosa,self.sizeTitle,center[0]()>>1,center[1]()*0.1,game))
        textoFuncao = setValueText("Recomeçar",Cor.rosa,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,value = "")
        textoFuncao.addNoValueFunction(self.restart)
        menuMain.addFunction(textoFuncao)
        textoFuncao = setValueText("Menu Principal",Cor.branco,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,value = "")
        textoFuncao.addValueFunction(self.returnToMenu)
        menuMain.addFunction(textoFuncao)
        textoFuncao = setValueText("Opções",Cor.branco,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,value = "")
        textoFuncao.addValueFunction(self.opcoes)
        menuMain.addFunction(textoFuncao)
        game.addEventFunction(self.backSpaceEvent)
        game.addEventFunction(menuMain.eventMenu)
        game.addRenderFunction(menuMain.render,0)
    def opcoes(self):
        self.lastBuild.add(self.opcoes)
        direc = directoryManager.directoryManager()
        center = self.center
        self.Menu = menu(game,"",(center[0]()>>1),(center[1]()>>1))
        menuMain = self.Menu
        game = self.game
        game.removeAllRender()
        game.removeAllEventFunction()
        game.addEventFunction(self.notePlay.eventPause)
        menuMain.addTitle(text('Opções',Cor.branco,int(self.sizeTitle*0.7),center[0]()>>1,center[1]()*0.1,game))
        textoFuncao = setChangeValueText("Volume: ",Color.rosa,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,
            game.getMusicVolume(),1,10)
        textoFuncao.addValueFunction(game.setMusicVolume)
        menuMain.addFunction(textoFuncao)
        textoFuncao = setChangeValueText("Volume: ",Color.branco,self.sizeText,center[0]()>>1,(center[1]()>>1)*0.3,game,
            game.getFxMusicVolume(),1,10)
        textoFuncao.addValueFunction(game.setFxMusicVolume)
        menuMain.addFunction(textoFuncao)
        game.addEventFunction(self.backSpaceEvent)
        game.addEventFunction(menuMain.eventMenu)
        game.addRenderFunction(menuMain.render,0)


        



gameState = gameStateManager.gameStateManager()
Notes = noteManager.imageNotes(gameState)
Notes.loadImages(gameState,("green.png","yellow.png","rednote.png","blue.png","orange.png"))
pressNotes = noteManager.playNote(nomallocal = ("greenNormal.png","yellowNormal.png","redNormal.png","blueNormal.png","orangeNormal.png")
    ,pressDir = ("greenPressed.png","yellowPressed.png","redPressed.png","bluePressed.png","orangePressed.png")
    ,rightDir = ("greenPressed.png","yellowPressed.png","redPressed.png","bluePressed.png", "orangePressed.png")
                      ,game = gameState
                      ,Notes = Notes)
gameState.addRenderFunction(pressNotes.drawPlayNotes,0)
gameState.addRenderFunction(Notes.updateNotes,1)
gameState.addEventFunction(pressNotes.events)
cena = mainMenu(gameState,Notes,pressNotes)
#Notes.loadImages(("download1.jpg","download1.jpg","download1.jpg","download1.jpg","download1.jpg"))


while not gameState.getGameExit():
    gameState.update()
pygame.quit()
print("fim")
