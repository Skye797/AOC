from readFile import readFile as r
from collections import defaultdict
import math
import gratheory

N, E, S, W = ((lambda x,i=i,j=j: (x[0]+i,x[1]+j)) for i, j in [(-1,0), (0,1), (1,0), (0,-1)])

inp = [[j for j in i] for i in r(10)]
[[j for j in i] for i in '''..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........'''.split("\n")]


def getConnections(char, loc, m):
    if char == "S":
        cs = []
        if m[loc[0]+1][loc[1]] in "|LJ":
            cs.append((loc,S(loc), 1))
        if m[loc[0]][loc[1]+1] in "-J7":
            cs.append((loc,E(loc), 1))
        if m[loc[0]-1][loc[1]] in "|7F":
            cs.append((loc,N(loc), 1))
        if m[loc[0]][loc[1]-1] in "-LF":
            cs.append((loc,W(loc), 1))
        return cs
    if char == "|":
        return [(loc,N(loc), 1), (loc,S(loc), 1)]
    if char == "-":
        return [(loc,E(loc), 1), (loc,W(loc), 1)]
    if char == "L":
        return [(loc,N(loc), 1), (loc,E(loc), 1)]
    if char == "J":
        return [(loc,N(loc), 1), (loc,W(loc), 1)]
    if char == "7":
        return [(loc,W(loc), 1), (loc,S(loc), 1)]
    if char == "F":
        return [(loc,E(loc), 1), (loc,S(loc), 1)]
    return []


edges = []
for i, x in enumerate(inp):
    for j, y in enumerate(x):
        edges += getConnections(y, (i,j), inp)
        if y == "S":
            start = (i,j)

graph = gratheory.Graph(edges, oneWayEdges=True)
loop = graph.BFS(start)
print(len(loop)//2)

edges2 = []
for i, x in enumerate(inp):
    for j, y in enumerate(x):
        if (i,j) not in loop:
            edges2 += [((i,j), k, 1) for k in list(filter(lambda x:x not in loop and 0<=x[0]<len(inp) and 0<=x[1]<len(inp[0]), [(i,j+1), (i,j-1), (i+1,j), (i-1,j)]))]

#for i in range(len(inp)):
#    edges2 += [((i,-1),(i+1,-1), 1), ((i,len(inp[0])), (i+1, len(inp[0])), 1), ((i,-1),(i-1,-1), 1), ((i,len(inp[0])), (i-1, len(inp[0])), 1)]
#for j in range(len(inp[0])):
#    edges2 += [((-1,j),(-1,j+1), 1), ((len(inp),j), (len(inp), j+1), 1), ((-1,j),(-1,j-1), 1), ((len(inp),j), (len(inp), j-1), 1)]

loop = graph.DFS(start) #in order
toSearchFrom = [[],[]] # if going up: right, left (loop+1 will be -1,0)
#right: down, up (0,1)
#down: left, right (1,0)
#left: up, down (0,-1)

for a, (i,j) in enumerate(loop[:-1]):
    if loop[a+1][0]-i == -1 or i-loop[a-1][0] == -1:
        if (i,j+1) not in loop and j+1 != len(inp[0]):
            toSearchFrom[0].append((i,j+1))
        if (i,j-1) not in loop and j-1 != -1:
            toSearchFrom[1].append((i,j-1))
    if loop[a+1][0]-i == 1 or i-loop[a-1][0] == 1:
        if (i,j-1) not in loop and j-1 != -1:
            toSearchFrom[0].append((i,j-1))
        if (i,j+1) not in loop and j+1 != len(inp[0]):
            toSearchFrom[1].append((i,j+1))
    if loop[a+1][1]-j == 1 or j-loop[a-1][1] == 1:
        if (i+1,j) not in loop and i+1 != len(inp): 
            toSearchFrom[0].append((i+1,j))
        if (i-1,j) not in loop and i-1 != -1:
            toSearchFrom[1].append((i-1,j))
    if loop[a+1][1]-j == -1 or j-loop[a-1][1] == -1:
        if (i-1,j) not in loop and i-1 != -1:
            toSearchFrom[0].append((i-1,j))
        if (i+1,j) not in loop and i+1 != len(inp):
            toSearchFrom[1].append((i+1,j))

onSide0 = set()
onSide1 = set()

graph2 = gratheory.Graph(edges2, oneWayEdges=True)
for i in range(len(inp)):
    for j in range(len(inp[0])):
        graph2.addVertex((i,j),raiseError=False)
for i in toSearchFrom[0]:
    if i not in onSide0:
        onSide0.update(set(graph2.BFS(i)))
for i in toSearchFrom[1]:
    if i not in onSide1:
        onSide1.update(set(graph2.BFS(i)))
 

if (0,0) in onSide0:
    print(len([0 for i, j in onSide1 if (i,j) not in loop]))
if (0,0) in onSide1:
    print(len([0 for i, j in onSide0 if (i,j) not in loop]))   

inp = [[" " for i in j] for j in inp]

for i, j in onSide0:
    inp[i][j] = "0"
for i, j in onSide1:
    inp[i][j] = "1"
