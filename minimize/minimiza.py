l = []
inp = set()
diz = {}
with open("minimize/input.txt","r") as input:
    statiFinali = set()
    altri = set()
    for x in input.readlines():
        if ":" in x.strip():
            try:
                stato = int(x.strip().split(":")[0])
                altri.add(stato)
                diz[stato] = {}
            except:
                stato = int(x.strip().split(":")[0][0])
                diz[int(x.strip().split(":")[0][0])] = {}
                statiFinali.add(int(x.strip().split(":")[0][0]))
        else:
            input = x.strip().split(" ")[0]
            if input != "è":
                inp.add(input)
            statoFuturo = int(x.strip().split(" ")[1])
            if input not in diz[stato]:
                diz[stato][input] = [statoFuturo]
            else:
                diz[stato][input].append(statoFuturo)
    l.append(statiFinali)
    l.append(altri)

def checkDiscrepanza(diz,input):
    o = {}
    for x in diz:
        for y in diz[x]:
            for z in range(0,len(l)):
                if y in l[z]:
                    if z not in o:
                        index = z
                        o[index] = [x]
                    else:
                        index = z
                        o[index].append(x)
            
    if len(o) > 1:
        for x in o:
            print("Per "+input+"  "+str(o[x])+" vanno in " +str(l[x]))
            l.append(set(o[x]))
        return True
    else:
        for x in o:
            print("Per "+input+" tutti gli stati vanno in " +str(l[x]))
        return False



while(True):
    stop = list(l)
    flag = False
    for ins in l:
        if len(ins) > 1:
            print("analizzo " + str(ins))
            for input in inp:
                d = {}
                for stato in ins:
                    ##### aggiungere inpunt not in diz
                    if input in diz[stato]:
                        d[stato] = diz[stato][input]
                if checkDiscrepanza(d,input):
                    flag = True
                    l.remove(ins)
                    print("π_new =" + str(l))
                    break

        if flag:
            break
    if l == stop:
        break

#finire l'output per disegnare velocemente
print(l)