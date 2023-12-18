from readFile import readFile as r
from collections import defaultdict
import math

class smartDict:
    
    def __init__(self):
        self.dests = []
        self.source = []
        self.rang = []
    
    def __getitem__(self, index):
        if not isinstance(index, slice):
            for i, j in enumerate(self.source):
                if j <= index < j+self.rang[i]:
                    return self.dests[i] + (index - j)
            return index
        else:
            start, end, step = index.start, index.stop, index.step
            startinrang = []
            for i, j in enumerate(self.source):
                if j <= start < j+self.rang[i]: #if the start is between the current dict values
                    if end >= j+self.rang[i]:
                        nextranges = self[j+self.rang[i]:end]
                        end = j+self.rang[i]
                    else:
                        nextranges = []
                    return [range(self.dests[i]+(start-j),self.dests[i]+(end-j))] + nextranges
                elif start < j < end: # if the current dict values start in the middle of the range
                    startinrang.append(i)
            if len(startinrang) != 0:
                best = min(startinrang, key=lambda x:self.source[x])
                return [range(start,self.source[best])] + self[self.source[best]:end]
            return [range(start,end)]
    
    def update(self, dest, source, rang):
        self.dests.append(dest)
        self.source.append(source)
        self.rang.append(rang)
    
        

inp = r(6)

times = [62, 73, 75, 65]
distances = [644, 1023, 1240, 1023]

def nWays(time, distance): #Formula for distance is (t-x)*x >= distances : -x^2+tx-d = 0 : (t+/-sqrt(t^2-4d))/2
    return math.ceil((time+math.sqrt(time**2-4*distance))/2) - math.floor((time-math.sqrt(time**2-4*distance))/2) -1 

print(nWays(7,9))
print(nWays(15,40))

print(nWays(30,200))

a = 1
for i, j in zip(times, distances):
    a *= nWays(i,j)
    
print(a)

inp = [int("".join(filter(lambda x:x.isdigit(), i))) for i in inp]

print(nWays(inp[0],inp[1]))
    