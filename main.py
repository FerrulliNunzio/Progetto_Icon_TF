import random as random
from pyswip import *
from Intervation import Intervation
from Classifier import classify
from Map.Graph import Graph
from Map.Node import Node

def createKB():
    kb = Prolog()
    for i in range(3):
        kb.assertz("caserma(caserma_" + str(i+1) + ")")

    kb.assertz("agenti(caserma_1, 5)")
    kb.assertz("agenti(caserma_2, 10)")
    kb.assertz("agenti(caserma_3, 20)")

    kb.assertz("veicoli(caserma_1, 3)")
    kb.assertz("veicoli(caserma_2, 7)")
    kb.assertz("veicoli(caserma_3, 10)")

    kb.assertz("veicoli_speciali(caserma_1, 0)")
    kb.assertz("veicoli_speciali(caserma_2, 2)")
    kb.assertz("veicoli_speciali(caserma_3, 5)")

    return kb

def createMap():
    map= Graph()

    #Dichiaro tutti i nodi
    A = Node("1", "A", 2, 0)
    B = Node("2", "B", 2, 7)
    C = Node("3", "C", 3, 2)
    D = Node("4", "D", 3, 4)
    E = Node("5", "E", 5, 1)
    F = Node("6", "F", 3, 3)
    G = Node("7", "G", 2, 2)
    H = Node("8", "H", 2, 2)
    I = Node("9", "I", 2, 1)
    J = Node("10", "J", 4, 3)
    L = Node("11", "L", 3, 3)
    M = Node("12", "M", 4, 4)
    N = Node("13", "N", 4, 3)
    O = Node("14", "O", 6, 5)
    P = Node("15", "P", 2, 2)
    Q = Node("16", "Q", 4, 6)
    R = Node("17", "R", 1, 4)
    S = Node("18", "S", 2, 1)
    T = Node("19", "T", 1, 1)
    U = Node("20", "U", 2, 1)

    # Caserme
    Cas1 = Node("Caserma 1", "Caserma 1", 2, 4)
    Cas2 = Node("Caserma 2", "Caserma 2", 2, 1)
    Cas3 = Node("Caserma 3", "Caserma 3", 2, 2)

    # Aggiungo i nodi alla
    map.add_node(A)
    map.add_node(B)
    map.add_node(C)
    map.add_node(D)
    map.add_node(E)
    map.add_node(F)
    map.add_node(G)
    map.add_node(H)
    map.add_node(I)
    map.add_node(J)
    map.add_node(L)
    map.add_node(M)
    map.add_node(N)
    map.add_node(O)
    map.add_node(P)
    map.add_node(Q)
    map.add_node(R)
    map.add_node(S)
    map.add_node(T)
    map.add_node(U)
    map.add_node(Cas1)
    map.add_node(Cas2)
    map.add_node(Cas3)

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
def createIncident(placeIncident: Node):
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
    print("L'incidente è avvenuto in " + placeIncident.name)
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

def random_place(map: Graph):
    return map.nodes()[random.randint(0, 19)]

def determine_number_barracks(nameBarracks):
    numBarack = 0
    if nameBarracks == "caserma_1":
        numBarack = -3
    elif nameBarracks == "caserma_2":
        numBarack = -2
    elif nameBarracks == "caserma_3":
        numBarack = -1

    return numBarack

def determine_barrack(nameBarrack, intervation: Intervation):
    map.a_star(map.nodes()[determine_number_barracks(nameBarrack)], intervation.placeIntervention)

    if intervation.placeIntervention.realDistanceValue > intervation.getTimeLimit():
        print("La " + nameBarrack + " ha le truppe necessarie per eseguire l'intervento ma è troppo lontana dal punto")
    else:
        print("La " + nameBarrack + " soddisfa tutti i requiditi per eseguire l'intervento con tempo "
              + str(intervation.placeIntervention.realDistanceValue))

if __name__ == '__main__':
    #Generazione della mappa
    map = createMap()
    #Generazione della KB
    kb = createKB()
    #Generazione dell'evento
    placeIncident = random_place(map)
    event = createIncident(placeIncident)
    #Addestramento del classificatote e classificazione incidente
    try:
        prediction = classify(event, "DataSet.csv")
    except FileNotFoundError:
        prediction = classify(event, "C:/Users/Utente/Desktop/Progetto_Icon_TF/DataSet.csv")   #da cancellare o modificare
    #Creazione dell'intervento in base alla classificazione dell'incidente
    intervation = Intervation(prediction, placeIncident)
    print("-----------Interrogazione Base di conoscenza-----------")
    strQuery = "caserma(X), agenti(X,A), veicoli(X,B), veicoli_speciali(X,C), A>=" + str(
        intervation.getNumAgent()) + ", B>=" + str(intervation.getNumVeihcles()) + ", C>=" + str(
        intervation.getNumSpecialeVeihcles())
    result = list(kb.query(strQuery))
    print("-----------Visaulizzazione Risultati-----------")
    if len(result) > 0:
        print("Le caserme consigliate per intervenire sono: \n")

        for item in result:
            determine_barrack(item["X"], intervation)
    else:
        print("Le caserme disponibili non hanno le risorse necessarie per riuscire a risolvere l'incidente da soli")
    print("-----------------------------------------------")
