class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self):
        string = str(self.data)+ " "
        x = self.next 
        while x:
            string += (str(x.data)+" ")
            x = x.next
        return string

class LinkedList():
    def __init__(self):
        self.first = None
        self.last = None
    
    def add(self,data):
        temp = Node(data)
  
        if self.first is None:
    
            self.first = temp
            self.last = temp
        else:
            self.last.next = self.last = Node(data)

    def remove(self,data):
        return 0

    def count(self):
        temp = self.first
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
    def __str__(self):
        temp = self.first
        string = "["
        while temp:
            string += (str(temp.data)+", ")
            temp = temp.next
        return string+"]"

    def reverse(self):
        prev = None
        curr = self.first
        while curr:
            print(curr)
            nex = curr.next
            print(nex)
            curr.next = prev
            print(curr)
            prev = curr
            print("prev")
            print(prev)
            curr = nex
            print(curr)
        self.first = prev
        print("self")
        print(self.first)

    def reverseDeon(self):
        new = None
        print(self.first)
        while self.first:
            curr = Node(self.first.data)
            print(curr)
            self.first = self.first.next
            print(self.first)
            curr.next = new
            print("curr")
            print(curr)
            new = curr
            print(new)
        self.first = new
            

if __name__ == "__main__":
    x = LinkedList()


    x.add(3)
    x.add(4)
    x.add(5)
    x.add(6)
    print(x)
    x.reverse()
    x.add(7)
    print(x)
   # print("reverse deon")
   # x.reverseDeon()
   # print(x)
    #x.add(7)
    #print(x)

    
