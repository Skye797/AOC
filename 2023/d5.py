from readFile import readFile as r
from collections import defaultdict

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
    
        
                
        

inp = "\n".join(r(5)).split("\n\n")


seeds = [int(i) for i in inp[0].split(" ")[1:]]

maps = []

for i in inp[1:]:
    a = i.split("\n")
    maps.append(smartDict())
    for j in a[1:]:
        dest, source, l = (int(k) for k in j.split(" "))
        maps[-1].update(dest, source, l)


locs = []
for i in seeds:
    a = i
    for j in maps:
        a = j[a]
    locs.append(a)

print(min(locs))
        
    
seeds = [range(i,i+j) for (i,j) in zip(seeds[::2],seeds[1::2])]
for j in maps:
    new = []
    for i in seeds:
        new += j[i.start:i.stop]
    seeds = new

print(seeds)
print(min(seeds, key=lambda x:x.start).start)

    
