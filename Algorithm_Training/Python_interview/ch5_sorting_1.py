class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Linked_List:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
    def append_node(self, data):
        new_node = Node(data)

a = Linked_List(0)
a.