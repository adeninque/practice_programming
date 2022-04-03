class Cell:
    
    def __init__(self, i, j):
        self.alive = False
        self.i = i
        self.j = j
        self.vision = 1
        self.will_live = False
    
    def discover(self, board, n, m):
        neighbors = 0
        for k in range(self.i - self.vision, self.i + self.vision + 1):
            for l in range(self.j - self.vision, self.j + self.vision + 1):
                if 0 <= k < n and 0 <= l < m:
                    if board[k][l] != self:
                        if board[k][l].alive:
                            neighbors += 1
        
        if self.alive:
            if neighbors in [2,3]:
                self.will_live = True
            else:
                self.will_live = False
        else:
            if neighbors == 3:
                self.will_live = True
            else:
                self.will_live = False
    
    def cycle(self):
        self.alive = self.will_live