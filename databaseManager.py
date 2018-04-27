import csv

class dataManager:
    def __init__(self,file):
        self.music = file
        self.exist = False
        self.highScore = 0
    def getHighScoreFromData(self):
        fileName = self.music + difficulty + ".csv"
        with open(self.file,'r') as csv_file:
            
            csv_r = csv.reader(csv_file,delimiter='-')
            csv_reader = list(csv_r)
            self.highScore = int(csv_reader[i])
    def getHighScore(self):
        return self.highScore
    def takeNotes(self,difficulty):
        fileName = self.music + difficulty + ".csv"
        with open(fileName,'r+') as csv_file:
            
            csv_r = csv.reader(csv_file,delimiter='-')
            csv_reader = list(csv_r)
            nLines = len(csv_reader)
            #nLines -= 1
            """if nLines <= 0:
                                                    self.highScore = 0
                                                    noteList = []
                                                    return noteList
                                                i = 0
                                                self.highScore = int(csv_reader[i][0])
                                                i = i + 1
                                                #for line in """
            noteList = []
            for preLista in csv_reader:
                """time = float(line[0])
                a = int(line[1])
                note = []
                note.append(time)
                note.append(a)"""
                line = list(preLista)
                t = []
                t.append(float(line[0]))
                t.append(int(line[1]))
                noteList.append(t)
            """while i < nLines:
                time = float(csv_reader[i][0])

                a = int(csv_reader[i][1])
                note = []
                note.append(time)
                note.append(a)
                noteList.append(note)

                i = i + 1"""
        return noteList
    def writeNotes(self,noteList,difficulty):
        fileName = self.music + difficulty + ".csv"
        with open(fileName, "w") as csv_file:
            writer = csv.writer(csv_file, delimiter='-')
            lista = []
            #lista.append('0')
            """writer.writerows(lista)
            for line in noteList:
                v = []
                v.append([line[0]])
                v.append([line[1]])"""
            writer.writerows(noteList)




