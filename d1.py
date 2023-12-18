from readFile import readFile as r

inp = r(1)
digs = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

def toInt(s):
    s = [i for i in s if i.isdigit()]
    return int(s[0]+s[-1])

def toInt2(s):
    b = []
    i = 0
    for j,k in enumerate(s):
        if k.isdigit():
            b.append(k)
            i = j+1
        else:
            for a in range(i,j+1):
                if s[a:j+1] in digs.keys():
                    b.append(str(digs[s[a:j+1]]))
                    i = j
            
    return int(b[0]+b[-1])

print(sum(list(map(toInt2,inp))))