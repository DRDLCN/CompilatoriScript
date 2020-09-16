import random
class Albero:
    def __init__(self, valore, figliosx=None, figliodx=None, op=None):
        self.v = valore
        self.sx = figliosx
        self.dx = figliodx
        self.op = op
        self.en = 0

    def Stampa(self):
        if self.sx:
            self.sx.Stampa()
        print(self.v)
        if self.dx:
            self.dx.Stampa()

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.dx is None and self.sx is None:
            line = '%s E=%s' % (self.v, self.en)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        # Two children.
        left, n, p, x = self.sx._display_aux()
        right, m, q, y = self.dx._display_aux()
        s = '%s E=%s' % (self.v, self.en)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

def Num(v):
    if not (v.sx or v.dx):  # se è foglia
        v.en = 1
        #print(v.v + " EN = " + str(v.en))
        return
    else:
        Num(v.sx)
        Num(v.dx)
        if(v.sx.en == v.dx.en): # se EN uguale
            v.en = v.sx.en + 1
        else:
            v.en = max(v.sx.en, v.dx.en)
        #print(v.v + " EN = " + str(v.en))
        return
    
def Ershov(v, b, l):
    if not (v.sx or v.dx):  # se è foglia
        print("\t"*l + "Ershov(" + v.v + ", " + str(b) + ") genera: LD R" + str(b) + ", " + str(v.v))
        return
    elif(v.sx.en == v.dx.en):   # figli con EN uguale
        print("\t"*l + "Ershov(" + v.v + ", " + str(b) + "):")
        print("\t"*l + "CASO 1")
        Ershov(v.dx, b+1, l+1)
        Ershov(v.sx, b, l+1)
        if(v.op == "+"):
            print("\t"*l + "Ershov(" + v.v + ", " + str(b) + ") genera: ADD R" + str(b+v.en-1) + ", R" + str(b+v.en-2) + ", R" + str(b+v.en-1))
        elif(v.op == "*"):
            print("\t"*l + "Ershov(" + v.v + ", " + str(b) + ") genera: MUL R" + str(b+v.en-1) + ", R" + str(b+v.en-2) + ", R" + str(b+v.en-1))
        elif(v.op == "-"):
            print("\t"*l + "Ershov(" + v.v + ", " + str(b) + ") genera: SUB R" + str(b+v.en-1) + ", R" + str(b+v.en-2) + ", R" + str(b+v.en-1))
        elif(v.op == "/"):
            print("\t"*l + "Ershov(" + v.v + ", " + str(b) + ") genera: DIV R" + str(b+v.en-1) + ", R" + str(b+v.en-2) + ", R" + str(b+v.en-1))
        return
    else:
        print("\t"*l + "Ershov(" + v.v + ", " + str(b) + "):")
        print("\t"*l + "CASO 2")
        if(v.sx.en < v.dx.en):  # max dx
            Ershov(v.dx, b, l+1)
            Ershov(v.sx, b, l+1)
            if(v.op == "+"):
                print("\t"*l + "Ershov(" + v.v + ", " + str(b) + ") genera: ADD R" + str(b+v.en-1) + ", R" + str(b+v.sx.en-1) + ", R" + str(b+v.en-1))
            elif(v.op == "*"):
                print("\t"*l + "Ershov(" + v.v + ", " + str(b) + ") genera: MUL R" + str(b+v.en-1) + ", R" + str(b+v.sx.en-1) + ", R" + str(b+v.en-1))
            elif(v.op == "-"):
                print("\t"*l + "Ershov(" + v.v + ", " + str(b) + ") genera: SUB R" + str(b+v.en-1) + ", R" + str(b+v.sx.en-1) + ", R" + str(b+v.en-1))
            elif(v.op == "/"):
                print("\t"*l + "Ershov(" + v.v + ", " + str(b) + ") genera: DIV R" + str(b+v.en-1) + ", R" + str(b+v.sx.en-1) + ", R" + str(b+v.en-1))
            return
        else:
            Ershov(v.sx, b, l+1)
            Ershov(v.dx, b, l+1)
            if(v.op == "+"):
                print("\t"*l + "Ershov(" + v.v + ", " + str(b) + ") genera: ADD R" + str(b+v.en-1) + ", R" + str(b+v.en-1) + ", R" + str(b+v.dx.en-1))
            elif(v.op == "*"):
                print("\t"*l + "Ershov(" + v.v + ", " + str(b) + ") genera: MUL R" + str(b+v.en-1) + ", R" + str(b+v.en-1) + ", R" + str(b+v.dx.en-1))
            elif(v.op == "-"):
                print("\t"*l + "Ershov(" + v.v + ", " + str(b) + ") genera: SUB R" + str(b+v.en-1) + ", R" + str(b+v.en-1) + ", R" + str(b+v.dx.en-1))
            elif(v.op == "/"):
                print("\t"*l + "Ershov(" + v.v + ", " + str(b) + ") genera: DIV R" + str(b+v.en-1) + ", R" + str(b+v.en-1) + ", R" + str(b+v.dx.en-1))
            return

