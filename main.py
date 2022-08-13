import random as random
from pyswip import Prolog
import Intervation
from Classifier import classify
from Map.Graph import Graph
from Map.Node import Node

def createKB():
    kb = Prolog()
    for i in range(3):
        kb.assertz("caserma(caserma_" + str(i+1) + ")")

    kb.assertz("agenti(caserma_1, 7)")
    kb.assertz("agenti(caserma_2, 15)")
    kb.assertz("agenti(caserma_3, 22)")

    kb.assertz("veicoli(caserma_1, 2)")
    kb.assertz("veicoli(caserma_2, 5)")
    kb.assertz("veicoli(caserma_3, 8)")

    kb.assertz("veicoli_speciali(caserma_1, 0)")
    kb.assertz("veicoli_speciali(caserma_2, 3)")
    kb.assertz("veicoli_speciali(caserma_3, 5)")

    return kb

def createMap():
    map= Graph()

    #Dichiaro tutti i nodi
    A = Node("1", 2, 0)
    B = Node("2", 2, 7)
    C = Node("3", 3, 2)
    D = Node("4", 3, 4)
    E = Node("5", 5, 1)
    F = Node("6", 3, 3)
    G = Node("7", 2, 2)
    H = Node("8", 2, 2)
    I = Node("9", 2, 1)
    J = Node("10", 4, 3)
    L = Node("11", 3, 3)
    M = Node("12", 4, 4)
    N = Node("13", 4, 3)
    O = Node("14", 6, 5)
    P = Node("15", 2, 2)
    Q = Node("16", 4, 6)
    R = Node("17", 1, 4)
    S = Node("18", 2, 1)
    T = Node("19", 1, 1)
    U = Node("20", 2, 1)

    # Caserme
    Cas1 = Node("Caserma 1", 2, 4)
    Cas2 = Node("Caserma 2", 2, 1)
    Cas3 = Node("Caserma 3", 2, 2)

    # Aggiungo i nodi alla
    map.addnode(A)
    map.addnode(B)
    map.addnode(C)
    map.addnode(D)
    map.addnode(E)
    map.addnode(F)
    map.addnode(G)
    map.addnode(H)
    map.addnode(I)
    map.addnode(J)
    map.addnode(L)
    map.addnode(M)
    map.addnode(N)
    map.addnode(O)
    map.addnode(P)
    map.addnode(Q)
    map.addnode(R)
    map.addnode(S)
    map.addnode(T)
    map.addnode(U)
    map.addnode(Cas1)
    map.addnode(Cas2)
    map.addnode(Cas3)

    #aggiungo gli archi
    map.connect(A, B, 9)
    map.connect(A, C, 4)
    map.connect(A, D, 8)
    map.connect(B, O, 13)
    map.connect(B, S, 9)
    map.connect(B, C, 4)
    map.connect(C, E, 4)
    map.connect(C, F, 6)
    map.connect(D, T, 5)
    map.connect(D, N, 6)
    map.connect(E, J, 8)
    map.connect(E, F, 8)
    map.connect(F, H, 5)
    map.connect(F, T, 4)
    map.connect(G, T, 3)
    map.connect(G, N, 6)
    map.connect(G, L, 5)
    map.connect(H, L, 5)
    map.connect(H, Cas3, 4)
    map.connect(I, S, 3)
    map.connect(I, O, 7)
    map.connect(I, J, 5)
    map.connect(J, P, 5)
    map.connect(J, M, 7)
    map.connect(L, M, 7)
    map.connect(M, U, 6)
    map.connect(N, Cas2, 5)
    map.connect(O, Q, 9)
    map.connect(P, Q, 6)
    map.connect(P, R, 7)
    map.connect(P, U, 4)
    map.connect(Q, Cas1, 8)
    map.connect(R, U, 6)

    return map

