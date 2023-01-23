class Key:
    def __init__(self, key=None):
        if key:
            self.A: bool = key.A
            self.B: bool = key.B
            self.C: bool = key.C
            self.U: bool = key.U
            self.R: bool = key.R
            self.D: bool = key.D
            self.L: bool = key.L
        else:
            self.empty()
    
    def empty(self):
        self.A = False
        self.B = False
        self.C = False
        self.U = False
        self.R = False
        self.D = False
        self.L = False
