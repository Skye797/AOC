from readFile import readFile as r
from collections import defaultdict
import math
from copy import deepcopy
import gratheory

inp = [[int(i) for i in j] for j in r(17)]
[[int(i) for i in j] for j in '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''.split("\n")]
[[int(i) for i in j] for j in '''111111111111
999999999991
999999999991
999999999991
999999999991'''.split("\n")]


N,E,S,W = 0,1,2,3
dic = {N:(lambda i,j:(i-1,j)), E:(lambda i,j:(i,j+1)), S:(lambda i,j:(i+1,j)), W:(lambda i,j:(i,j-1))}
# for run lengths of 1,2 or 3 if a run length of 3 just assert that next is not in the same direction
best = [[[[gratheory.inf() for _ in range(4)] for a in range(3)] for i in range(len(inp[0]))] for j in range(len(inp))]
best[0][1][0][E] = inp[0][1]
best[1][0][0][S] = inp[1][0]
posTurns = {N:[E,W], E:[S,N], S:[E,W], W:[N,S]}
#point => (i,j,runlength,direction)
# (i,j,k,d) => (i+a,j+b,k+1,d) weighting inp[i][j]
# => (i+a,j+b,0,!d) weighting inp[i][j]
'''
edges = []
for i in range(len(inp)):
    for j in range(len(inp[0])):
        for d in range(4):
            newi,newj = dic[d](i,j)
            if 0 <= newi < len(inp) and 0 <= newj < len(inp[0]):
                for r in range(0,2):
                    edges.append((((i,j),r,d), ((newi,newj),r+1,d), inp[newi][newj]))
            for d_ in posTurns[d]:
                newi,newj = dic[d_](i,j)
                if 0 <= newi < len(inp) and 0 <= newj < len(inp[0]):
                    for r in range(0,3):
                        edges.append((((i,j),r,d), ((newi,newj),0,d_), inp[newi][newj]))
for d in range(4):
    edges.append(("start",((0,0),0,d), 0))
    for r in range(3):
        edges.append((((len(inp)-1,len(inp[0])-1), r, d), "end", 0))
g = gratheory.Graph(edges,oneWayEdges=True)
s = g.findShortestPath("start","end")
a = [[" " for i in j] for j in inp]
for i in s[0][1:-1]:
    a[i[0][0]][i[0][1]] = "X"
print("\n".join(["".join(i) for i in a]))
print(s[1])
'''

def doPass():
    c = 0 
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if i != 0:
                for a in range(3):
                    if a < 2:
                        if best[i-1][j][a][S] + inp[i][j] < best[i][j][a+1][S]:
                            best[i][j][a+1][S] = best[i-1][j][a][S]+inp[i][j]
                            c += 1
                    for b in [E,W]:
                        if best[i-1][j][a][b] + inp[i][j] < best[i][j][0][S]:
                            best[i][j][0][S] = best[i-1][j][a][b]+inp[i][j]
                            c += 1
                            
            if i != len(inp)-1:
                for a in range(3):
                    if a < 2:
                        if best[i+1][j][a][N] + inp[i][j] < best[i][j][a+1][N]:
                            best[i][j][a+1][N] = best[i+1][j][a][N]+inp[i][j]
                            c += 1
                    for b in [E,W]:
                        if best[i+1][j][a][b] + inp[i][j] < best[i][j][0][N]:
                            best[i][j][0][N] = best[i+1][j][a][b]+inp[i][j]
                            c += 1
                            
            if j != 0:
                for a in range(3):
                    if a < 2:
                        if best[i][j-1][a][E] + inp[i][j] < best[i][j][a+1][E]:
                            best[i][j][a+1][E] = best[i][j-1][a][E]+inp[i][j]
                            c += 1
                    for b in [N,S]:
                        if best[i][j-1][a][b] + inp[i][j] < best[i][j][0][E]:
                            best[i][j][0][E] = best[i][j-1][a][b]+inp[i][j]
                            c += 1
            
            if j != len(inp[0])-1:
                for a in range(3):
                    if a < 2:
                        if best[i][j+1][a][W] + inp[i][j] < best[i][j][a+1][W]:
                            best[i][j][a+1][W] = best[i][j+1][a][W]+inp[i][j]
                            c += 1
                    for b in [N,S]:
                        if best[i][j+1][a][b] + inp[i][j] < best[i][j][0][W]:
                            best[i][j][0][W] = best[i][j+1][a][b]+inp[i][j]
                            c += 1
    return c

def toString(i):
    if isinstance(i, gratheory.inf):
        return "inf"
    else:
        return str(i)


a = 0
while doPass() != 0:
    a += 1
    print("\rNumber of passes completed: {0:.0f}. Current result: {1:}              ".format(a,toString(min(map(min,best[-1][-1])))), end="")
print()
print(min(map(min,best[-1][-1])))


N,E,S,W = 0,1,2,3
dic2 = {N:(lambda i,j:(i+1,j)), E:(lambda i,j:(i,j-1)), S:(lambda i,j:(i-1,j)), W:(lambda i,j:(i,j+1))}
# for run lengths of 1,2 or 3 if a run length of 3 just assert that next is not in the same direction
best = [[[[gratheory.inf() for _ in range(4)] for a in range(10)] for i in range(len(inp[0]))] for j in range(len(inp))]
best[0][1][0][E] = inp[0][1]
best[1][0][0][S] = inp[1][0]
posTurns = {N:[E,W], E:[S,N], S:[E,W], W:[N,S]}

'''
edges = []
for i in range(len(inp)):
    for j in range(len(inp[0])):
        for d in range(4):
            newi,newj = dic[d](i,j)
            if 0 <= newi < len(inp) and 0 <= newj < len(inp[0]):
                for r in range(0,10):
                    edges.append((((i,j),r,d), ((newi,newj),r+1,d), inp[newi][newj]))
            for d_ in posTurns[d]:
                newi,newj = dic[d_](i,j)
                if 0 <= newi < len(inp) and 0 <= newj < len(inp[0]):
                    for r in range(3,11):
                        edges.append((((i,j),r,d), ((newi,newj),0,d_), inp[newi][newj]))
for d in range(4):
    edges.append(("start",((0,0),0,d), 0))
    for r in range(11):
        edges.append((((len(inp)-1,len(inp[0])-1), r, d), "end", 0))
g = gratheory.Graph(edges,oneWayEdges=True)
s = g.findShortestPath("start","end")
a = [[" " for i in j] for j in inp]
for i in s[0][1:-1]:
    a[i[0][0]][i[0][1]] = "X"
print("\n".join(["".join(i) for i in a]))
print(s[1])
'''

def doPass_():
    c = 0 
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            for d in range(4):
                newi,newj = dic[d](i,j)
                if 0 <= newi < len(inp) and 0 <= newj < len(inp[0]):
                    for r in range(9):
                        if best[i][j][r][d] + inp[newi][newj] < best[newi][newj][r+1][d]:
                            best[newi][newj][r+1][d] = best[i][j][r][d] + inp[newi][newj]
                            c += 1
                for newD in posTurns[d]:
                    newi,newj = dic[newD](i,j)
                    if 0 <= newi < len(inp) and 0 <= newj < len(inp[0]):
                        for r in range(3,10):
                            if best[i][j][r][d] + inp[newi][newj] < best[newi][newj][0][newD]:
                                best[newi][newj][0][newD] = best[i][j][r][d] + inp[newi][newj]
                                c += 1
                        
    return c

    

a = 0
while doPass_() != 0:
    a += 1
    print("\rNumber of passes completed: {0:.0f}. Current result: {1:}          ".format(a,toString(min(map(min,best[-1][-1][3:])))), end="")
print()
print(min(map(min,best[-1][-1][3:])))
print(len(inp)*len(inp[0])*4*10)
