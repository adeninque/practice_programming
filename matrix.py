import random

class Matrix:
    def __init__(self, n, m):
        self.__matrix = [[random.randint(1, 9) for _ in range(n)] for _ in range(m)]
    
    def swapRows(self, r1, r2):
        self.__matrix[r1 - 1], self.__matrix[r2 - 1] = self.__matrix[r2 - 1], self.__matrix[r1 - 1]
    
    def swapCollums(self, c1, c2):
        for i in self.__matrix:
            i[c1 - 1], i[c2 - 1] = i[c2 - 1], i[c1 - 1]
    
    def display(self):
        for m in self.__matrix:
            print(m)
    
    def sumRow(self, r):
        summa = 0
        for i in self.__matrix[r - 1]:
            summa += i
        return summa
    
    def sumColl(self, c):
        summa = 0
        for i in self.__matrix:
            summa += i[c - 1]
        return summa
    
    def sumDiagonal(self):
        summa = 0
        for i in range(len(self.__matrix)):
            summa += self.__matrix[i][i]
        return summa
    

m1 = Matrix(3,3)
m1.display()
print(m1.sumColl(2))
print(m1.sumRow(1))
print(m1.sumDiagonal())
