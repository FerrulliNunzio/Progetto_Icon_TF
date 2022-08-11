class Node:
    totalDistanceValue: int = 0
    realDistanceValue: int = 0
    heuristicDistanceValue: int = 0

    def __init__(self, value, x, y):
        self.parent = None
        self.value = value
        self.x = x
        self.y = y

    def set_parent(self, parent_node):
        self.parent = parent_node

    def set_real_distance_value(self, distance_value):
        self.realDistanceValue = distance_value
        self.set_total_distance_value()

    def set_heuristic_distance_value(self, distance_value):
        self.heuristicDistanceValue = distance_value
        self.set_total_distance_value()

    def set_total_distance_value(self):
        self.totalDistanceValue = self.realDistanceValue + self.heuristicDistanceValue

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def is_same(self, node):
        return self.value == node.value

    def __str__(self):
        return str(self.value)