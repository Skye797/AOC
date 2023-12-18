from readFile import readFile as r
from collections import defaultdict

inp = r(3)

def inrangeofsymbol(row, start, end, symbols):
    r = []
    for i in range(row-1, row+2):
        for j in range(start-1, end+2):
            if (i,j) in symbols:
                return True
    return False

def whichSymbol(row,start,end,symbols):
    r = []
    for i in range(row-1, row+2):
        for j in range(start-1, end+2):
            if (i,j) in symbols:
                r.append((i,j))
    return r

symbols = []

for i in range(len(inp)):
    for j in range(len(inp)):
        if inp[i][j] != '.' and not inp[i][j].isdigit():
            symbols.append((i,j))

digitlocs = []

for i in range(len(inp)):
    for j in range(len(inp)):
        if inp[i][j].isdigit():
            digitlocs.append((i,j))

digits = []
lrow, lcol = -1, -1
for (i,j) in digitlocs:
    if i == lrow and j == lcol+1:
        digits[-1][3] += 1
        lcol += 1
    else:
        digits.append([0,i,j,j])
        lrow, lcol = i,j

s = 0

for i in digits:
    if inrangeofsymbol(i[1], i[2], i[3], symbols):
        s += int(inp[i[1]][i[2]:i[3]+1])

print(s)

stars = []
for i in range(len(inp)):
    for j in range(len(inp)):
        if inp[i][j] == '*':
            stars.append((i,j))

starsDict = defaultdict(lambda :[])

for i in digits:
    r = whichSymbol(i[1], i[2], i[3], stars)
    for j in r:
        starsDict[j].append(i)

s = 0

for i in starsDict.keys():
    if len(starsDict[i]) == 2:
        k = starsDict[i]
        a, b = k[0], k[1]
        s += int(inp[a[1]][a[2]:a[3]+1]) * int(inp[b[1]][b[2]:b[3]+1])
         
print(s)
# number, row, start, end

