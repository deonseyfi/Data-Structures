class Node:
    def __init__(self,data,node):
        self.data = data
        self.next = node

class SingleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # O(1) adds data to the singe linked list.
    def add(self,data):
        if not self.length():
            self.tail = Node(data,None)
            self.head = self.tail
            self.size += 1
            return 
        self.tail.next = Node(data,None)
        self.tail = self.tail.next
        self.size += 1
        return 

    #O(n) removes the specfic index of the list, being in range of the 
    def remove_index(self,index):
        if not index < self.length() and not index < -1:
            print("Index Out of Bounds")
            return
        temp = self.head
        prev = temp
        count = 0
        while count <= index and temp:
            if count == self.length() - 1:
                self.tail = prev
                self.tail.next = None
                self.size -= 1
                return
            elif count == index:
                prev.next = temp.next
                self.size -= 1
                return 
            prev = temp
            temp = temp.next
            count += 1
        return

    # O (k) where k : 0 <= k <= n-1. n is the size of the list. Worst Case O(n-1)
    # Adds a values to a index in the list.
    def add_to_index(self,index,data):
        if index > self.length() and not index < -1:
            print("Index out of bounds.")
            return
        if index == 0:
            self.head = Node(data,self.head)
            self.size += 1
            return
        if index == self.length():
            self.add(data)
            return
        temp = self.head
        count = 0
        while count < index and temp:
            if count == index-1: 
                temp.next = Node(data,temp.next)
                self.size += 1
                break
            count += 1
            temp = temp.next
        return 

    # O(n) reveres the SingleLinkedList and assigns the linked list tail properly.
    def reverse(self):
        curr = self.head
        prev = None
        set_tail = True
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            if set_tail:
                self.tail = prev
                set_tail = False
            curr = nex
        self.head = prev

    
    #O(1) clears the data of the single linked list.
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0   
        return

    # O(1) return data of the head of single linked list.
    def peek_first(self):
        return self.head.data

    # O(1) return data of the tail of single linked list.
    def peek_last(self):
        return self.tail.data

    # O(1) returns size of single linked list.
    def length(self):
        return self.size

    # O(n) string representation of class.
    def __str__(self):
        if not self.length():
            return "[]"
        temp = self.head
        string = "["
        while temp:
            if not temp.next:
                string += str(temp.data)
                break
            string += (str(temp.data)+", ")
            temp = temp.next
        return string + "]"

if __name__ == "__main__":
    Llist = SingleLinkedList()
    print("Print Empty List: "+str(Llist))
    for i in range(1,5):
        Llist.add(i)
    print("Print List Filled With Data: "+str(Llist))
    Llist.remove_index(2)
    print("Removed index 2 from List: "+str(Llist))
    Llist.add(5)
    print("Adding 5 to the Llist: "+str(Llist))
    Llist.remove_index(3)
    print("Removing index 3 from List: "+str(Llist))
    Llist.add(3)
    print("Adding 3 to the Llist: "+str(Llist))
    Llist.remove_index(2)
    print("Removed index 2 from List: "+str(Llist))
    Llist.add_to_index(2,10)
    print("Adding 10 to index 2 of List: "+str(Llist))
    Llist.remove_index(2)
    print("Removed index 2 from List: "+str(Llist))
    Llist.add_to_index(0,9)
    print("Adding 9 to index 0 of List: "+str(Llist))
    Llist.add_to_index(4,8)
    print("Adding 8 to index 4 of List: "+str(Llist))
    Llist.reverse()
    print("Reversing List: "+str(Llist))
    Llist.add(10)
    print("Adding 10 to the List: "+str(Llist))