from readFile import readFile as r
from collections import defaultdict
import math

inp = r(9)

def findNext(l):
    d = [l[i+1]-l[i] for i in range(len(l)-1)]
    if all(list(map(lambda x:x==0, d))):
        return l[-1]
    else:
        return findNext(d)+l[-1]
    
s = sum(map(lambda x:findNext([int(i) for i in x.split(" ")]), inp))

print(s)

def findNext_(l):
    d = [l[i+1]-l[i] for i in range(len(l)-1)]
    if all(list(map(lambda x:x==0, d))):
        return l[0]
    else:
        return -findNext_(d)+l[0]


s = sum(list(map(lambda x:findNext_([int(i) for i in x.split(" ")]), inp)))
print(s)