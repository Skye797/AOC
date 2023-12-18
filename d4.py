from readFile import readFile as r
from collections import defaultdict

inp = r(4)

def points(c):
    w, n = c[len("Card   1:"):].split(" |")
    w = set(map(lambda x : int(x[0]+x[1]),zip(w[1::3], w[2::3])))
    n = set(map(lambda x : int(x[0]+x[1]),zip(n[1::3], n[2::3])))
    c = len(w.intersection(n))
    if c == 0:
        return 0
    return 2**(c-1)

print(sum(map(points, inp)))

test='''Card   1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card   2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card   3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card   4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card   5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card   6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''.split("\n")


def nMatches(c):
    w, n = c[len("Card   1:"):].split(" |")
    w = set(map(lambda x : int(x[0]+x[1]),zip(w[1::3], w[2::3])))
    n = set(map(lambda x : int(x[0]+x[1]),zip(n[1::3], n[2::3])))
    c = len(w.intersection(n))
    return c

a = list(map(nMatches, inp))
ncopies = {i:1 for i in range(len(inp))}
for i, j in enumerate(a):
    b = ncopies[i]
    for k in range(1,j+1):
        ncopies[i+k] += b

print(sum(ncopies.values()))
    