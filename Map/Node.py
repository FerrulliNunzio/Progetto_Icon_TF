'''

Classe che implementa la realizzazione della
classe Node

'''
class Node:

    # Variabile che contiene la somma del valore della distanza Euristica e il valore della distanza effettiva:
    # Distanza totale = Distanza Euristica + Distanza Effettiva
    totalDistanceValue: int = 0

    # Variabile che contiene il valore della Distanza Effettiva
    realDistanceValue: int = 0

    # Variabile che contiene il valore della Distanza Euristica
    heuristicDistanceValue: int = 0

    '''
    
    Comportamento:
        Il metodo "__init__" viene chiamato automaticamente appena andiamo
        a creare un oggetto e ci permette di inizializzare gli attributi della classe.
    
    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento
        value: variabile che inizializzerà il valore di self.value
        x: variabile che inizializzerà il valore di self.x
        y: variabile che inizializzerà il valore di self.y
        
    Output
        Inizializzazione attributi:
        self.value;
        self.x;
        self.y
        
    '''
    def __init__(self, value, x, y):
        self.parent = None
        self.value = value
        self.x = x
        self.y = y

    '''
    
    Comportamento:
        Il metodo "set_parent" imposta il valore del nodo genitore
        del nodo corrente nel grafo
    
    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento
        parent_node: variabile contente il valore che sarà assegnato
                     alla variabile self.parent_node
                     
    Output:
        Valore aggiornato della variabile self.parent_node
    
    '''
    def set_parent(self, parent_node):
        self.parent = parent_node

    '''
    
    Comportamento:
        Il metodo "set_real_distance_value" imposta il valore della variabile realDistanceValue
        e calcola il valore della variabile totalDistanceValue
    
    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento
        distance_value: variabile contente il valore che sarà assegnato
                        alla variabile self.realDistanceValue
                     
    Output:
        Valore aggiornato della variabile self.realDistanceValue
    
    '''
    def set_real_distance_value(self, distance_value):
        self.realDistanceValue = distance_value
        self.set_total_distance_value()

    '''

    Comportamento:
        Il metodo "set_heuristic_distance_value" imposta il valore della variabile heuristicDistanceValue
        e calcola il valore della variabile totalDistanceValue

    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento
        distance_value: variabile contente il valore che sarà assegnato
                        alla variabile self.heuristicDistanceValue

    Output:
        Valore aggiornato della variabile self.heuristicDistanceValue

    '''
    def set_heuristic_distance_value(self, distance_value):
        self.heuristicDistanceValue = distance_value
        self.set_total_distance_value()

    '''

    Comportamento:
        Il metodo "set_total_distance_value" calcola il valore della variabile totalDistanceValue

    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento

    Output:
        Valore aggiornato della variabile self.totalDistanceValue

    '''
    def set_total_distance_value(self):
        self.totalDistanceValue = self.realDistanceValue + self.heuristicDistanceValue

    '''
    
    Comportamento:
        La funzione "get_x" restituisce il valore del membro self.x

    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento

    Output:
        Valore del self.x

    '''
    def get_x(self):
        return self.x

    '''

    Comportamento:
        La funzione "get_y" restituisce il valore del membro self.y

    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento

    Output:
        Valore del self.y

    '''
    def get_y(self):
        return self.y

    '''

    Comportamento:
        La funzione "is_same" di tipo booleano restituisce true se il valore del
        membro self.value è uguale al valore della valore passato nella funzione.
        Restituisce false altrimenti

    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento
        node: variabile che andrà confrontata con l'istanza dell'oggetto
    Output:
        true se slef.value == node.value, false altrimenti

    '''
    def is_same(self, node):
        return self.value == node.value

    '''

    Comportamento:
        Funzione "__str__" che restituisce una rappresentazione dell'oggetto
        sotto forma di stringa

    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento

    Output:
        Valore del membro self.x

    '''
    def __str__(self):
        return str(self.value)