#attraverso la generazione di numeri casuali questa funzione crea un incidente
def createIncident():
    xInput = [[]]
    incident = []
    incident.append(random.randint(0, 4))#indica il numero dei feriti
    if incident.__getitem__(0) >= 1: #se ci sono dei feriti, ci sarà soccorso
        incident.append(1)
    else:
        incident.append(random.randint(0, 1))
    incident.append(random.randint(0, 1))#inidica se c'è un incendio oppure no
    incident.append(random.randint(0, 1))#indica se c'è stata un esplosione oppure no
    incident.append(random.randint(0, 1))#indica se c'è stato un incidente stradale opppure no
    incident.append(random.randint(0, 1))#indica se c'è stata una calamità naturale oppure no
    #inserire la funzione che sceglie un nodo casuale nel grafo

    print("---------------SEGNALATO INCIDENTE---------------")
    print("")
    print("DESCRIZIONE DELL'INCIDENTE:")
    print(createStringToWounded(incident.__getitem__(0)))
    print(createStringToRescue(incident.__getitem__(1)))
    print(createStringToFire(incident.__getitem__(2)))
    print(createStringToExplosion(incident.__getitem__(3)))
    print(createStringToCarAccident(incident.__getitem__(4)))
    print(createStringToNaturalDisaster(incident.__getitem__(5)))
    #inserire la stampa che indica il posto in cui è stato generato l'incidente
    print("-------------------------------------------------")

    xInput = [incident]
    return xInput

#descrive il numero dei feriti in base all'intero uscito
def createStringToWounded(value : int):
    if value == 0:
        return "-Ci sono 0 persone ferite o in pericolo"
    elif value == 1:
        return "-Ci sono da 1 a 3 persone ferite o in pericolo"
    elif value == 2:
        return "-Ci sono da 4 a 7 persone ferite o in pericolo"
    elif value == 3:
        return "-Ci sono da 8 a 12 persone ferite o in pericolo"
    elif value == 4:
        return "-Ci sono 13 o più  persone ferite o in pericolo"

#descrive se è richiesto effetture un soccorso o non è necessario
def createStringToRescue(value : int):
    if value == 0:
        return "-Non bisognerà effettuare dei soccorsi"
    elif value == 1:
        return "-Bisognerà effettuare dei soccorsi"

#descrive se c'è un incendio
def createStringToFire(value : int):
    if value == 0:
        return "-Non è stato rilevato nessun incendio nell'incidente"
    elif value == 1:
        return "-E' stato rilevato un incendio nell'incidente"

#descrive se ci sono state delle esplosioni
def createStringToExplosion(value : int):
    if value == 0:
        return "-Non ci sono state delle esplosioni nell'incidente"
    elif value == 1:
        return "-Ci sono state delle esplosioni nell'incidente"

#descrive se c'è stato un incidente stradale
def createStringToCarAccident(value : int):
    if value == 0:
        return "-Non è avvenuto nessun incidente stradale"
    elif value == 1:
        return "-C'è stato un incidente stradale"

#descrive se c'è stato una calamità naturale
def createStringToNaturalDisaster(value : int):
    if value == 0:
        return "-L'incidente non è stato causato da una calamità naturale"
    elif value == 1:
        return "-L'incidente è stato causato da una calamità naturale"


if __name__ == '__main__':
    #Generazione della mappa

    #Generazione della KB
    kb = createKB()
    #Generazione dell'evento
    event = createIncident()
    #Addestramento del classificatote e classificazione incidente
    try:
        prediction = classify(event,"DataSet.csv")
    except FileNotFoundError:
        prediction = classify(event,"Source/DataSet.csv")   #da cancellare o modificare
    #Creazione dell'intervento in base alla classificazione dell'incidente
    intervation = Intervation(prediction)
    print("-----------Interrogazione Base di conoscenza-----------")
    strQuery = "caserma(X), agenti(X,A), veicoli(X,B), veicoli_speciali(X,C), A>=" + str(
        intervation.getNumAgent()) + ", B>=" + str(intervation.getNumVeihcles()) + ", C>=" + str(
        intervation.getNumSpecialeVeihcles())
    result = list(kb.query(strQuery))
    print("-----------Visaulizzazione Risultati-----------")
    if len(result) > 0:
        print("Le caserme consigliate per intervenire sono: \n")
        for item in result:
            print("-" + item["X"] + "\n")
    else:
        print("Le caserme disponibili non hanno le risorse necessarie per riuscire a risolvere l'incidente da soli")
    print("-----------------------------------------------")
