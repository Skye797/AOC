from readFile import readFile as r
from collections import defaultdict
import math
from copy import deepcopy

inp = r(14)
'''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''.split("\n")


N, E, S, W = lambda x: (x[0]-1,x[1]), lambda x: (x[0],x[1]+1), lambda x: (x[0]+1,x[1]),lambda x: (x[0],x[1]-1)


class spaces:
    
    def __init__(self,m):
        self.rocks = [(i,j) for i in range(len(m)) for j in range(len(m[0])) if m[i][j] == 'O']
        self.boulders = [(i,j) for i in range(len(m)) for j in range(len(m[0])) if m[i][j] == '#']
        self.mrow = len(m)
        self.mcol = len(m[0])
        self.prevs = []
    
    def moveRocks(self,d):
        c = 1
        if d == N:
            a = 0
            b = False
        elif d == E:
            a = 1
            b = True
        elif d == S:
            a = 0
            b = True
        else:
            a = 1
            b = False
        self.rocks = sorted(self.rocks, key=lambda x:x[a], reverse=b)
        for i in range(len(self.rocks)):
            m = True
            while m:
                a = d(self.rocks[i])
                if a[0] == -1 or a[0] == self.mrow or a[1] == -1 or a[1] == self.mcol:
                    m = False
                elif a not in self.rocks + self.boulders:
                    self.rocks[i] = a
                else:
                    m = False

    def calcLoad(self):
        return sum(map(lambda x:(self.mrow-x[0]), self.rocks))
    
    def spin(self):
        self.prevs.append(deepcopy(self.rocks))
        for i in [N,W,S,E]:
            self.moveRocks(i)
        
    def showMap(self):
        k = [["." for j in range(self.mcol)] for i in range(self.mrow)]
        for i,j in self.rocks:
            k[i][j] = 'O'
        for i,j in self.boulders:
            k[i][j] = '#'
        print("\n".join(["".join([j for j in i]) for i in k]))
        
    
    def do1000000000Cycles(self):
        c = 0
        n = 1000000000
        while self.rocks not in self.prevs:
            self.spin()
            c += 1
            print("\r{:.2f}%".format(100*c/112),end="")
        for i in range(len(self.prevs)):
            if self.prevs[i] == self.rocks:
                f = c - i
                break
        c = ((n - c)//f)*f + c
        while c < n:
            self.spin()
            c += 1
        print()
        
        
    
s = spaces(inp)
s.moveRocks(N)
print(s.calcLoad())

s = spaces(inp)
s.do1000000000Cycles()
print(s.calcLoad())
