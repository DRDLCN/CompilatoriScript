stato = ""
statoIniziale = -1
diz = {}
inp = set()
with open("nfa2dfa/input.txt","r") as input:
    for x in input.readlines():
        if ":" in x.strip():
            stato = int(x.strip().split(":")[0])
            if statoIniziale == -1:
                statoIniziale = stato
            diz[stato] = {}
        else:
            input = x.strip().split(" ")[0]
            if input != "è":
                inp.add(input)
            statoFuturo = int(x.strip().split(" ")[1])
            if input not in diz[stato]:
                diz[stato][input] = [statoFuturo]
            else:
                diz[stato][input].append(statoFuturo)

            


def eclosure(stato,visitati):
    visitati.append(stato)
    if "è" not in diz[stato]:
        return visitati
    for stati in diz[stato]["è"]:
        if stati not in visitati:
            eclosure(stati,visitati)
    return visitati

def move(setStati,input):
    o = []
    for stato in setStati:
        if input in diz[stato]:
            o += (diz[stato][input])
    return set(o)

output = {}

def multipleEClosure(setStati):
    l = []
    for x in setStati:
        for y in set(eclosure(x,[])):
            l.append(y)
    return set(l)


primoCondensato = set(eclosure(statoIniziale,[]))
print("E-C("+str(statoIniziale)+")=" + str(primoCondensato))
iterate = [primoCondensato] 
output[tuple(primoCondensato)] = {}

while(len(iterate)>0):
    for x in iterate:
        if x != set():
            for input in inp:
                mv = move(x,input)
                k = multipleEClosure(mv)
                print("E-C(move("+str(x)+","+input+") = E-C(" + str(mv)+") = " + str(k))
                output[tuple(x)][input] = k
                if tuple(k) not in output and k != set():
                    output[tuple(k)] = {}
                    iterate.append(k)
            iterate.remove(x)
            print("----------------------------------------------------------------")
print("RICORDATI STATI INIZIALI E OUTPUT")

for x in output:
    for y in output[x]:
        print(x,y,output[x][y])