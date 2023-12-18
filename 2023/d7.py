from readFile import readFile as r
from collections import defaultdict
import math

dic = {"A":14,"K":13,"Q":12,"J":11,"T":10}
dic.update({str(i):i for i in range(2,10)})

#five -> four -> full house -> three -> two pair -> one pair -> high card

def value(cards):
    v = 0
    tdic = {i:0 for i in dic.keys()}
    for i in cards:
        tdic[i] += 1
    
    counts = sorted(list(filter(lambda x:x != 0, tdic.values())), reverse=True)
    if counts == [5]:
        v += 6
    elif counts == [4,1]:
        v += 5
    elif counts == [3,2]:
        v += 4
    elif counts == [3,1,1]:
        v += 3
    elif counts == [2,2,1]:
        v += 2
    elif counts == [2,1,1,1]:
        v += 1
    for i in cards:
        v *= 15
        v += dic[i]
    return v

inp = r(7)

ranks = sorted(inp, key=lambda x:value(x[:5]))
s = 0
for i in range(len(ranks)):
    s += (i+1)*int(ranks[i][6:])
print(s)

def value2(cards):
    dic['J'] = 1
    v = 0
    tdic = {i:0 for i in dic.keys()}
    for i in cards:
        tdic[i] += 1
    nJokers = tdic["J"]
    tdic['J'] = 0
    counts = sorted(list(filter(lambda x:x != 0, tdic.values())), reverse=True)
    if nJokers == 5:
        counts = [5]
        nJokers = 0
    for i in range(nJokers):
        counts[0] += 1
    if counts == [5]:
        v += 6
    elif counts == [4,1]:
        v += 5
    elif counts == [3,2]:
        v += 4
    elif counts == [3,1,1]:
        v += 3
    elif counts == [2,2,1]:
        v += 2
    elif counts == [2,1,1,1]:
        v += 1
    for i in cards:
        v *= 15
        v += dic[i]
    return v

ranks = sorted(inp, key=lambda x:value2(x[:5]))
s = 0
for i in range(len(ranks)):
    s += (i+1)*int(ranks[i][6:])
print(s)
