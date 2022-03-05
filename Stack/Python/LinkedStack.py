class Node:
    def __init__(self,data,node):
        self.data = data
        self.next = node
    
class Stack:
    def __init__(self):
        self.size = 0
        self.top = None

    def pop(self):
            if not self.length():
                print("Empty Stack.")
                return
            temp = self.top.data
            self.top = self.top.next
            return temp
    def push(self,data):
            self.top = Node(data,self.top)
            self.size += 1
    def clear(self):
        self.size = 0
        self.top = None

    def peek(self):
        if not self.length():
            print("Stack Empty peek.")
            return
        return self.top.data

    def length(self):
        return self.size
    def print_stack(self):
        if not self.length():
            print("Empty Stack.")
            return
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    stack = Stack()
    stack.pop()
    stack.print_stack()
    stack.peek()
    for i in range(10):
        stack.push(i)
    stack.print_stack()
    print(stack.length())
    print(stack.peek())
    stack.clear()
    print(stack.length())
    stack.peek()
    stack.pop()
    stack.print_stack()
