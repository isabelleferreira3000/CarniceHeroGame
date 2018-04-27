#Explicação do codigo:A maioria das funções aqui provavelmente não serão aproveitadas(provavelmente serão feitos ou 
#usados alguns modulos para fazer essas funcionalidades),as variaveis mais importantes são:
#buttonList,indexButtonDraw,Time,deltaTime,Notes,gameDisplay,background_surface.
#as classes mais importantes são:Image,imageNotes
#os metodos mais importantes fora dos que estão dentro das classes beginScene(),ButtonsToDraw(),drawScene(),Update()
#from colorName import *
#Nomes das cenas mainMenu,songLevel,levelMaker
import random
import math
import pygame
from pygame.locals import *
import delegation
from imageManager import *
from gameStateManager import *
from noteManager import *
#import pygame
display_Width = 1240
display_Height = 720
FPS = 60
scene = 'mainMenu'
gameName = "Carnice Hero"
gameExit = False
onLoad = False
#UI = Canvas()
buttonList = ([],[],[],[])#aqui tem a lista dos tempos que cada nota devera ser pressionada
indexButtonDraw = [0,0,0,0,0]#diz qual é o index da ultima nota a ser desenhada,para não ter que percorrer toda a buttonList
onPause = False
Time = 0.0#variavel de tempo
deltaTime = 4.0#diferença de tempo onde começa a ver as notas, para poder pressiona-las
Frame = 0
numberOfButtons = 0


def makesList():
    lista = []
    lastTime = '0.0'
    n = 0
    #dn = 1
    #flag = 0
    #print('flag' + str(flag))
    while n < 200:
        i = random.randint(0,20)
        if lista:
            lastTime = lista[len(lista) - 1][0]
        lastTime = float(lastTime) + random.randint(0,40)/10
        t = []
        t.append(lastTime)
        t.append(i)

        lista.append(t)
        n = n + 1
    for line in lista:
        print(str(line[0])+'-' + str(line[1]))
makesList()
"""def makesList(notes):
    buttonList = notes.noteList
    lastTime = 0.0
    n = 0
    #dn = 1
    #flag = 0
    #print('flag' + str(flag))
    while n < 2000:
        i = random.randint(0,20)
        if buttonList:
            lastTime = buttonList[len(buttonList) - 1][0]
        lastTime = lastTime + float(random.randint(0,40)/10)
        t = []
        t.append(lastTime)
        t.append(i)

        buttonList.append(t)
        n = n + 1
        #dn = dn - 1
    #return n


gameState = gameStateManager()
Notes = imageNotes(gameState)
Notes.loadImages(gameState,("green.png","yellow.png","rednote.png","blue.png","orange.png"))
pressNotes = playNote(nomallocal = ("greenNormal.png","yellowNormal.png","redNormal.png","blueNormal.png","orangeNormal.png")
    ,pressDir = ("greenPressed.png","yellowPressed.png","redPressed.png","bluePressed.png","orangePressed.png")
    ,rightDir = ("greenPressed.png","yellowPressed.png","redPressed.png","bluePressed.png", "orangePressed.png")
                      ,game = gameState
                      ,Notes = Notes)
gameState.addRenderFunction(pressNotes.drawPlayNotes,0)
gameState.addRenderFunction(Notes.updateNotes,1)
gameState.addEventFunction(pressNotes.events)
makesList(Notes)
#Notes.loadImages(("download1.jpg","download1.jpg","download1.jpg","download1.jpg","download1.jpg"))


while not gameState.getGameExit():
    gameState.update()
pygame.quit()
print("fim")
"""
