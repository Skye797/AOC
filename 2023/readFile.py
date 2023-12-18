

def readFile(day):
    
    fName = "./d"+str(day)+".txt"
    with open(fName, 'r') as f:
        inp = f.read().split("\n")
    
    return inp
