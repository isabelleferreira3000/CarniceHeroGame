class delegate:
    def __init__(self,function = None):
        self.func = []
        if(function != None):
            self.func.append(function)
    def add(self,function):
        if not function == None:
            i = self.find(function)

            if i == -1:
                self.func.append(function)
    def remove(self,function):
        i = self.find(function)
        if i != -1:
            del self.func[i]
    def call(self,x = None):
        if x == None:
            for a in self.func:
                a()
        else:
            for a in self.func:
                a(x)
    def isEmpty(self):
        if len(self.func) == 0:
            return True
        return False
    def find(self,function):
        i = 0
        n = len(self.func)
        found = False
        while i < n:
            if(self.func[i] == function):
                return i
            i = i + 1

        return -1
    def pop(self):
        n = len(self.func) - 1
        a = None
        if n>= 0:
            a = self.func[n]
            del self.func[n]
        return a
    def top(self):
        n = len(self.func) - 1
        a = None
        if n>= 0:
            a = self.func[n]
        return a