def ErshovGen(v, r, b, l):
    if not (v.sx or v.dx):  # se è foglia
        print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: LD R" + str(b) + ", " + str(v.v))
        return
    elif(v.en > r): # CASO 0
        print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + "):")
        print("\t"*l + "CASO 0")
        if(v.dx.en < v.sx.en):  # EN sx > EN dx
            ErshovGen(v.sx, r, 1, l+1)
            print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: ST T" + str(v.en) + ", R" + str(r))
            if(v.dx.en < r):
                ErshovGen(v.dx, r, r-v.dx.en+1, l+1)
            else:
                ErshovGen(v.dx, r, 1, l+1)
            print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: LD R" + str(r-1) + ", T" + str(v.en))
            if(v.op == "+"):
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: ADD R" + str(r) + ", R" + str(r-1) + ", R" + str(r))
            elif(v.op == "*"):
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: MUL R" + str(r) + ", R" + str(r-1) + ", R" + str(r))
            elif(v.op == "-"):
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: SUB R" + str(r) + ", R" + str(r-1) + ", R" + str(r))
            elif(v.op == "/"):
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: DIV R" + str(r) + ", R" + str(r-1) + ", R" + str(r))
            return
        elif(v.sx.en < v.dx.en): # EN dx > EN sx
            ErshovGen(v.dx, r, 1, l+1)
            print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: ST T" + str(v.en) + ", R" + str(r))
            if(v.sx.en < r):
                ErshovGen(v.sx, r, r-v.sx.en+1, l+1)
            else:
                ErshovGen(v.sx, r, 1, l+1)
            print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: LD R" + str(r-1) + ", T" + str(v.en))
            if(v.op == "+"):
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: ADD R" + str(r) + ", R" + str(r) + ", R" + str(r-1))
            elif(v.op == "*"):
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: MUL R" + str(r) + ", R" + str(r) + ", R" + str(r-1))
            elif(v.op == "-"):
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: SUB R" + str(r) + ", R" + str(r) + ", R" + str(r-1))
            elif(v.op == "/"):
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: DIV R" + str(r) + ", R" + str(r) + ", R" + str(r-1))
            return
        else:   # EN sx == EN dx
            if(random.random() % 2):
                ErshovGen(v.dx, r, 1, l+1)
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: ST T" + str(v.en) + ", R" + str(r))
                if(v.sx.en < r):
                    ErshovGen(v.sx, r, r-v.sx.en+1, l+1)
                else:
                    ErshovGen(v.sx, r, 1, l+1)
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: LD R" + str(r-1) + ", T" + str(v.en))
                if(v.op == "+"):
                    print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: ADD R" + str(r) + ", R" + str(r) + ", R" + str(r-1))
                elif(v.op == "*"):
                    print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: MUL R" + str(r) + ", R" + str(r) + ", R" + str(r-1))
                elif(v.op == "-"):
                    print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: SUB R" + str(r) + ", R" + str(r) + ", R" + str(r-1))
                elif(v.op == "/"):
                    print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: DIV R" + str(r) + ", R" + str(r) + ", R" + str(r-1))
                return
            else:
                ErshovGen(v.sx, r, 1, l+1)
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: ST T" + str(v.en) + ", R" + str(r))
                if(v.dx.en < r):
                    ErshovGen(v.dx, r, r-v.dx.en+1, l+1)
                else:
                    ErshovGen(v.dx, r, 1, l+1)
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: LD R" + str(r-1) + ", T" + str(v.en))
                if(v.op == "+"):
                    print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: ADD R" + str(r) + ", R" + str(r-1) + ", R" + str(r))
                elif(v.op == "*"):
                    print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: MUL R" + str(r) + ", R" + str(r-1) + ", R" + str(r))
                elif(v.op == "-"):
                    print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: SUB R" + str(r) + ", R" + str(r-1) + ", R" + str(r))
                elif(v.op == "/"):
                    print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: DIV R" + str(r) + ", R" + str(r-1) + ", R" + str(r))
                return
    elif(v.sx.en == v.dx.en):   # figli con EN uguale
        print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + "):")
        print("\t"*l + "CASO 1")
        ErshovGen(v.dx, r, b+1, l+1)
        ErshovGen(v.sx, r, b, l+1)
        if(v.op == "+"):
            print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: ADD R" + str(b+v.en-1) + ", R" + str(b+v.en-2) + ", R" + str(b+v.en-1))
        elif(v.op == "*"):
            print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: MUL R" + str(b+v.en-1) + ", R" + str(b+v.en-2) + ", R" + str(b+v.en-1))
        elif(v.op == "-"):
            print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: SUB R" + str(b+v.en-1) + ", R" + str(b+v.en-2) + ", R" + str(b+v.en-1))
        elif(v.op == "/"):
            print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: DIV R" + str(b+v.en-1) + ", R" + str(b+v.en-2) + ", R" + str(b+v.en-1))
        return
    else:
        print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + "):")
        print("\t"*l + "CASO 2")
        if(v.sx.en < v.dx.en):  # max dx
            ErshovGen(v.dx, r, b, l+1)
            ErshovGen(v.sx, r, b, l+1)
            if(v.op == "+"):
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: ADD R" + str(b+v.en-1) + ", R" + str(b+v.sx.en-1) + ", R" + str(b+v.en-1))
            elif(v.op == "*"):
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: MUL R" + str(b+v.en-1) + ", R" + str(b+v.sx.en-1) + ", R" + str(b+v.en-1))
            elif(v.op == "-"):
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: SUB R" + str(b+v.en-1) + ", R" + str(b+v.sx.en-1) + ", R" + str(b+v.en-1))
            elif(v.op == "/"):
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: DIV R" + str(b+v.en-1) + ", R" + str(b+v.sx.en-1) + ", R" + str(b+v.en-1))
            return
        else:
            ErshovGen(v.sx, r, b, l+1)
            ErshovGen(v.dx, r, b, l+1)
            if(v.op == "+"):
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: ADD R" + str(b+v.en-1) + ", R" + str(b+v.en-1) + ", R" + str(b+v.dx.en-1))
            elif(v.op == "*"):
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: MUL R" + str(b+v.en-1) + ", R" + str(b+v.en-1) + ", R" + str(b+v.dx.en-1))
            elif(v.op == "-"):
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: SUB R" + str(b+v.en-1) + ", R" + str(b+v.en-1) + ", R" + str(b+v.dx.en-1))
            elif(v.op == "/"):
                print("\t"*l + "ErshovGen(" + v.v + ", " + str(r) + ", " + str(b) + ") genera: DIV R" + str(b+v.en-1) + ", R" + str(b+v.en-1) + ", R" + str(b+v.dx.en-1))
            return

