from readFile import readFile as r
from collections import defaultdict
import math
from copy import deepcopy
import gratheory
import time

class rang:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def split(self, splitby):
        if splitby - self.start >0:
            if self.end - splitby >0:
                return rang(self.start,splitby), rang(splitby, self.end)
            return self, None
        return None, self
    
    def __repr__(self):
        return "range("+str(self.start)+", "+str(self.end)+")"

def toRule(rule):
    r = rule.split(":")
    if len(r) == 1:
        return ["result=True",r[0]]
    return ["result="+r[0],r[1]]

inp = [i.split("\n") for i in ("\n".join(r(19))).split("\n\n")]
workflows = {i.split("{")[0]:list(map(toRule, i.split("{")[1][:-1].split(","))) for i in inp[0]}

{i.split("{")[0]:list(map(toRule, i.split("{")[1][:-1].split(","))) for i in inp[0]}
x,m,a,s, result = 0,0,0,0, False
accepted = []
for i in inp[1]:
    for j in i[1:-1].split(","):
        exec(j)
    curr = "in"
    while curr not in ["A","R"]:
        for j in workflows[curr]:
            exec(j[0])
            if result:
                curr = j[1]
                break
    if curr == "A":
        accepted.append([x,m,a,s])
    
print(sum(map(sum,accepted)))

x,m,a,s = rang(1,4001), rang(1,4001), rang(1,4001), rang(1,4001)
workflows = {i.split("{")[0]:i.split("{")[1][:-1].split(",") for i in inp[0]}
valToRange = {"x":0, "m":1, "a":2, "s":3}
def applyRule(ranges,workflow): #workflow as a tuple (wf, r)
    r = workflows[workflow[0]][workflow[1]].split(":")
    if len(r) == 1:
        return [(ranges, (r[0], 0))]
    rToEdit = valToRange[r[0][0]]
    if r[0][1] == ">":
        splitted = ranges[rToEdit].split(int(r[0][2:])+1)
        smallerRanges = deepcopy(ranges)
        largerRanges = deepcopy(ranges)
        smallerRanges[rToEdit] = splitted[0]
        largerRanges[rToEdit] = splitted[1]
        return [(smallerRanges, (workflow[0],workflow[1]+1)), (largerRanges, (r[1], 0))]
    if r[0][1] == "<":
        splitted = ranges[rToEdit].split(int(r[0][2:]))
        smallerRanges = deepcopy(ranges)
        largerRanges = deepcopy(ranges)
        smallerRanges[rToEdit] = splitted[0]
        largerRanges[rToEdit] = splitted[1]
        return [(largerRanges, (workflow[0],workflow[1]+1)), (smallerRanges, (r[1], 0))]

allOf = [([x,m,a,s], ("in", 0))]
accepted = []
rejected = []
while allOf != []:
    curr = allOf.pop(0)
    if curr[1][0] == "A":
        accepted.append(curr[0])
    elif curr[1][0] == "R":
        rejected.append(curr[1])
    else:
        allOf += applyRule(curr[0], curr[1])

def c(ranges):
    s = 1
    for i in ranges:
        s *= (i.end-i.start)
    return s
print(sum(map(c,accepted)))