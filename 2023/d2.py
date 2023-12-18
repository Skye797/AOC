from readFile import readFile as r

m = {"red":12, "green":13, "blue":14}

inp = r(2)
def form(i):
    a, b = i.split(": ")
    a = int(a[5:])
    #print(b)
    #print([{i.split(" ")[1]:i.split(" ")[0] for i in j.split(", ")} for j in b.split("; ")])
    b = [{i.split(" ")[1]:int(i.split(" ")[0]) for i in j.split(", ")} for j in b.split("; ")]
    
    return (a,b)

inp = list(map(form, inp))
s = 0
for a,b in inp:
    valid = True
    for c in b:
        for d in m.keys():
            if d in c.keys():
                if c[d] > m[d]:
                    valid = False
    if valid:
        s += a

print(s)

s = 0
for a,b in inp:
    m = {"red":0, "green":0, "blue":0}
    for c in b:
        for d in m.keys():
            if d in c.keys():
                if c[d] > m[d]:
                    m[d] = c[d]
    k = 1
    for i in m.values():
        k *= i
    s += k

print(s)
