import random as random
from pyswip import Prolog
import Intervation
from Classifier import classify

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
