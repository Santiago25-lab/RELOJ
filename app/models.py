# app/models.py
from datetime import datetime

# --- COMPONENTE 1: ESTRUCTURAS DE DATOS ---
class Node:
    """Nodo para la lista circular doblemente enlazada."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    """Lista circular doblemente enlazada."""
    def __init__(self):
        self.head = None
        self.nodes = {}

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
        self.nodes[data] = new_node

    def get_node(self, data):
        return self.nodes.get(data)

# --- COMPONENTE 2: MODELO DE DATOS DEL RELOJ ---
class ClockModel:
    """Gestiona los datos del reloj usando listas circulares."""
    def __init__(self):
        self.hours_list = self._create_time_list(24)
        self.minutes_list = self._create_time_list(60)
        self.seconds_list = self._create_time_list(60)

    def _create_time_list(self, limit):
        time_list = CircularDoublyLinkedList()
        for i in range(limit):
            time_list.append(i)
        return time_list

    def get_current_time_nodes(self):
        now = datetime.now()
        hour_node = self.hours_list.get_node(now.hour)
        minute_node = self.minutes_list.get_node(now.minute)
        second_node = self.seconds_list.get_node(now.second)
        return hour_node, minute_node, second_node
