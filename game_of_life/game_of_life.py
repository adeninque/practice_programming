import random
from tkinter import *
from time import sleep
import os

class Game:
    def __init__(self, n, m):
        self.__generate_field(n, m)
        self.__patterns = []
            
    def __generate_field(self, n, m):
        self.game_field = [[0 for _ in range(self.__is_int(m))] for _ in range(self.__is_int(n))]
        self.__rows, self.__cols = n, m
        

    @staticmethod
    def __is_int(x):
        if type(x) != int:
            raise TypeError('Check for int not passed')
        return x
    
    def display(self):
        print('\n'.join([' '.join(['*' if col == 1 else '-' for col in row]) for row in self.game_field]))
    
    def step(self):
        changes = []
        for i in range(self.__rows):
            for j in range(self.__cols):
                neighbors = 0
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if k != i or l != j:
                            if 0 <= k < self.__rows and 0 <= l < self.__cols:
                                if self.game_field[k][l] == 1:
                                    neighbors += 1
                                    
                if self.game_field[i][j] == 1:
                    if not(neighbors in [2,3]):
                        changes.append([0, [i, j]])
                else:
                    if neighbors == 3:
                        changes.append([1, [i, j]])
        for c in changes:
            self.game_field[c[1][0]][c[1][1]] = c[0]
    
    def start(self):
        width = self.__cols * 20
        height = self.__rows * 20
        dead_color = '#F1F1F1'
        alive_clors = ['#FB512D']
        
        root = Tk()
        root.geometry(f'{width}x{height}')
        canva = Canvas(root, width = width, height = height)
        
        def run():
            canva.delete('all')
            for i in range(self.__rows):
                    for j in range(self.__cols):
                        canva.create_rectangle(0 + (20*j), 0 + (20*i), 20 + (20*j), 20 + (20*i), fill = dead_color if self.game_field[i][j] == 0 else random.choice(alive_clors), outline='')
            self.step()
            canva.after(300, run)
        
        canva.pack()
        run()
        root.mainloop()
    
    def fill_random(self):
        for _ in range((self.__cols * self.__rows) // 2):
            while True:
                i, j = random.randint(0, self.__rows-1), random.randint(0, self.__cols-1)
                if self.game_field[i][j] != 1:
                    self.game_field[i][j] = 1
                    break
        self.game_field[self.__rows // 2][self.__cols // 2] = 1
    
    @property
    def pattern():
        pass
    
    @pattern.setter
    def pattern(self, other):
        self.__patterns.append(self.__create_pattern(other))
    
    @staticmethod
    def __create_pattern(pat):
        m = []
        for p in pat:
            col = []
            for l in p:
                if l in ['1','0']:
                    col.append(int(l))
                else:
                    raise ValueError('Pattern shoud contain only 1 or 0')
            m.append(col)
        return m
    
    def place_pattern(self, index):
        pat_rows = len(self.__patterns[index])
        pat_cols = len(self.__patterns[index][0])
        for i in range(pat_rows):
            for j in range(pat_cols):
                self.game_field[self.__rows // 2 - pat_rows // 2 + i][self.__cols // 2 - pat_cols // 2 + j] = self.__patterns[index][i][j]

    def add_pattern(self, link):
        if type(link) != str:
            raise TypeError('Link should be string')
        with open(link) as file:
            self.pattern = file.read().split('\n')

if __name__ == '__main__':
    g = Game(30, 40)
    # g.add_pattern(os.path.abspath('game_of_life\pattern1.txt'))
    # g.place_pattern(0)
    # g.fill_random()
    g.start()