from readFile import readFile as r
from collections import defaultdict
import math

inp = [[i for i in j] for j in r(11)]

[[i for i in j] for j in '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''.split("\n")]

def expand(m):
    rows, cols = [], []
    for row in range(len(m)):
        if all(map(lambda x:x=='.', m[row])):
            rows.append(row)
    for col in range(len(m[0])):
        if all(map(lambda x:x=='.', [m[i][col] for i in range(len(m))])):
            cols.append(col)
    c = 0
    while rows != []:
        nIncrease = rows.pop(0) + c
        m.insert(nIncrease,['.' for i in range(len(m[0]))])
        c += 1
    c = 0
    while cols != []:
        nIncrease = cols.pop(0) + c
        for i in range(len(m)):
            m[i].insert(nIncrease,'.')
        c += 1

expand(inp)

def calcDist(a,b):
    x1,y1 = a
    x2,y2 = b
    return abs(x2-x1) + abs(y2-y1)

s = 0
gals = [(i,j) for i in range(len(inp)) for j in range(len(inp[0])) if inp[i][j] == "#"]
for i, a in enumerate(gals):
    for j, b in enumerate(gals[(i+1):]):
        s += calcDist(a,b)
print(s)



def expand2(m):
    rows, cols = [], []
    for row in range(len(m)):
        if all(map(lambda x:x=='.', m[row])):
            rows.append(row)
    for col in range(len(m[0])):
        if all(map(lambda x:x=='.', [m[i][col] for i in range(len(m))])):
            cols.append(col)
    return rows, cols

def calcDist2(a,b,rows,cols):
    x1,y1 = a
    x2,y2 = b
    mx, my, Mx, My = min(x1,x2), min(y1,y2), max(x1,x2), max(y1,y2)
    return Mx-mx + My-my + (10**6-1)*(len([0 for i in range(mx,Mx) if i in rows])
                                      +len([0 for i in range(my,My) if i in cols]))

inp = [[i for i in j] for j in r(11)]
rows, cols = expand2(inp)
s = 0
gals = [(i,j) for i in range(len(inp)) for j in range(len(inp[0])) if inp[i][j] == "#"]
for i, a in enumerate(gals):
    for j, b in enumerate(gals[(i+1):]):
        s += calcDist2(a,b,rows,cols)
print(s)
