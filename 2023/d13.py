from readFile import readFile as r
from collections import defaultdict
import math
from copy import deepcopy

ROW = True
COL = False
c = 0
d = {"#":".",".":"#"}

inp = [[list(j) for j in i.split("\n")] for i in "\n".join(r(13)).split("\n\n")]
[[list(j) for j in i.split("\n")] for i in '''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

.#..##.#..#
...#..##..#
..#...##..#
..#...##..#
...#..##..#
.#..##.#..#
.#..#..##..
###.##.##.#
.###.#...#.
###.####...
##.###.#.##
#..#.#..###
.#.##...#..
#...#.#.##.
...#.#....#
####.#..###
.###.#..###'''.split("\n\n")]


def isHorRef(m,r):
    b = min(len(m)-r,r)
    return [m[a] for a in range(r-b,r)] == [m[a]for a in range(r+b-1,r-1,-1)]

def isVerRef(m, c):
    b = min(len(m[0]) - c, c)
    return [[i[a] for i in m] for a in range(c-b,c)] == [[i[a] for i in m] for a in range(c+b-1,c-1,-1)]

def findMirror(m, avoid = -1):
    for row in range(1,len(m)):
        if avoid != 100*row:
            if isHorRef(m,row):
                return ROW, row
    for col in range(1,len(m[0])):
        if avoid != col:
            if isVerRef(m,col):
                return COL, col
    return None, None

def calcPoints(m, avoid = -1):
    isRow, p = findMirror(m, avoid=avoid)
    if isRow == None:
        return None
    return (isRow*100+(not isRow))*p

def flip(m,i,j):
    m[i][j] = d[m[i][j]]

def testSmudge(m):
    global c
    isRow, p = None, None
    originalSol = calcPoints(m)
    sols = set()
    for i in range(len(m)):
        for j in range(len(m[0])):
            flip(m,i,j)
            p = calcPoints(m, avoid=originalSol)
            if p != None:
                sols.add(p)
                #return (isRow*100+(not isRow))*p
            flip(m,i,j)
    sols = list(filter(lambda x:x!=originalSol,list(sols)))
    return sols[0]
print(sum(map(testSmudge,inp)))
print(c, len(inp))
