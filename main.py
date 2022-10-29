import random as random
from collections import defaultdict

from pyswip import Prolog
from Intervation import Intervation
from Classifier import classify


def createKB():
    kb = Prolog()
    kb.consult("kb.pl")
    return kb

def createMap():
    weighted_edges =[['A', 'B', 9], ['A', 'D', 8], ['A', 'C', 4], ['B', 'A', 9], ['D', 'A', 8], ['C', 'A', 4],
                     ['B', 'O', 13], ['B', 'C', 4],['O', 'B', 13], ['C', 'B', 4],
                     ['C', 'E', 4], ['C', 'F', 6],['E', 'C', 4], ['F', 'C', 6],
                     ['D', 'T', 5], ['D', 'N', 6],['T', 'D', 5], ['N', 'D', 6],
                     ['E', 'F', 8], ['E', 'J', 8],['F', 'E', 8], ['J', 'E', 8],
                     ['F', 'H', 5], ['F', 'T', 4], ['H', 'F', 5], ['T', 'F', 4],
                     ['G', 'L', 5], ['G', 'T', 3], ['G', 'N', 6], ['L', 'G', 5], ['T', 'G', 3], ['N', 'G', 6],
                     ['H', 'Cas3', 4], ['H', 'L', 5], ['Cas3', 'H', 4], ['L', 'H', 5],
                     ['I', 'S', 3], ['I', 'J', 5], ['I', 'O', 7], ['S', 'I', 3], ['J', 'I', 5], ['O', 'I', 7],
                     ['J', 'M', 7], ['J', 'P', 5], ['M', 'J', 7], ['P', 'J', 5],
                     ['L', 'M', 7], ['M', 'L', 7],
                     ['M', 'U', 6], ['U', 'M', 6],
                     ['N', 'Cas2', 5], ['Cas2', 'N', 5],
                     ['O', 'Q', 9], ['Q', 'O', 9],
                     ['P', 'Q', 6], ['P', 'R', 7], ['P', 'U', 4], ['Q', 'P', 6], ['R', 'P', 7], ['U', 'P', 4],
                     ['Q', 'Cas1', 8], ['Cas1', 'Q', 8],
                     ['R', 'U', 6], ['U', 'R', 6],
                     ['S', 'B', 9], ['B', 'S', 9]]
    return weighted_edges

def randomIncident():
    incident = []
    incident.append(random.randint(0, 3))  # indica il numero dei feriti
    incident.append(random.randint(0, 2))  # inidica se c'è un incendio
    incident.append(random.randint(0, 2))  # indica se c'è stata un esplosione
    incident.append(random.randint(0, 2))  # indica se c'è stato un incidente
    incident.append(random.randint(0, 3))  # indica se c'è stata una calamità
    return incident

#attraverso la generazione di numeri casuali questa funzione crea un incidente
def createIncident(placeIncident):
    xInput = [[]]
    incident = []
    incident = randomIncident()
    while checkIncident(incident):
        incident = randomIncident()

    print("---------------SEGNALATO INCIDENTE---------------")
    print("")
    print("DESCRIZIONE DELL'INCIDENTE:")
    print(createStringToWounded(incident.__getitem__(0)))
    print(createStringToFire(incident.__getitem__(1)))
    print(createStringToExplosion(incident.__getitem__(2)))
    print(createStringToCarAccident(incident.__getitem__(3)))
    print(createStringToNaturalDisaster(incident.__getitem__(4)))
    print("L'incidente è avvenuto in " + placeIncident)
    print("-------------------------------------------------")

    xInput = [incident]
    return xInput

def checkIncident(incident):
    flag = True
    for elem in incident:
        if elem != 0:
            flag = False
            return flag
    return flag

#descrive il numero dei feriti in base all'intero uscito
def createStringToWounded(value : int):
    if value == 0:
        return "-Ci sono 0 persone ferite o in pericolo"
    elif value == 1:
        return "-Ci sono da 1 a 3 persone ferite o in pericolo"
    elif value == 2:
        return "-Ci sono da 4 a 8 persone ferite o in pericolo"
    elif value == 3:
        return "-Ci sono da 9 o più persone ferite o in pericolo"


#descrive se c'è un incendio
def createStringToFire(value : int):
    if value == 0:
        return "-Non è stato rilevato nessun incendio nell'incidente"
    elif value == 1:
        return "-E' stato rilevato un incendio  di rischio basso nell'incidente"
    elif value == 2:
        return "-E' stato rilevato un incendio  di rischio medio o alto nell'incidente"

#descrive se ci sono state delle esplosioni
def createStringToExplosion(value : int):
    if value == 0:
        return "-Non ci sono state delle esplosioni nell'incidente"
    elif value == 1:
        return "-Ci sono state delle esplosioni di grado 1 nell'incidente"
    elif value == 2:
        return "-Ci sono state delle esplosioni di grado 2 nell'incidente"

#descrive se c'è stato un incidente stradale
def createStringToCarAccident(value : int):
    if value == 0:
        return "-Non è avvenuto nessun incidente stradale"
    elif value == 1:
        return "-C'è stato un incidente stradale di una sola macchina"
    elif value == 2:
        return "-C'è stato un incidente stradale di più macchine"


