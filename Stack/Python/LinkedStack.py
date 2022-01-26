from Node import Node


temp = Node("string")

temp.set_next_node(Node("next"))


tempTemp = temp


print(tempTemp.get_data())
tempTemp = tempTemp.get_next_node()
print(tempTemp.get_data())




class LinkedStack:
    def __init__(self):
        self.top_node = None
    
    def pop(self):
        if self.topNode.is_empty():
            raise Exception("Stack is Empty")
        temp_data = self.topNode.get_data() 
        self.top_node = self.top_node.get_next_node()
        return 