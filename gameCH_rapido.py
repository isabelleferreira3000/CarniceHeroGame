# Explicação do codigo:A maioria das funções aqui provavelmente não serão aproveitadas(provavelmente serão feitos ou
# usados alguns modulos para fazer essas funcionalidades),as variaveis mais importantes são:
# buttonList,indexButtonDraw,Time,deltaTime,Notes,gameDisplay,background_surface.
# as classes mais importantes são:Image,imageNotes
# os metodos mais importantes fora dos que estão dentro das classes beginScene(),ButtonsToDraw(),drawScene(),Update()
# from colorName import *
import random, math, pygame, sys, os, time
from pygame.locals import *

last_frame_rect = []
atual_frame_rect = []
timePause = 0
tempodespause = 0
tempopause = 0


class Relogio:
    """ Classe com as informacoes do relogio do jogo. """

    def __init__(self, fps):
        self.fps = fps
        self.relogio = pygame.time.Clock()


class Audio:
    """ Classe com as informacoes dos audios do jogo. """

    def __init__(self, endereco, volume):
        self.audio = pygame.mixer.Sound(endereco)
        self.audio.set_volume(volume)

    def play(self):
        self.audio.play()

    def stop(self):
        self.audio.stop()


class Tela:
    """ Classe com as informacoes do display do jogo. """

    def __init__(self, largura, altura, titulo, enderecoImagemFundo):
        self.largura = largura
        self.altura = altura
        self.titulo = titulo
        self.imagemFundo = pygame.image.load(enderecoImagemFundo)
        self.imagemFundo = pygame.transform.scale(self.imagemFundo, (self.largura, self.altura))
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption(self.titulo)



