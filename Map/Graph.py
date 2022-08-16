from Map.Node import Node

'''

Classe che implementa la realizzazione della
classe Graph

'''
class Graph:
    '''

    Comportamento:
        Il metodo "__init__" viene chiamato automaticamente appena andiamo
        a creare un oggetto e ci permette di inizializzare gli attributi della classe.

    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento

    Output
        Inizializzazione attributi:
        self.node;
        self.connections;

    '''
    def __init__(self):
        self.node = []
        self.connections = {}

    '''

    Comportamento:
        Il metodo "add_node" aggiunge un nodo al membro self.node

    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento
        node: nodo che sarà aggiunto al membro self.node

    Output
        Valori del membro self.node aggiornato

    '''
    def add_node(self, node):
        self.node.append(node)

    '''

    Comportamento:
        Il metodo "__oriented_graph_connection" connette due nodi con arco avente
        peso passato come argomento in un grafo orientato

    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento
        node1: nodo da connettere con l'altro nodo passato come argomento
        node2: nodo da connettere con l'altro nodo passato come argomento
        weight: peso dell'arco con cui connettere i nodi

    Output
        Connessione di node1 a node2 in un grafo orientato

    '''
    def __oriented_graph_connection(self, node1, node2, weight):
        if node1 in self.connections:
            all_nodes = self.connections.get(node1)
            all_nodes[node2] = weight
        else:
            self.connections[node1] = {node2: weight}

    '''

    Comportamento:
        Il metodo "__undirected_graph_connection" connette due nodi con arco avente
        peso passato come argomento in un grafo non orientato

    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento
        node1: nodo da connettere con l'altro nodo passato come argomento
        node2: nodo da connettere con l'altro nodo passato come argomento
        weight: peso dell'arco con cui connettere i nodi

    Output
        Connessione di node1 a node2 in un grafo non orientato

    '''
    def __undirected_graph_connection(self, node1, node2, weight):
        if node2 in self.connections:
            all_nodes = self.connections.get(node2)
            all_nodes[node1] = weight
        else:
            self.connections[node2] = {node1: weight}

    '''

    Comportamento:
        Il metodo "connect" connette due nodi con arco avente
        peso passato come argomento

    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento
        node1: nodo da connettere con l'altro nodo passato come argomento
        node2: nodo da connettere con l'altro nodo passato come argomento
        weight: peso dell'arco con cui connettere i nodi

    Output
        Connessione di node1 a node2 in un grafo

    '''
    def connect(self, node1, node2, weight):
        if type(weight).__name__ != "int" and type(weight).__name__ != "float":
            raise Exception("Peso non valido".format(type(weight).__name__))
        if node1 in self.node and node2 in self.node:
            self.__oriented_graph_connection(node1, node2, weight)
            # Utile solo se il grafo non è orientato--------------------
            self.__undirected_graph_connection(node1, node2, weight)
            # -----------------------------------------------------------
        else:
            raise Exception("L'arco non è valido".format(node1, node2))

    '''

    Comportamento:
        La funzione "path_weight" restituisce peso di arco tra due nodi

    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento
        node1: nodo connesso con l'altro nodo passato come argomento
        node2: nodo connesso con l'altro nodo passato come argomento

    Output
        Valore del peso dell'arco dato dalla connessione fra node1 e node2

    '''
    def path_weight(self, node1, node2):
        if node1 in self.connections and node2 in self.connections:
            support_connection = self.connections.get(node1)
            if node2 in support_connection:
                return support_connection.get(node2)
            else:
                raise Exception("L'arco non è valido".format(node1, node2))
        else:
            raise Exception("L'arco non è valido".format(node1, node2))

    '''

    Comportamento:
        La funzione "connection" restituisce una lista di nodi adiacienti a node

    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento
        node: nodo da cui prendere i nodi adiacenti ad esso

    Output
        Lista di nodi adiacenti a node

    '''
    def connection(self, node):
        connection_result = []
        if node in self.connections:
            for connection_nodes in self.connections.get(node):
                connection_result.append(connection_nodes)

        return connection_result

    '''

        Comportamento:
            La funzione "nodes" restituisce i nodi presenti nel membro self.node

        Input:
            self: rappresenta l'istanza dell'oggetto a cui si fa riferimento

        Output
            nodi presenti in self.node

        '''
    def nodes(self):
        return self.node

    '''

    Comportamento:
        La funzione "__str__" restituisce una rappresentazione dell'oggetto
        sotto forma di stringa

    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento

    Output:
        Valore del membro self.__class__.__name__

    '''
    def __str__(self):
        return self.__class__.__name__

    '''

    Comportamento:
        La funzione statica "euristic" calcola il valore assoluto di un numero,
        eliminando il segno negativo

    Input:
        node1: nodo con il quale calcolare il valore assoluto
        node2: nodo con il quale calcolare il valore assoluto
    
    Output:
        Valore assoluto tra la differenza del membro x dei nodi node1
        e node2 sommati alla differenza del membro y dei nodi node1 e node2

    '''
    @staticmethod
    def euristic(node1, node2):
        return abs(node1.get_x() - node2.get_x()) + abs(node1.get_y() - node2.get_y())

    '''

    Comportamento:
        La funzione "min_search" data una lista restituisce il nodo
        avente il parametro totalDistanceValue minimo.
        (euristica + distanza stimata)

    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento       
        list: lista dalla quale trovare il nodo avente il parametro 
              totalDistanceValue minimo
        
    Output:
        Valore minimo nei nodi del parametro totalDistanceValue

    '''
    def min_search(self, list: list()):
        min = Node("", "", 100, 100)
        min.set_real_distance_value(9999)
        min.set_heuristic_distance_value(9999)

        for item in list:
            item: Node()
            if item.totalDistanceValue <= min.totalDistanceValue:
                min = item

        return min

    '''

    Comportamento:
        La funzione "a_strar" calcola il percorso migliore per arrivare
        da un nodo iniziale (start) a un nodo obiettivo (goal)

    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento       
        start: nodo iniziale da cui raggiungere l'obiettivo (goal)
        goal: nodo obiettivo da raggiungere partendo da un nodo iniziale (start)

    Output:
        percorso minimo tra il nodo iniziale (start) e il nodo obiettivo (goal)

    '''
    def a_star(self, start, goal):

        if start not in self.connections or goal not in self.connections:
            raise Exception("Non sono stati forniti nodi validi.")

        open_list = list()
        start.set_real_distance_value(0)
        start.set_heuristic_distance_value(self.euristic(start, goal))
        closed_list = list()
        open_list.append(start)

        while len(open_list) != 0:
            current = self.min_search(open_list)
            open_list.remove(current)
            if current.is_same(goal):
                break
            successor: Node
            for successor in self.connection(current):
                successor_current_cost = current.realDistanceValue + self.path_weight(current, successor)
                if successor in open_list:
                    if successor.realDistanceValue <= successor_current_cost:
                        break
                elif successor in closed_list:
                    if successor.realDistanceValue <= successor_current_cost:
                        continue
                else:
                    open_list.append(successor)
                    successor.set_heuristic_distance_value(self.euristic(successor, goal))
                successor.set_real_distance_value(successor_current_cost)
                successor.set_parent(current)
            closed_list.append(current)

    '''

    Comportamento:
        La funzione "print_path" stampa il percorso trovato per arrivare
        al nodo destinazione

    Input:
        self: rappresenta l'istanza dell'oggetto a cui si fa riferimento       
        node: nodo da cui stampae il path
        path: percorso del nodo

    Output:
        stampa del percorso del nodo

    '''
    def print_path(self, node, path):
        node: Node()

        if node.parent == None:
            path.append(node)
        else:
            self.print_path(node.parent, path)
            path.append(node)