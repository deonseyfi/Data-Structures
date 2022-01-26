class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None

    def set_node(self,data,Node):
        self.data = data
        self.nextNode = Node

    def get_data(self):
        return self.data
    
    def get_next_node(self):
        return self.next_node

    def set_data(self,data):
        self.data = data
    
    def set_next_node(self,node):
        self.next_node = node