class Menu:

    def game_menu(self, musica_menu):

        pygame.init()
        musica_menu.play(-1)
        
        menu_inicial_iniciar = Tela(1115, 713, "CarniceHero", "menu_inicial_iniciar.jpg")
        menu_inicial_como_jogar = Tela(1115, 713, "CarniceHero", "menu_inicial_como_jogar.jpg")
        menu_inicial_creditos = Tela(1115, 713, "CarniceHero", "menu_inicial_creditos.jpg")

        menu_como_jogar = Tela(1115, 713, "CarniceHero", "menu_como_jogar.jpg")
        menu_creditos = Tela(1115, 713, "CarniceHero", "menu_creditos_2.jpg")

        menu_dificuldade_olodum = Tela(1115, 713, "CarniceHero", "menu_dificuldade_olodum.jpg")
        menu_dificuldade_samba_normal = Tela(1115, 713, "CarniceHero", "menu_dificuldade_samba_normal.jpg")
        menu_dificuldade_samba_frenetico = Tela(1115, 713, "CarniceHero", "menu_dificuldade_samba_frenetico.jpg")
        menu_dificuldade_voltar = Tela(1115, 713, "CarniceHero", "menu_dificuldade_voltar.jpg")
        nivel_bloqueado = Tela(1115, 713, "CarniceHero", "nivel_bloqueado.jpg")

        audio_menu_navigate = Audio("menu_navigate_0.wav", 1)

        relogio_jogo = Relogio(60)

        fechar_jogo = False

        estado = "menu_inicial_iniciar"
        menu = True
        while menu:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    fechar_jogo = True
                    menu = False

                elif event.type == pygame.KEYDOWN:

                    if event.key == 13:  # 13 == botao ENTER:
                        if estado == "menu_inicial_iniciar":
                            audio_menu_navigate.audio.play()
                            estado = "menu_dificuldade_olodum"
                        elif estado == "menu_dificuldade_voltar" or estado == "nivel_bloqueado":
                            audio_menu_navigate.audio.play()
                            estado = "menu_inicial_iniciar"
                        elif estado == "menu_inicial_como_jogar":
                            audio_menu_navigate.audio.play()
                            estado = "menu_como_jogar"
                        elif estado == "menu_inicial_creditos":
                            audio_menu_navigate.audio.play()
                            estado = "menu_creditos"
                        elif estado == "menu_como_jogar":
                            audio_menu_navigate.audio.play()
                            estado = "menu_inicial_como_jogar"
                        elif estado == "menu_creditos":
                            audio_menu_navigate.audio.play()
                            estado = "menu_inicial_creditos"
                        elif estado == "menu_dificuldade_olodum" or estado == "menu_dificuldade_samba_frenetico":
                            audio_menu_navigate.audio.play()
                            estado = "nivel_bloqueado"
                        else:
                            audio_menu_navigate.audio.play()
                            menu = False

                    elif estado == "menu_inicial_iniciar":
                        if event.key == pygame.K_DOWN:
                            audio_menu_navigate.audio.play()
                            estado = "menu_inicial_como_jogar"
                        elif event.key == pygame.K_UP:
                            audio_menu_navigate.audio.play()
                            estado = "menu_inicial_creditos"

                    elif estado == "menu_inicial_como_jogar":
                        if event.key == pygame.K_DOWN:
                            audio_menu_navigate.audio.play()
                            estado = "menu_inicial_creditos"
                        elif event.key == pygame.K_UP:
                            audio_menu_navigate.audio.play()
                            estado = "menu_inicial_iniciar"

                    elif estado == "menu_inicial_creditos":
                        if event.key == pygame.K_DOWN:
                            audio_menu_navigate.audio.play()
                            estado = "menu_inicial_iniciar"
                        elif event.key == pygame.K_UP:
                            audio_menu_navigate.audio.play()
                            estado = "menu_inicial_como_jogar"

                    elif estado == "menu_dificuldade_olodum":
                        if event.key == pygame.K_DOWN:
                            audio_menu_navigate.audio.play()
                            estado = "menu_dificuldade_samba_normal"
                        elif event.key == pygame.K_UP:
                            audio_menu_navigate.audio.play()
                            estado = "menu_dificuldade_voltar"

                    elif estado == "menu_dificuldade_samba_normal":
                        if event.key == pygame.K_DOWN:
                            audio_menu_navigate.audio.play()
                            estado = "menu_dificuldade_samba_frenetico"
                        elif event.key == pygame.K_UP:
                            audio_menu_navigate.audio.play()
                            estado = "menu_dificuldade_olodum"

                    elif estado == "menu_dificuldade_samba_frenetico":
                        if event.key == pygame.K_DOWN:
                            audio_menu_navigate.audio.play()
                            estado = "menu_dificuldade_voltar"
                        elif event.key == pygame.K_UP:
                            audio_menu_navigate.audio.play()
                            estado = "menu_dificuldade_samba_normal"

                    elif estado == "menu_dificuldade_voltar":
                        if event.key == pygame.K_DOWN:
                            audio_menu_navigate.audio.play()
                            estado = "menu_dificuldade_olodum"
                        elif event.key == pygame.K_UP:
                            audio_menu_navigate.audio.play()
                            estado = "menu_dificuldade_samba_frenetico"

            if estado == "menu_inicial_iniciar":
                menu_inicial_iniciar.tela.blit(menu_inicial_iniciar.imagemFundo, (0, 0))
            elif estado == "menu_inicial_como_jogar":
                menu_inicial_como_jogar.tela.blit(menu_inicial_como_jogar.imagemFundo, (0, 0))
            elif estado == "menu_inicial_creditos":
                menu_inicial_creditos.tela.blit(menu_inicial_creditos.imagemFundo, (0, 0))
            elif estado == "menu_como_jogar":
                menu_como_jogar.tela.blit(menu_como_jogar.imagemFundo, (0, 0))
            elif estado == "menu_creditos":
                menu_creditos.tela.blit(menu_creditos.imagemFundo, (0, 0))
            elif estado == "menu_dificuldade_olodum":
                menu_dificuldade_olodum.tela.blit(menu_dificuldade_olodum.imagemFundo, (0, 0))
            elif estado == "menu_dificuldade_samba_normal":
                menu_dificuldade_samba_normal.tela.blit(menu_dificuldade_samba_normal.imagemFundo, (0, 0))
            elif estado == "menu_dificuldade_samba_frenetico":
                menu_dificuldade_samba_frenetico.tela.blit(menu_dificuldade_samba_frenetico.imagemFundo, (0, 0))
            elif estado == "menu_dificuldade_voltar":
                menu_dificuldade_voltar.tela.blit(menu_dificuldade_voltar.imagemFundo, (0, 0))
            elif estado == "nivel_bloqueado":
                nivel_bloqueado.tela.blit(nivel_bloqueado.imagemFundo, (0, 0))

            relogio_jogo.relogio.tick(relogio_jogo.fps)
            pygame.display.update()

        musica_menu.stop()

        if fechar_jogo:
            return "fechar_jogo"
        else:
            return estado


