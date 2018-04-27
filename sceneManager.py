import delegation

class sceneManager:
    def __init__(self,sceneName):
        self.name = sceneName
        self.beginScene = delegation.delegate()
        self.updateScene = delegation.delegate()
    def addBeginScene(self,beginFunction):
        self.beginScene.add(beginScene)
    def removeBeginScene(self,beginFunction):
        self.beginScene.remove(beginFunction)
    def removeAllBeginScenes(self):
        self.beginScene = delegation.delegate()
    def addUpdateScene(self,updateFunction):
        self.updateScene.add(updateFunction)
    def removeUpdateScene(self,updateFunction):
        self.updateScene.remove(updateFunction)
    def removeAllUpdateScenes(self):
        self.updateScene = delegation.delegate()
