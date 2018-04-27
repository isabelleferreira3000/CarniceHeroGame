import os.path
from pathlib import Path
class directoryManager:
    def __init__(self):
        self.main = str(Path(os.path.dirname(os.path.realpath(__file__))).parent)
        self.audio = 'sound mp3'
        self.imagens = 'imagens'
        self.scripts = 'scripts'
        self.musicas = 'musicas'
        self.added = 'adcionadas'
    def getMain(self):
        return self.main
    def getAudio(self):
        return self.main + "\\" +self.audio
    def getImage(self):
        return self.main + "\\" +self.imagens
    def getScripts(self):
        return self.main + "\\" +self.scripts
    def getMusic(self):
        return self.main + "\\" +self.musicas
    def getAddedDir(self):
        return self.main + "\\" +self.added
    def goTo(self,direc):
        return self.main + "\\" + direc
    def getMusicList(self,difficulty):
    #vai para o diretorio de musicas e retorna a lista de todas as musicas
        musicList = []
        audioDir = self.main + '\\' + self.musicas
        """subString = difficulty + '.csv'"""
        subString = '.mp3'
        for file in os.listdir(audioDir):
            if file.endswith(subString):
                audio = os.path.basename(os.path.normpath(file)).replace(subString,'')
                musicList.append(audio)
                #procurar pelo banco de dados correspondente

        return musicList
    def getAdded(self,difficulty):
        #vai para o diretorio de musicas e retorna a lista de
        #todas as musicas com banco de dados
        musicList = []
        audioDir = self.main + '\\' + self.added
        subString = difficulty + '.csv'
        for file in os.listdir(audioDir):
            if file.endswith(subString):
                audio = os.path.basename(os.path.normpath(file)).replace(subString,'')
                musicList.append(audio)
                #procurar pelo banco de dados correspondente se
                #encontra adciona na lista
        return musicList
    def getNoAdded(self):
        #vai para o diretorio de musicas e retorna a lista de
        #todas as musicas sem banco de dados
        musicList = []
        audioDir = self.main + '\\' + self.added
        for file in os.listdir(audioDir):
            if file.endswith('.mp3'):
                audio = os.path.basename(os.path.normpath(file)).replace('.mp3','')
                musicList.append(audio)
                #procurar pelo banco de dados correspondente,adciona na
                #lista se não encontrar
        return musicList

"""direc = directoryManager()
musilist = direc.getMusicList()
print(musilist)"""
