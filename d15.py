from readFile import readFile as r
from collections import defaultdict
import math
from copy import deepcopy

inp = r(15)[0].split(",")
#inp = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(",")

def calcHash(h):
    c = 0 
    for i in h:
        c += ord(i)
        c *= 17
        c = c % 256
    return c

print(sum(map(calcHash, inp)))


class boxes:
    
    def __init__(self):
        self.boxes = [[] for _ in range(256)]
    
    def addTo(self,box,lens,n):
        for i in range(len(self.boxes[box])):
            if lens == self.boxes[box][i][0]:
                self.boxes[box][i][1] = n
                return None
        self.boxes[box].append([lens,n])
    
    def remove(self,box,lens):
        for i in range(len(self.boxes[box])):
            if lens == self.boxes[box][i][0]:
                self.boxes[box].__delitem__(i)
                return None
            
    def runCommand(self,c):
        if c[-1] == "-":
            self.remove(calcHash(c[:-1]), c[:-1])
        else:
            a,b = c.split("=")
            self.addTo(calcHash(a),a,int(b))
            
    def calcPower(self):
        s = 0
        for i in range(len(self.boxes)):
            for j in range(len(self.boxes[i])):
                s += (i+1)*(j+1)*self.boxes[i][j][1]
        return s
    
b = boxes()
for i in inp:
    b.runCommand(i)
print(b.calcPower())
