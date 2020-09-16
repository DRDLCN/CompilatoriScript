nodi=[1,2,6,5,3,10,8,7,9,12,11,4] #inserisci reverse della visita post-order del tuo albero nato dalla dfs
#post order f xs f dx padre , 
listaraggiunti={1:[1],2:[1,7,4,5],3:[2],4:[11,9],5:[6],6:[2],7:[12,8,5],8:[4,10],9:[7],10:[3],11:[10],12:[8]}
 #i valori sono i nodi che raggiungono la chiave nel grafo di partenza


def dom(nodi,listaraggiunti):
    dom={}
    controllo={}
    conto=0
    for i,x in enumerate(nodi):
        if i==0:
            dom[x]={x}
        else:
            dom[x]=set(nodi)
    while(True):
        conto+=1
        print("\n\n"+str(conto)+"° ITERAZIONE\n")
        for nodo in nodi:
            raggiunti=listaraggiunti[nodo]
            primoraggiunto=raggiunti[0]
            domtot=set(dom[primoraggiunto])
            print("DOM("+str(nodo)+")=",end="")
            for raggiunto in raggiunti:
                domtot=domtot&set(dom[raggiunto])
                if raggiunti.index(raggiunto)==len(raggiunti)-1:
                     print("DOM("+str(raggiunto)+")",end="")
                else:
                    print("DOM("+str(raggiunto)+") & ",end="")
            domtot=domtot|{nodo}
            print(" U {"+str(nodo)+"}",end="")
            domtot=list(domtot)
            dom[nodo]=domtot
            dom[nodo].sort()
            print(" = "+str(set(dom[nodo])))
        if dom==controllo:
            break
        controllo=dom
    print("\n\nTROVO I BACK\n")
    for x in nodi[1:]:
        for doma in listaraggiunti[x]:
            if doma!=x:
                if x in dom[doma]:
                    print("{"+str(doma)+","+str(x)+"}  "+str(x)+" esiste in DOM("+str(doma)+")")
    print("\nELIMINO QUESTI ARCHI(BACK) DAL GRAFO ORIGINALE E RIESEGUO LA DFS")
    print("\nESEGUITA LA DFS, SE CI SONO ARCHI ALL'INDIETRO NON è RIDUCIBILE, SE NON CI SONO ARCHI ALL'INDIETRO è RIDUCIBILE")
dom(nodi,listaraggiunti)

    
        