os.environ['SDL_VIDEO_CENTERED'] = '1'  # abre a tela do jogo já centralizada

pygame.init()
pygame.font.init()

display_Width = 1115
display_Height = 713

# cores
yellow_carni = (254, 163, 0)
pink_carni = (222, 0, 148)
white = (255, 255, 255)
black = (0, 0, 0)

# variáveis de contagem
countacertos = 0
counterros = 0

gameExit = False
onLoad = False
onPause = False

musica_menu = pygame.mixer.music
musica_menu.load("garotadeipanema.ogg")
menu = Menu()
estado = menu.game_menu(musica_menu)
if estado == "fechar_jogo":
    gameExit = True

buttonList = ([], [], [], [], [])  # lista dos tempos que cada nota deverá ser pressionada
indexButtonDraw = [0, 0, 0, 0, 0]  # diz qual é o index da última nota a ser desenhada,
# para não ter que percorrer toda a buttonList
Time = 0.0  # variável de tempo
deltaTime = 4.0  # diferença de tempo onde começa a ver as notas, para poder pressioná-las
Frame = 0
numberOfButtons = 0

# configurações iniciais
FPS = 24
scene = 'main_menu'
gameName = "CarniceHero"
gameDisplay = pygame.display.set_mode((display_Width, display_Height))
clock = pygame.time.Clock()
# background_surface = pygame.Surface((display_Width, display_Height))
# background_surface.fill(black)
icon = pygame.image.load('images/urubu.png')
pygame.display.set_icon(icon)

# áudios importados
errorSound = pygame.mixer.Sound("sounds/note_erro.ogg")
gameoverSound = pygame.mixer.Sound("sounds/gameoversound.ogg")
wingameSound = pygame.mixer.Sound("sounds/winsound.ogg")
musicaJogo = pygame.mixer.music
musicaJogo.load("sounds/samba_normal_2_0.7.ogg")



def DrawDisplay(display_width, display_heigth, fps, Name):
    global clock, FPS
    pygame.display.set_caption(Name)
    clock = pygame.time.Clock()
    FPS = fps
    return pygame.display.set_mode((display_width, display_heigth))


def Event():
    return pygame.event.get()


def GameQuit():
    return pygame.QUIT


def Quit():
    pygame.quit()
    sys.exit()


class Image:
    def __init__(self, local):
        self.Local = local
        self.Image = Image.scaleImage(pygame.image.load(local), (1.0, 1.0)).convert_alpha()
        self.Rect = self.Image.get_rect()

    def changeImage(self,image):
        self.Image = image
        self.Rect = self.Image.get_rect()

    def scaleImage(image, scale=(1.0, 1.0)):
        ScaledImage = pygame.transform.smoothscale(image, (
        int(scale[0] * image.get_width()), int(scale[1] * image.get_height())))
        return ScaledImage

    def cutImage(image, shown=(1.0, 1.0)):
        CutImage = pygame.transform.chop(image, (0.0, 0.0, shown[0] * image.get_width(), shown[1] * image.get_height()))
        return CutImage

    def drawChangedImage(image, pos=(0.0, 0.0)):
        rect = image.get_rect()
        global gameDisplay
        global atual_frame_rect
        atual_frame_rect.append(gameDisplay.blit(image, (int(pos[0] - rect.center[0]), int(pos[1] - rect.center[1]))))


