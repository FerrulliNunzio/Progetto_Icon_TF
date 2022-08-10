from Map.Node import Node

class Graph:
    def __init__(self):
        self.node = []
        self.connections = {}

    def add_node(self, node):
        self.node.append(node)

    def __oriented_graph_connection(self, node1, node2, weight):
        if node1 in self.connections:
            all_nodes = self.connections.get(node1)
            all_nodes[node2] = weight
        else:
            self.connections[node1] = {node2: weight}

    def __undirected_graph_connection(self, node1, node2, weight):
        if node2 in self.connections:
            all_nodes = self.connections.get(node2)
            all_nodes[node1] = weight
        else:
            self.connections[node2] = {node1: weight}

    def connect(self, node1, node2, weight):
        if type(weight).__name__ != "int" and type(weight).__name__ != "float":
            raise Exception("Peso non valido".format(type(weight).__name__))
        if node1 in self.node and node2 in self.node:
            self.oriented_graph_connection(node1, node2, weight)
            # Utile solo se il grafo non è orientato--------------------
            self.undirected_graph_connection(node1, node2, weight)
            # -----------------------------------------------------------
        else:
            raise Exception("L'arco non è valido".format(node1, node2))

    def path_weight(self, node1, node2):
        if node1 in self.connection and node2 in self.connection:
            support_connection = self.connections.get(node1)
            if node2 in support_connection:
                return support_connection.get(node2)
            else:
                raise Exception("L'arco non è valido".format(node1, node2))
        else:
            raise Exception("L'arco non è valido".format(node1, node2))

    def connection(self, node):
        connection_result = []
        if node in self.connections:
            for connection_nodes in self.connections.get(node):
                connection_result.append(connection_nodes)

        return connection_result

    def nodes(self):
        return self.node

    def __str__(self):
        return self.__class__.__name__

    @staticmethod
    def euristic(node1, node2):
        return abs(node1.get_x() - node2.get_x()) + abs(node1.get_y() - node2.get_y())

    def min_search(self, list: list()):
        min = Node("", 100, 100)
        min.set_real_distance_value(9999)
        min.set_heuristic_distance_value(9999)

        for item in list:
            item: Node()
            if item.totalDistanceValue <= min.totalDistanceValue:
                min = item

        return min

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

    def print_path(self, node, path):
        node: Node()

        if node.parent == None:
            path.append(node)
        else:
            self.print_path(node.parent, path)
            path.append(node)