alb = {}
with open("ershov/input.txt", "r") as f:
    for line in f:
        line = line.strip()
        l = line.split("=")
        alb.setdefault(l[0], Albero(l[0]))
        l2 = l[1].split("+")    # addizione
        if(len(l2)>1):
            alb.setdefault(l2[0], Albero(l2[0]))
            alb.setdefault(l2[1], Albero(l2[1]))
            alb[l[0]].sx = alb[l2[0]]
            alb[l[0]].dx = alb[l2[1]]
            alb[l[0]].op = "+"
            
        l2 = l[1].split("*")    # moltiplicazione
        if(len(l2)>1):
            alb.setdefault(l2[0], Albero(l2[0]))
            alb.setdefault(l2[1], Albero(l2[1]))
            alb[l[0]].sx = alb[l2[0]]
            alb[l[0]].dx = alb[l2[1]]
            alb[l[0]].op = "*"
            
        l2 = l[1].split("-")    # sottrazione
        if(len(l2)>1):
            alb.setdefault(l2[0], Albero(l2[0]))
            alb.setdefault(l2[1], Albero(l2[1]))
            alb[l[0]].sx = alb[l2[0]]
            alb[l[0]].dx = alb[l2[1]]
            alb[l[0]].op = "-"
            
        l2 = l[1].split("/")    # divisione
        if(len(l2)>1):
            alb.setdefault(l2[0], Albero(l2[0]))
            alb.setdefault(l2[1], Albero(l2[1]))
            alb[l[0]].sx = alb[l2[0]]
            alb[l[0]].dx = alb[l2[1]]
            alb[l[0]].op = "/"




Num(alb[l[0]])
alb[l[0]].display()
print("\n")
print("********** ERSHOV **********")
Ershov(alb[l[0]], 1, 0)
print("\n")
print("********** ERSHOVGEN **********")
ErshovGen(alb[l[0]], 2, 1, 0)