class imageNotes:  # lista de botões para instanciar as notas (definir comportamento), sem ter que armazenar as notas da tela
    def __init__(self):
        global display_Height
        global display_Width
        self.display_Height = display_Height
        self.display_Width = display_Width
        self.rposX = [[0.105,-0.255],[0.06,-0.130],[0.0,0.0],[-0.06,0.130],[-0.105,0.255]]

    def loadImages(self, local):
        self.Images = []
        i = 0
        for loc in local:
            self.Images.append(Image(loc))
            i = i + 1
        self.i = i  # número de imagens armazenadas na variável

    def isometricPositionDraw(self, index,
                              time):  # transforma a imagem dependendo da posição em que ela aparece,para se mostrar uma vista isometrica,para desenha-la
        global Time, deltaTime
        iniRatio = 0.54
        lastRatio = 0.95
        posY0 = iniRatio*self.display_Height

        r = (Time - time - deltaTime)
        if (r <= 0.0):
            return

        ratio = (r * (lastRatio - iniRatio) / deltaTime + iniRatio)/lastRatio

        image = Image.scaleImage(self.Images[index].Image, (ratio, ratio))
        #### altera-se em posY a distância do topo da tela e o início da nota
        posY = ratio * self.display_Height
        #### altera-se em posX a distância horizontal entre as notas
        posX = self.display_Width*(1+self.rposX[index][0] + ratio*(self.rposX[index][1]- self.rposX[index][0]))/2
        dy = image.get_height()
        r = (posY + (dy>>1) - posY0)/dy
        if (r < 1):
            image = Image.cutImage(image, (1.0, r))
            dy = (dy - image.get_height())>>1
            Image.drawChangedImage(image, (posX, posY + int(dy)))
            return
        Image.drawChangedImage(image, (posX, posY))


class playNote():
    def __init__(self, nomallocal, pressDir, rightDir):
        global display_Height
        global display_Width
        global Notes
        self.posY = 0.95 * display_Height
        self.posX = []

        """for i in range(0, 5):
                                    self.posX.append(display_Width / 2 + 1.5 * (i - 2) * Notes.Images[i].Image.get_width())"""
        self.Images = []  # imagem a ser desenhada
        self.NormalStateImage = []  # imagem a ser desenhada quando os botões para pressionar as notas não forem ativados
        self.pressedImages = []  # imagem a ser desenhada quando os botões forem ativados e errarem
        self.rightImages = []  # imagem a ser desenhada quando as notas forem pressionadas corretamente
        i = 0
        escala = 2
        for loc in nomallocal:
            img = Image(loc)
            img.changeImage(Image.scaleImage(img.Image, scale=(escala, escala)))
            self.NormalStateImage.append(img)
            self.Images.append(img)
            i = i + 1
        for i in range(0, 5):
            self.posX.append(display_Width / 2 + 1.5 * (i - 2) * self.NormalStateImage[i].Image.get_width())

        for loc in pressDir:
            img = Image(loc)
            img.changeImage(Image.scaleImage(img.Image, scale=(escala, escala)))
            self.pressedImages.append(img)

        for loc in rightDir:
            img = Image(loc)
            img.changeImage(Image.scaleImage(img.Image, scale=(escala, escala)))
            self.rightImages.append(img)
        self.i = i  # número de imagens armazenadas na variável

    def notePressed(self, i, time, impresTime):
        global buttonList
        global deltaTime
        global indexButtonDraw
        global counterros, countacertos
        if i == -1:
            return
        if not buttonList[i]:
            self.Images[i] = self.pressedImages[i]
            return

        t = time - buttonList[i][0] - 2 * deltaTime
        t = impresTime * 2  # garante que entra no próximo loop
        n = indexButtonDraw[i]
        j = -1

        while t > impresTime and j < n:
            j = j + 1
            t = time - buttonList[i][j] - 2 * deltaTime
        if onPause == False:
            if t < impresTime/10 and t > -impresTime:
                self.Images[i] = self.rightImages[i]  # troca a imagem a ser desenhada
                del buttonList[i][j]
                indexButtonDraw[i] = indexButtonDraw[i] - 1
                countacertos = countacertos + 1
                print('acertos = ', countacertos)  # adiciona os pontos por ter acertado a nota
            else:
                self.Images[i] = self.pressedImages[i]
                errorSound.play()
                counterros = counterros + 1
                print('erros = ', counterros)

    # def noteUnpress(self, i):
    #     if i == -1:
    #         self.Images[i] = self.NormalStateImage[i]

    def noteUnpress(self, i):
        if i == -1:
            return
        self.Images[i] = self.NormalStateImage[i]

    def drawPlayNotes(self):
        i = 0
        while i < 5:
            pos = (self.posX[i], self.posY)
            Image.drawChangedImage(self.Images[i].Image, (self.posX[i] , self.posY))
            i = i + 1

    def events(self, evt):
        global Time
        imprecisionTime = 1  # intervalo de tempo em que o jogador pode ser impreciso
        i = -1
        for event in evt:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    i = 0
                elif event.key == pygame.K_s:
                    i = 1
                elif event.key == pygame.K_d:
                    i = 2
                elif event.key == pygame.K_k:
                    i = 3
                elif event.key == pygame.K_l:
                    i = 4
                self.notePressed(i, Time, imprecisionTime)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    i = 0
                elif event.key == pygame.K_s:
                    i = 1
                elif event.key == pygame.K_d:
                    i = 2
                elif event.key == pygame.K_k:
                    i = 3
                elif event.key == pygame.K_l:
                    i = 4
                self.noteUnpress(i)

