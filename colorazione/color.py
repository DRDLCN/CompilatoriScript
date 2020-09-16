import pprint,random
import copy
k = 2
with open("colorazione/input.txt","r") as input:
    data = input.readlines()
    diz = {}
    for i in range(0,len(data)):
        primo = data[i].split("=")[0]
        diz[primo] = []
        flag = False
        for j in range(len(data)-1,i,-1):
            sx = data[j].split("=")[0]
            secondo = data[j].split("=")[1].replace("\n","").split("+")
            
            if flag == True:
                diz[primo].append(sx)
            elif primo in secondo:
                flag = True


for vertici in diz:
    for v2 in diz[vertici]:
        if vertici not in diz[v2]:
            diz[v2].append(vertici)

g = copy.deepcopy(diz)
print("+++++++++++++++++++++++")
print("INTERFERENCE GRAPH = ")     
pprint.pprint(diz)
print("+++++++++++++++++++++++")


reverse = []


G = 1
while(g != {}):
    print("G{}".format(G))
    deleted = None
    new = copy.deepcopy(g)
    for vertici in g:
        if len(g[vertici]) < k:
            print("ELIMINO {} PERCHE' HA MENO DI {} ADIACENTI".format(vertici,k))
            deleted = vertici
            del g[vertici]
            for v in g:
                if vertici in g[v]:
                    g[v].remove(vertici)
            break
    toSpilled = None
    if g != {}:
        toSpill = True
        for vertici in g:
            if len(g[vertici]) < k:
                toSpill = False
        if toSpill:
            r = random.randint(0,(len(g.keys())-1))
            toSpilled = list(g.keys())[r]
            del g[list(g.keys())[r]]
            for v in g:
                if toSpilled in g[v]:
                    g[v].remove(toSpilled)
            print("TUTTI I NODI HANNO >= {} ADIACENTI".format(k))
            print("CONTRASSEGNO {} COME TOSPILL".format(toSpilled))
    new["toSpilled"] = toSpilled
    new["deleted"] = deleted
    reverse.append(new)
    pprint.pprint(g)
    print("-----------------------------------")
    G += 1


print("PERCORRO AL CONTRARIO I GRAFI E COLORO, IGNORANDO I TOSPILL")
colori = dict.fromkeys(list(diz.keys()),None)
for grafo in reverse[::-1]:
    if grafo["deleted"] != None:
        if grafo[grafo["deleted"]] == []:
            colori[grafo["deleted"]] = random.randint(1,2)
        elif grafo[grafo["deleted"]] != []:
            if colori[grafo[grafo["deleted"]][0]] == 1:
                colori[grafo["deleted"]] = 2
            else:
                colori[grafo["deleted"]] = 1
pprint.pprint(colori)