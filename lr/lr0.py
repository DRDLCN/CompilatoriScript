import copy
with open("lr/input.txt","r") as input:
    data = input.readlines()
    diz = {}
    for nonterm in data:
        lect = nonterm.split(" → ")[0]
        diz[lect] = []
        pro = nonterm.replace("\n","").split(" → ")[1]
        for s in pro.split(" | "):

            diz[lect].append(s.split(" "))

for t in diz:
    for p in diz[t]:
        p.insert(0,"•")

def isTerminals(c):
    if c.isupper() == True or "'" in c or "ε" in c:
        return False
    elif c.islower() == True or c.isalpha() == False:
        return True

def closure(nonterm,c):
    if not isTerminals(nonterm):
        for p in diz[nonterm]:
            if not isTerminals(p[(p.index("•") + 1)]):
                if nonterm not in c:
                    c[nonterm] = [p]
                else:
                    c[nonterm].append(p)
                if p[(p.index("•") + 1)] != nonterm and p[(p.index("•") + 1)] not in c:
                    closure(p[(p.index("•") + 1)],c)
            else:
                if nonterm not in c:
                    c[nonterm] = [p]
                else:
                    c[nonterm].append(p)
            c[-1].add((p[(p.index("•") + 1)]))
        return c
    else:
        return {}
            

def printDiz(diz):
    for k in diz:
        if k != -1:
            for p in diz[k]:
                print("{} → {}".format(k,"".join(p)))

def goTo(stato,dopoPunto):
    gotoStato = copy.deepcopy(stato)
    del gotoStato[-1]
    newStato = {-1:set()}
    for nonterm in gotoStato:
        for p in gotoStato[nonterm]:
            if dopoPunto in p:
                indexOfDP = p.index(dopoPunto)
                indexOfPunto = p.index("•")
                if indexOfDP == indexOfPunto + 1:
                    p.insert(indexOfDP+1, "•")
                    p.pop(indexOfPunto)
                    try:
                        newStato[-1].add(p[p.index("•")+1])
                    except:
                        pass
                    if nonterm not in newStato:
                        newStato[nonterm] = []
                    newStato[nonterm].append(p)
    newClosure = {}
    for nonterm in newStato[-1]:
        d = closure(nonterm,{-1:set()})
        for k in d:
            if k not in newClosure:
                newClosure[k] = d[k]
    return newStato,newClosure

lr = {0 : closure("S'",{-1:set()})}
print("CLOSURE S' -> S")
printDiz(lr[0])
daFare = [lr[0]]
g = []
while(g != daFare):
    g = list(daFare)
    for stato in daFare:
        for dopoPunto in stato[-1]:
            print("\nGOTO( {} , {} )".format(daFare.index(stato),dopoPunto))
            newStato,newClosure = goTo(stato,dopoPunto)
            printDiz(newStato)
            print("")
            printDiz(newClosure)
            merge = {}
            for k in newStato:
                if k not in merge:
                    merge[k] = []
                for p in newStato[k]:
                    merge[k].append(p)
            for k in newClosure:
                if k not in merge:
                    merge[k] = []
                for p in newClosure[k]:
                    merge[k].append(p)
            merge[-1] = set(merge[-1])
            if merge not in daFare:
                daFare.append(merge)
                print("NUOVO STATO = {}".format(daFare.index(merge)))
            else:
                print("ESISTE GIA = {}".format(daFare.index(merge)))