Notes = imageNotes()
Notes.loadImages(("images/green_note.png", "images/yellow_note.png", "images/red_note.png", "images/blue_note.png",
                  "images/orange_note.png"))
pressNotes = playNote(nomallocal=(
"images/green_fixed.png", "images/yellow_fixed.png", "images/red_fixed.png", "images/blue_fixed.png",
"images/orange_fixed.png")
                      , pressDir=(
    "images/green_pressed.png", "images/yellow_pressed.png", "images/red_pressed.png", "images/blue_pressed.png",
    "images/orange_pressed.png")
                      , rightDir=(
    "images/ok_note.png", "images/ok_note.png", "images/ok_note.png", "images/ok_note.png",
    "images/ok_note.png"))


def makesList():
    global buttonList
    lastTime = 0
    n = 0
    while n < 200:
        i = random.randint(0, 4)
        if buttonList[i]:
            lastTime = buttonList[i][len(buttonList[i]) - 1]
        lastTime = lastTime + random.randint(0, 40) / 5
        buttonList[i].append(lastTime)
        n = n + 1


def makesListVirada():
    global buttonList
    lastTime = 0
    x = 1.3
    buttonList = (
    [12.1-x, 17.8-x, 23.6-x, 25-x, 30.1-x, 31.5-x, 36.6-x, 38-x, 43.1-x, 44.5-x, 48.7-x, 52.2-x, 52.9-x, 57.8-x, 61.1-x, 64.6-x, 65.3-x, 70.2-x],
    [10.7-x, 12.9-x, 16.6-x, 50.8-x, 53.6-x, 57.1-x, 63.2-x, 66-x, 69.5-x, 74.5-x, 75.2-x, 76-x, 76.7-x, 77.5-x, 78.2-x, 79-x, 79.8-x, 80.6-x, 81.3-x, 82.1-x, 82.8-x, 83.6-x, 84.3-x, 85.1-x, 85.9-x, 86.7-x],
    [11.6-x, 15.2-x, 17.2-x, 22.9-x, 24.3-x, 29.4-x, 30.8-x, 35.9-x, 37.3-x, 42.4-x, 43.8-x, 48-x, 49.4-x, 55.7-x, 60.4-x, 61.8-x, 68.1-x, 99.8-x, 100.4-x, 101.3-x, 102.1-x],
    [19.2-x, 50.1-x, 54.3-x, 55.0-x, 58.5-x, 59.2-x, 62.5-x, 66.7-x, 67.4-x, 70.9-x, 75.6-x, 77.1-x, 78.6-x, 79.4-x, 80.2-x, 81.7-x, 83.2-x, 84.7-x, 85.5-x, 86.3-x],
    [6.9-x, 7.4-x, 7.9-x, 10-x, 16.0-x, 22.2-x, 28.7-x, 35.2-x, 41.7-x, 47.3-x, 51.5-x, 56.4-x, 59.7-x, 63.9-x, 68.8-x, 90.5-x, 91.3-x, 92.1-x, 92.9-x, 96.2-x, 97-x, 97.8-x, 98.6-x])


 

BackGr = pygame.image.load("images/backgr_ok.png")


