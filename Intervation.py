#Qua va importato la map
from Map.Node import Node

class Intervation:
    grade: int #grado di urgenza dell'intervento
    numAgent: int #numero di agenti necessari
    numVehicles: int # numero di veicoli necessari
    numSpecialVehicles: int #numero di veicoli speciali necessari
    timeLimit: int # tempo massimo di attesa per l'intervento
    placeIntervention: Node

    def __init__(self, grade: int, node: Node):
        self.grade = grade
        self.placeIntervention = node
        #in base al grado assegnato vengono avvalorati gli altri valori

        if grade == 1:
            self.createIntevationLevel1()
        elif grade == 2:
            self.createIntevationLevel2()
        elif grade == 3:
            self.createIntevationLevel3()
        elif grade == 4:
            self.createIntevationLevel4()
        print(self.__str__())

    def getGrade(self):
        return self.grade

    def getNumAgent(self):
        return self.numAgent

    def getNumVeihcles(self):
        return self.numVehicles

    def getNumSpecialeVeihcles(self):
        return self.numSpecialVehicles

    def getTimeLimit(self):
        return self.timeLimit

#Avvalora le varie truppe richieste per un intervento di grado 1
    def createIntevationLevel1(self):
        self.numAgent = 2
        self.numVehicles = 2
        self.numSpecialVehicles = 0
        self.timeLimit = 40

    # Avvalora le varie truppe richieste per un intervento di grado 2
    def createIntevationLevel2(self):
        self.numAgent = 7
        self.numVehicles = 5
        self.numSpecialVehicles = 0
        self.timeLimit = 30

    # Avvalora le varie truppe richieste per un intervento di grado 3
    def createIntevationLevel3(self):
        self.numAgent = 10
        self.numVehicles = 7
        self.numSpecialVehicles = 1
        self.timeLimit = 25

    # Avvalora le varie truppe richieste per un intervento di grado 4
    def createIntevationLevel4(self):
        self.numAgent = 15
        self.numVehicles = 10
        self.numSpecialVehicles = 5
        self.timeLimit = 20

#descrive l'intervento in base ai vari valori degli attributi
    def __str__(self):
        return "\n E' STATO RILEVATO UN INCIDENTE DI GRADO" + str(self.grade) + "\n\n" \
                "Per risolvere l'incidente al meglio sarà necessario programmare un intervento che rispetti" \
                                                                                " le seguenti condizioni\n" \
                "-Tempo richiesto per l'intervento: <= " + str(self.timeLimit) + "min \n" \
                "-Numero di agenti richiesto: >= " + str(self.numAgent) + "\n" \
                "-Numero di veicoli necessari: >= " + str(self.numVehicles) + "\n" \
                "-Numeto di veicoli speciali necessari: >= " + str(self.numSpecialVehicles)\
