from readFile import readFile as r
from collections import defaultdict
import math

inp = list(map(lambda x:[x[0],tuple(int(j) for j in x[1].split(","))], [i.split(" ") for i in r(12)]))
list(map(lambda x:[x[0],tuple(int(j) for j in x[1].split(","))], [i.split(" ") for i in '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''.split("\n")]))

N = {}
a,b = 0,0

def nWays_(ms,gs):
    global a,b
    if (ms,gs) in N.keys():
        a+=1
        return N[(ms,gs)]
    b += 1
    result = nWays_2(ms,gs)
    N[(ms,gs)] = result
    return result

def nWays_2(ms,gs):

    if ms == () and gs == ():
        return 1
    elif ms == () and gs != ():
        return 0
    if gs == ():
        if all(map(lambda x:x=="?","".join(ms))):
            return 1
        else:
            return 0
    c = 0
    if len(ms[0]) >= gs[0]:
        #if the first string is longer than the first group
        #then it can contain the list of springs
        for i in range(len(ms[0])-gs[0]+1): #for each way of choosing the correct length of spring
            if len(ms[0])-i == gs[0]: #make sure the following character is either not in the string
                c += nWays_(ms[1:],gs[1:]) # if not in the string we can just use the case that the entire current
                                          # m0 is used for g0
            elif ms[0][i+gs[0]] == '?': #or is unknown
                if i + gs[0] + 1 == len(ms[0]) :
                    c += nWays_(ms[1:], gs[1:]) #there is no m after unknown m
                    
                else:
                    c += nWays_((ms[0][i+gs[0]+1:],)+ms[1:], gs[1:]) # then we can keep the rest of m after the unknown val
            if ms[0][i] == '#': #if the substring starts with spring then the first group must start there
                break
    if all(map(lambda x:x=="?", ms[0])):
        c += nWays_(ms[1:], gs)
            #if the following character is # then it cannot be where the group ends and is ignored
    #there is also the case that gs[0] does not apply to ms[0]  if all ms[0] is ?
    
    return c

def nWays(m): #m is map of springs str, l is list of groups [int]
    # we want ".?.??..#.##" [1,1,2] -> ["??","?","#","##"], [1,1,2]
    # two options : the first group contains the first working spring if it contains question marks
    # or : the next group contains the list of working springs
    # can speed this up by identifying fixed group sizes
    ms = tuple(filter(lambda x:x!="", tuple(m[0].split("."))))
    return nWays_(ms, m[1])

print(sum(map(nWays,inp)))

inp = list(map(lambda x:[("?".join(5*[x[0]])), tuple(x[1]*5)], inp))
s = 0
c = 1

for i in range(len(inp)):
    print("\r{:.2f}%".format(c/10), end="")
    c += 1
    s += nWays(inp[i])
print()
print(s)
print("Fraction of times dictionary used compared to non dictionary: {:.2f}".format(a/(a+b)))
