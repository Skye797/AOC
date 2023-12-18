from readFile import readFile as r
from collections import defaultdict
import math
from copy import deepcopy
from gratheory import Graph

inp = [list(i) for i in r(16)]
[list(i) for i in '''.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....'''.split("\n")]
#print((inp))
E = (0,1)
W = (0,-1)
N = (-1,0)
S = (1,0)
c = {}
r = {}

def nextIJ(i,j,d):
    #if (i,j,d) in c.keys():
    #    return c[(i,j,d)]
    #print(i,j,inp[i][j], d)
    if inp[i][j] == '.':
        #print("a")
        return [(i+d[0],j+d[1],d)]
    elif inp[i][j] == "-":
        if d[0] == 0:
            return [(i+d[0],j+d[1],d)]
        return [(i,j-1,W),(i,j+1,E)]
    elif inp[i][j] == "|":
        if d[1] == 0:
            return [(i+d[0],j+d[1],d)]
        return [(i-1,j,N),(i+1,j,S)]
    elif inp[i][j] == "/":
        if d == E:
            return [(i-1,j,N)]
        if d == W:
            return [(i+1,j,S)]
        if d == N:
            return [(i,j+1,E)]
        if d == S:
            return [(i,j-1,W)]
    elif inp[i][j] == "\\":
        if d == W:
            return [(i-1,j,N)]
        if d == E:
            return [(i+1,j,S)]
        if d == S:
            return [(i,j+1,E)]
        if d == N:
            return [(i,j-1,W)]
def run(s):
    stack = [s]
    found = []
    
    while stack != []:
        n = stack.pop(0)
        if 0 <= n[0] < len(inp) and 0 <= n[1] < len(inp[0]) and n not in found:
            found.append(n)
            a = nextIJ(*n)
            stack += a
            #c[n] = a
            #f = [i[:2] for i in found]
            #print(a)
            #print("\n".join(["".join(["#" if (i,j) in f else " " for j in range(len(inp[0]))]) for i in range(len(inp))]))
    
    f = [i[:2] for i in found]
    return len(set(f))
#print("\n".join(["".join(["#" if (i,j) in f else " " for j in range(len(inp[0]))]) for i in range(len(inp))]))
#print(len(set(f)))
print(run((0,0,E)))
m = 0
for i in range(len(inp)):
    print("\r{:.2f}".format(i/(len(inp)+len(inp[0]))), end="")
    m = max(m, run((i,0,E)))
    m = max(m, run((i,len(inp[0])-1,W)))
for j in range(len(inp[0])):
    m = max(m, run((0,j,S)))
    m = max(m, run((len(inp)-1,j,N)))
    print("\r{:.2f}".format((j+len(inp))/(len(inp)+len(inp[0]))),end="")
print()
print(m)