def beginScene():
    global onPause
    global display_Width
    global display_Height
    global FPS
    global gameName
    global gameDisplay
    global musicaJogo
    global atual_frame_rect
    global BackGr
    atual_frame_rect.append(gameDisplay.blit(BackGr, (0, 0)))
    onPause = False
    global Time
    Time = 0.0
    gameDisplay.fill((0.0, 0.0, 0.0))
    gameDisplay = DrawDisplay(display_Width, display_Height, FPS, gameName)
    musicaJogo.play()


beginScene()


def ButtonsToDraw():
    global buttonList
    global indexButtonDraw
    global Time
    global deltaTime
    global Notes
    global display_Width
    global pressNotes
    global counterros
    i = Notes.i - 1
    while i >= 0:
        if buttonList[i]:
            if Time - buttonList[i][0] > 2 * deltaTime:
                del buttonList[i][0]
                counterros += 1
                indexButtonDraw[i] = indexButtonDraw[i] - 1
        i = i - 1
    i = Notes.i - 1
    leftLine = display_Width / 2 - 2 * 45
    pressNotes.drawPlayNotes()
    while i >= 0:
        j = indexButtonDraw[i]
        if buttonList[i]:
            n = len(buttonList[i]) - j
            while n > 0:
                if buttonList[i][j] - Time > deltaTime:
                    break
                j = j + 1
                n = n - 1
                indexButtonDraw[i] = j
        while j > 0:
            j = j - 1
            Notes.isometricPositionDraw(i, buttonList[i][j])
        i = i - 1


ImageMestreNormal = pygame.image.load('images/normal.png')
ImageMestreSurprised = pygame.image.load('images/surpresa.png')
ImageMestreSad = pygame.image.load('images/triste.png')
ImageMestreDead = pygame.image.load('images/morta.png')
ImageMestreWings = pygame.image.load('images/mortaAsas.png')
ImageGameOver = pygame.image.load('images/game_over.png')
ImageScoreFinal = pygame.image.load('images/score_final_over.png')
ImageMestreGanhou = pygame.image.load('images/ganhouBone.png')

gameOver = False
playerGanhou = False
contador_musica_derrota = 0

def drawScene():
    global gameDisplay
    # global background_surface
    global display_Width, display_Height
    global counterros, countacertos, BackGr
    global musicaJogo
    global onPause
    global text2, pauseFont
    global gameOver, playerGanhou, contador_musica_derrota

    scr = countacertos - counterros

    # gameDisplay.blit(background_surface,(0,0))
    gameDisplay.blit(BackGr, (0, 0))
    
    if playerGanhou == False:
        atual_frame_rect.append(gameDisplay.blit(ImageMestreNormal, (display_Width / 2 - 125, 45)))

        if -10 < scr < 0:
            atual_frame_rect.append(gameDisplay.blit(ImageMestreSad, (display_Width / 2 - 125, 45)))
        elif -25 < scr <= -10:
            atual_frame_rect.append(gameDisplay.blit(ImageMestreDead, (display_Width / 2 - 125, 45)))
        elif scr <= -25:
            atual_frame_rect.append(gameDisplay.blit(ImageMestreWings, (display_Width / 2 - 125, 45)))
            onPause = True
            gameOver = True
            if contador_musica_derrota == 0:
                musicaJogo.pause()
                gameoverSound.play()
                contador_musica_derrota += 1
            atual_frame_rect.append(gameDisplay.blit(ImageGameOver, (240,255)))
            atual_frame_rect.append(gameDisplay.blit(ImageScoreFinal, (80, 630)))


        if scr > 60:
            atual_frame_rect.append(gameDisplay.blit(ImageMestreSurprised, (display_Width / 2 - 125, 45)))

    ButtonsToDraw()


ImageOne = pygame.image.load('images/cont1.png')
ImageTwo = pygame.image.load('images/cont2.png')
ImageThree = pygame.image.load('images/cont3.png')
ImageFour = pygame.image.load('images/cont4.png')
CarniChegou = pygame.image.load('images/carniceriachegou.png')
VoceGanhou = pygame.image.load('images/voce_ganhou.png')

contador_musica_vitoria = 0

