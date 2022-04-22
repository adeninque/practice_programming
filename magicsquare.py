from operator import le
from turtle import left


class Magic:
    def __init__(self, square: list):
        self.n = len(square)
        self.m = len(square[0])
        self.square = square
        self.solve()

    def solve(self):
        self.bottom = []
        self.left = []
        self.d1 = 0
        self.d2 = 0
        for i in range(self.n):
            temp_b = 0
            temp_l = 0
            self.d1 += self.square[i][i]
            self.d2 += self.square[i][self.n - i - 1]
            for j in range(self.m):
                temp_l += self.square[i][j]
                temp_b += self.square[j][i]
            self.left.append(temp_l)
            self.bottom.append(temp_b)
    
    def __str__(self):
       
        # return f'{sum(self.bottom) / (self.n)} {self.d1} {self.d2} {sum(self.left) / (self.n)}'
        return f"{self.d1}" if sum(self.bottom) / (self.n) == self.d1 == self.d2 == sum(self.left) / (self.n) else "It is not magic box" 
sq = [[8, 1, 6],
      [3, 5, 7],
      [4, 9, 2]]

m1 = Magic(sq)
print(m1)
        
        