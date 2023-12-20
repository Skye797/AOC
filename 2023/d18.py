from readFile import readFile as r
from collections import defaultdict
import math
from copy import deepcopy
import gratheory
import time

class rang:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def split(self, splitby):
        if splitby - self.start >0:
            if self.end - splitby >0:
                return rang(self.start,splitby), rang(splitby, self.end)
            return self, None
        return None, self
    
    def __repr__(self):
        return "range("+str(self.start)+", "+str(self.end)+")"
    
    def toTuple(self):
        return (self.start,self.end)
    

inp = [(lambda x:(x[0],int(x[1]),x[2]))(i.split(" ")) for i in r(18)]
[(lambda x:(x[0],int(x[1]),x[2]))(i.split(" ")) for i in  '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''.split("\n")]

U, R, D, L = "U", "R", "D", "L"

intToDir = {"0":"R", "1":"D", "2":"L", "3":"U"}

def rgb(r):
    return (intToDir[r[2][-2]], int(r[2][2:-2], base=16))

part2 = True
if part2:
    inp = list(map(rgb, inp))
    
vertLines = []
horLines = []
edges = []
corners = []
pointType = defaultdict(lambda :"|")
lastD = U
firstD = inp[0][0]
cType = {(U,R):"F", (L,D):"F", (U,L):"7", (R,D):"7", (D,R):"L", (L,U):"L", (R,U):"J", (D,L):"J"}
y = 0
x = 0 
def move(d, n):
    global x,y, lastD
    pointType[(y,x)] = cType[(lastD,d)]
    lastD = d
    if d == U:
        vertLines.append((x, rang(y-n,y+1)))
        y, x = y-n, x
    if d == R:
        edges.append(y)
        horLines.append((y,rang(x,x+n+1)))
        y,x = y, x+n
    if d == D:
        vertLines.append((x, rang(y,y+n+1)))
        y, x = y+n, x
    if d == L:
        edges.append(y)
        horLines.append((y,rang(x-n,x+1)))
        y,x = y, x-n
    corners.append((y,x))

def calcOverlaps():
    for a in horLines:
        for b in vertLines:
            if b[1].start+1<a[0]<b[1].end-1 and a[1].start+1<b[0]<a[1].end-1:
                print("Overlap at",a[0],b[0])

def splitVerLines(horLine):
    v = []
    for i in vertLines:
        splitted = i[1].split(horLine)
        for j in splitted:
            if j != None:
                v.append((i[0],j))
    return v

vertLines = []
y = 0
def nextInstruction(instruction):
    move(instruction[0],instruction[1])
for i in inp:
    nextInstruction(i)
calcOverlaps()
pointType[(0,0)] = cType[(lastD,firstD)]
for i in horLines:
    vertLines = splitVerLines(i[0])
    vertLines = splitVerLines(i[0]+1)



ranges = defaultdict(lambda :[])
for i in vertLines:
    ranges[i[1].toTuple()].append(i[0])
# now in form of vertical line to the horizontal positions

for i in ranges.keys():
    ranges[i] = sorted(ranges[i])
ranges = list(ranges.items())
s = 0
p = [0,0,0,0,0,0,0,0,0]
for i in range(len(ranges)):
    a = ranges[i][0][1] - ranges[i][0][0]
    y = ranges[i][0][0]
    xs = ranges[i][1]
    n = True #True means use the next non edge values
    for j in range(len(xs)-1):
        ptype0, ptype1 = pointType[(y,xs[j])], pointType[(y,xs[j+1])]
        if ptype0 == "L" and ptype1 == "J":
            if n:
                s += (xs[j+1] + 1 - xs[j])*a
            else:
                s += (xs[j+1] - xs[j])*a
            n = not n
        elif ptype0 == "F" and ptype1 == "7":
            if n:
                s += (xs[j+1] + 1 - xs[j])*a
            else:
                s += (xs[j+1] - xs[j])*a
            n = not n
        elif ptype0 in "FL" and ptype1 in "J7":
            if n:
                s += (xs[j+1] - xs[j])*a
            else:
                s += (xs[j+1] + 1 - xs[j])*a
        elif ptype1 in "LF":
            if n:
                s += (xs[j+1] - xs[j])*a
            n = not n
        else:
            if n:
                s += (xs[j+1] + 1 - xs[j])*a
            n = not n

print(s)