def contRegress():
    global ImageOne
    global ImageTwo
    global ImageThree
    global ImageFour
    global CarniChegou
    global atual_frame_rect
    global timePause
    global playerGanhou, contador_musica_vitoria
    
    timePause=0

    if not onPause:
        if temporizador >= (3 + timePause) and temporizador < (3.8 + timePause):
            atual_frame_rect.append(gameDisplay.blit(ImageOne, (display_Width / 2 - 250, 100)))
        elif temporizador >= (3.8 + timePause) and temporizador < (4.6 + timePause):
            atual_frame_rect.append(gameDisplay.blit(ImageTwo, (display_Width / 2 - 180, 100)))
        elif temporizador >= (4.6 + timePause) and temporizador < (5.4 + timePause):
            atual_frame_rect.append(gameDisplay.blit(ImageThree, (display_Width / 2 - 180, 100)))
        elif temporizador >= (5.4 + timePause) and temporizador < (6.2 + timePause):
            atual_frame_rect.append(gameDisplay.blit(ImageFour, (display_Width / 2 - 220, 100)))
        elif temporizador >= (25.5 + timePause) and temporizador < (27.7 + timePause):
            atual_frame_rect.append(gameDisplay.blit(CarniChegou, (display_Width / 2 - 370, 280)))
        elif temporizador > 140:
            playerGanhou = True
            atual_frame_rect.append(gameDisplay.blit(ImageMestreGanhou, (display_Width / 2 - 125, 45)))
            atual_frame_rect.append(gameDisplay.blit(VoceGanhou, (228,255)))
            if contador_musica_vitoria == 0:
                musicaJogo.pause()
                wingameSound.play()
                contador_musica_vitoria += 1
        

ImagePause = pygame.image.load('images/pause.png')
ImageScore = pygame.image.load('images/score.png')
scoreAntigo = 0
##painel de scores
text = pygame.font.Font("Symtext.ttf", 37)
text2 = pygame.font.Font("8-bit pusab.ttf", 40)
realScore = text.render(str(0), 1, white)
pauseFont = text.render("PAUSE", 1, yellow_carni)

blitText = []
def Update():
    global Time
    global onPause
    global Frame
    global gameExit, gameOver
    global FPS
    global pressNotes
    global gameDisplay, display_Width, display_Height
    global musicaJogo
    global counterros, countacertos,scoreAntigo
    global atual_frame_rect, last_frame_rect
    global ImagePause, ImageScore
    global realScore,text,blitText
    global timePause, tempopause, tempodespause
    global pauseFont,text2,blitText

    score = countacertos - counterros

    dt = clock.tick(FPS) / 1000
    if onPause == False:
        Frame = Frame + 1
        Time = Time + dt

    
    if not score == scoreAntigo:
        realScore = text.render(str(score), 1, white)

    drawScene()
    evt = Event()
    for event in evt:
        if event.type == GameQuit():
            gameExit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if temporizador > 27.7:
                    if onPause:
                        onPause = False
                        musicaJogo.unpause()
                        print(onPause)
                        tempodespause = temporizador

                    elif not onPause:
                        onPause = True
                        musicaJogo.pause()
                        tempopause = temporizador
                        print(onPause)

    if not onPause:
        if not scoreAntigo == score:
            atual_frame_rect.append(gameDisplay.blit(ImageScore, (40, 630)))
            atual_frame_rect.append(gameDisplay.blit(realScore, (240, 619)))
            atual_frame_rect.append(blitText)
        else:
            gameDisplay.blit(ImageScore, (40, 630))
            blitText = gameDisplay.blit(realScore, (240, 619))
    else:
        if not gameOver:
            blitText = gameDisplay.blit(pauseFont, (100, 630))

    contRegress()

    rects = atual_frame_rect + last_frame_rect
    pressNotes.events(evt)
    pygame.display.update(rects)
    last_frame_rect = atual_frame_rect
    atual_frame_rect = []


# makesList()
makesListVirada()

inicio = time.time()

frame = 0
while not gameExit:

    fim = time.time()
    temporizador = fim - inicio
    
    if frame % 30 == 0:
        print(temporizador)
    Update()
    frame += 1
Quit()
print("fim")
