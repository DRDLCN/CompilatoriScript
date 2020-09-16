primo = None
with open("firstfollow/input.txt","r") as input:
    data = input.readlines()
    diz = {}
    for nonterm in data:
        lect = nonterm.split(" → ")[0]
        if primo == None:
            primo = lect
        diz[lect] = []
        pro = nonterm.replace("\n","").split(" → ")[1]
        for s in pro.split(" | "):

            diz[lect].append(s.split(" "))
        

first = {}
for x in diz:
    first[x] = set()


def isTerminals(c):
    if c.isupper() == True or "'" in c or "ε" in c:
        return False
    elif c.islower() == True or c.isalpha() == False:
        return True

def firstTerminals():

    print("-----------------------------------------")
    print("FIRST DEI TERMINALI")
    for t in diz:
        for p in diz[t]:
            for c in p:
                if isTerminals(c) and c not in first:
                    first[c] = set()
                    first[c].add(c)
                    print("FIRST( {} ) = {{{}}}".format(c,c))
                    

def isNullable(ins):
    if "ε" in ins:
        return True
    return False

firstTerminals()
g = {}
while(g != first):
    g = dict(first)
    print("-----------------------------------------")
    for t in diz:
        for p in diz[t]:
            for c in p:
                if c != "ε":
                    if c in first:
                        first[t] = first[t].union(first[c])
                    if not isNullable(first[c]):
                        flag = True
                        break
        for p in diz[t]:
            if "ε" in p:
                first[t].add("ε")
                break
    
    for x in first:
        print("FIRST( {} ) = {}".format(x,first[x]))
    

print("************************************************FOLLOW************************************************")

follow = {}
c = 0
for x in diz:
    if c == 0:
        follow[x] = set("$")
    else:
        follow[x] = set()
    c += 1
        

def checkForma(index,produzione):
    try:
        if produzione[index+1]:
            return 2,produzione[index+1]
    except:
        return 1,None
    
g = {}
while(g != follow):
    g = dict(follow)
    print("-----------------------------------------")
    for B in diz:
        for A in diz:
            for p in diz[A]:
                if B in p:
                    for x in range(0,len(p)):
                        if not isTerminals(p[x]) and p[x] == B:
                            forma,beta = checkForma(x,p)
                            if forma == 1:
                                follow[B] = follow[B].union(follow[A])
                            if forma == 2:
                                follow[B] = follow[B].union(first[beta] - set("ε"))
                            if forma == 2 and "ε" in first[beta]:
                                follow[B] = follow[B].union(follow[A])
    for x in follow:
        print("FOLLOW( {} ) = {}".format(x,follow[x]))