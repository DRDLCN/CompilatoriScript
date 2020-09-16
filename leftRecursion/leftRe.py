with open("leftRecursion/input.txt","r") as input:
    data = input.readlines()
    diz = {}
    for nonterm in data:
        diz[nonterm.split(" → ")[0]] = nonterm.split(" → ")[1].split("|")
        diz[nonterm.split(" → ")[0]][-1] = diz[nonterm.split(" → ")[0]][-1].replace("\n","") 


print(diz)

#1
y = 1
l = []
for x in diz:
    print(x+ ":A" + str(y))
    y += 1
    l.append(x)

def eliminaRicorsioneImmediata(i):
    prefix = l[i][0]
    flag = False
    print("Ric.Immediata su ",end="")
    for p in diz[l[i]]:
        if p.startswith(prefix):
            print(prefix + " → "+ p,end="   ")
            flag = True
    print("")
    if flag == True:
        new  = []
        new2 = []
        for p in diz[l[i]]:
            if p.startswith(prefix):
                newP2 = p[1::] + prefix + "*"
                new2.append(newP2)
            else:
                newP = p + prefix + "*"
                new.append(newP)
        new2.append("ε")
        diz[prefix] = new
        print(prefix + " → " + "|".join(new))
        print(prefix + "* → " + "|".join(new2))



def sostituisco(i,j):
    prefix2 = l[i][0]
    prefix1 = l[j][0]
    flag = False
    for p in diz[l[i]]:
        if p.startswith(prefix1):
            print("Ai → Aj :  " + prefix2 + " → "+ p)
            flag = True
    if flag == True:
            new  = []
            print(prefix2 + " → ", end="")
            for p in diz[prefix2]:
                if p.startswith(prefix1):
                    for p1 in diz[prefix1]:
                        newP = p1 + p[1::]
                        print(newP, end="|")
                        new.append(newP)
                else:
                    print(p, end="|")
                    new.append(p)
            diz[prefix2] = new
            print("")
                
                    

               



for i in range(0,len(l)):
    print("i =",(i+1) ,end=" ")
    for j in range(0,i):
        print("j = ",(j+1))
        sostituisco(i,j)
        
    eliminaRicorsioneImmediata(i)
    print("--------------------------------------------------------------")