#descrive se c'è stato una calamità naturale
def createStringToNaturalDisaster(value : int):
    if value == 0:
        return "-L'incidente non è stato causato da una calamità naturale"
    elif value == 1:
        return "-L'incidente è stato causato da una calamità naturale lieve"
    elif value == 2:
        return "-L'incidente è stato causato da una calamità naturale media"
    elif value == 3:
        return "-L'incidente è stato causato da una calamità naturale alta"

def random_place(map):
    queue = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']

    i = random.randint(0,19)
    return queue[i]

def determine_number_barracks(nameBarracks):
    numBarack = 0
    if nameBarracks == "caserma_1":
        numBarack = 'Cas1'
    elif nameBarracks == "caserma_2":
        numBarack = 'Cas2'
    elif nameBarracks == "caserma_3":
        numBarack = 'Cas3'

    return numBarack

def determine_barrack(directed_weighted_graph, nameBarrack, intervation: Intervation):
    distance = UCS(directed_weighted_graph, nameBarrack, intervation.placeIntervention)
    if distance > intervation.getTimeLimit():
        print("La " + nameBarrack + " ha le truppe necessarie per eseguire l'intervento ma è troppo lontana dal punto")
    else:
        print("La " + nameBarrack + " soddisfa tutti i requiditi per eseguire l'intervento con tempo "
              + str(distance))

def generateDirectedGraph(edges):
    graph = defaultdict(dict)
    for u, v, dist in edges:
        graph[u][v] = dist

    return graph


def dijkstra(graph, start):
    # The only criterium of adding a node to queue is if its distance has changed at the current step.
    queue = [start]
    minDistances = {v: float("inf") for v in graph}
    minDistances[start] = 0
    predecessor = {}

    while queue:
        currentNode = queue.pop(0)
        for neighbor in graph[currentNode]:
            # get potential newDist from start to neighbor
            newDist = minDistances[currentNode] + graph[currentNode][neighbor]

            # if the newDist is shorter to reach neighbor updated to newDist
            if newDist < minDistances[neighbor]:
                minDistances[neighbor] = min(newDist, minDistances[neighbor])
                queue.append(neighbor)
                predecessor[neighbor] = currentNode

    return minDistances, predecessor


# Unifrom Cost Search - shortest path between Source and Destination (Greedy)
def UCS(graph, start, goal):
    minDistances, predecessor = dijkstra(graph, start)

    path = []
    currentNode = goal
    while currentNode != start:
        if currentNode not in predecessor:
            #Path not reachable
            break
        else:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
    path.insert(0, start)

    return minDistances[goal]

if __name__ == '__main__':
    #Generazione della mappa
    map = createMap()
    directed_weighted_graph = generateDirectedGraph(map)
    #Generazione della KB
    kb = createKB()
    #Generazione dell'evento
    placeIncident = random_place(directed_weighted_graph)
    event = createIncident(placeIncident)
    #Addestramento del classificatote e classificazione incidente
    try:
        prediction = classify(event, "DataSet.csv")
    except FileNotFoundError:
        prediction = classify(event, "C:/Users/Utente/Desktop/Progetto_Icon_TF/DataSet.csv")   #da cancellare o modificare
    #Creazione dell'intervento in base alla classificazione dell'incidente
    intervation = Intervation(prediction, placeIncident)
    print("-----------Interrogazione Base di conoscenza-----------")
    strQueryCas1 = "caserma1Giusta("+str(intervation.getNumAgent())+","+\
                   str(intervation.getNumVeihcles())+","+\
                   str(intervation.getNumSpecialeVeihcles())+")."
    resultCas1 = list(kb.query(strQueryCas1))
    strQueryCas2 = "caserma2Giusta(" + str(intervation.getNumAgent()) + "," + \
                   str(intervation.getNumVeihcles()) + "," + \
                   str(intervation.getNumSpecialeVeihcles()) + ")."
    strQueryCas3 = "caserma3Giusta(" + str(intervation.getNumAgent()) + "," +\
                   str(intervation.getNumVeihcles()) + "," + \
                   str(intervation.getNumSpecialeVeihcles()) + ")."
    resultCas2 = list(kb.query(strQueryCas2))
    resultCas3 = list(kb.query(strQueryCas3))
    print("-----------Visaulizzazione Risultati-----------")
    if len(resultCas1) == 0 and len(resultCas2) == 0 and len(resultCas3) == 0:
        print("Le caserme disponibili non hanno le risorse necessarie per riuscire a risolvere l'incidente da soli")
    else:
        print("Le caserme consigliate per intervenire sono: \n")
        if len(resultCas1) > 0:
            determine_barrack(directed_weighted_graph, 'Cas1', intervation)
        if len(resultCas2) > 0:
            determine_barrack(directed_weighted_graph, 'Cas2', intervation)
        if len(resultCas3) > 0:
            determine_barrack(directed_weighted_graph, 'Cas3', intervation)
    print("-----------------------------------------------")
    '''map = createMap()
    directed_weighted_graph = generateDirectedGraph(map)
    print(directed_weighted_graph)
    shortest_path_cost, predecessor = dijkstra(directed_weighted_graph, 'A')
    print("shortest_path_cost from node a to every nodes in graph:", shortest_path_cost, "\npredecessor dictionary:",
          predecessor)
    distance = UCS(directed_weighted_graph, 'Cas1', 'I')
    print(distance)'''
