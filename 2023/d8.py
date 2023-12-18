from readFile import readFile as r
from collections import defaultdict
import math

inp = r(8)
'''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''.split("\n")


def coords(s):
    i = 0
    for j in s:
        i *= 128
        i += ord(j)
    return i

def loc(c):
    s = ""
    while c != 0:
        s = chr(c%128) + s
        c //=128
    return s

d = {(coords(i[:3]),0):coords(i[7:10]) for i in inp[2:]}
d.update({(coords(i[:3]),1):coords(i[12:15]) for i in inp[2:]})
'''
c = coords('AAA')
e = coords('ZZZ')
s = 0
while c != e:
    for i in inp[0]:
        c = d[(c,i=="R")]
        s += 1
        if c == e:
            break
        
print(s)
'''
def findCycles(repeatLen, prevcs, matches):
    # have (offset, range)
    i = len(prevcs)-1 - repeatLen
    while i > 0:
        for j in range(len(prevcs[i])):
            if prevcs[-1][j] % 128 == ord("Z") and not matches[j][2]:
                if prevcs[i][j] == prevcs[-1][j]:
                    matches[j] = (i,len(prevcs)-i-1, True)
        i -= repeatLen
    

cs = [coords(i[:3]) for i in inp[2:] if i[2] == "A"]
matches = [(0,0,False) for i in range(len(cs))] #answer will require s = a+x*b = ... = ... for (a,b) in list for any integer x
# which means that (s-a)%b == 0 
prevcs = [cs[:]]
s = 0
rLen = len(inp[0])
while not all(map(lambda x: x[2],matches)):
    for i in inp[0]:
        cs = list(map(lambda x:d[(x,i=="R")], cs))
        prevcs.append(cs[:])
        if all(map(lambda x: x[2],matches)):
            break
    findCycles(rLen, prevcs, matches)
print(matches)
xs = [0 for i in range(len(matches))]
def getS(xs,matches):
    return [matches[i][0] + xs[i]*matches[i][1] for i in range(len(xs))]
def increase(s):
    return min([i for i in range(len(s))], key=lambda x:s[x])
def valid(s):
    return all(map(lambda x:s[0]==x, s))
s = (getS(xs,matches))
c = 0
while not valid(s):
    xs[increase(s)] += 1
    s = getS(xs,matches)
    c += 1
    if c %10000 == 0:
        print("\r{:}, {:}".format(c, valid(s[:2])),end="")
print(s)
