class scoreManager:
    def __init__(self,highScore):
        self.score = 0
        self.highScore = highScore
        self.multiplier = 1
        self.maxInARow = 0
        self.inARow = 0
    def addRow(self):
        self.inARow = self.inARow + 1
        if self.maxInARow < self.inARow:
            self.maxInARow = self.inARow
    def addScore(self,point):
        
        self.score = self.score + self.multiplier*point
        if self.inARow >= 60:
            self.multiplier = 5
        elif self.inARow >= 40:
            self.multiplier = 4
        elif self.inARow >= 30:
            self.multiplier = 3
        elif self.inARow >= 15:
            self.multiplier = 2
    def gotWrong(self):
        self.inARow = 0
        self.multiplier = 1
    def getMultipler(self):
        return self.multiplier
    def getScore(self):
        return self.score
    def getInARow(self):
        return self.inARow
    def getMaxInARow(self):
        return self.maxInARow

class hpManager:
    def __init__(self):
        self.hp = 50
    def addHp(self,point):#pode ser usado para adciona ou subtrair
        if self.hp <=20:
            if point > 0:
                point = 4*point
            point = point/2
        self.hp = self.hp + point
        if self.hp <= 0:
            self.hp = 0
        elif self.hp >= 100:
            self.hp = 100
    def getHp(self):
        return self.hp


