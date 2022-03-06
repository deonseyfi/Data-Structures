class Node:
    def __init__(self,key,value,node):
        self.key = key
        self.value = value
        self.next = node

class SingleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # O(1) adds data to the singe linked list.
    def add(self,key,value):
        if not self.length():
            self.tail = Node(key,value,None)
            self.head = self.tail
            self.size += 1
            return 
        self.tail.next = Node(key,value,None)
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
    def add_to_index(self,index,key,value):
        if index > self.length() and not index < -1:
            print("Index out of bounds.")
            return
        if index == 0:
            self.head = Node(key,value,self.head)
            self.size += 1
            return
        if index == self.length():
            self.add(key,value)
            return
        temp = self.head
        count = 0
        while count < index and temp:
            if count == index-1: 
                temp.next = Node(key,value,temp.next)
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
        return (self.head.key,self.head.value)

    # O(1) return data of the tail of single linked list.
    def peek_last(self):
        return (self.tail.key,self.tail.value)

    # O(1) returns size of single linked list.
    def length(self):
        return self.size

    # O(n) string representation of class.
    def __str__(self):
        if not self.length():
            return "[]"
        temp = self.head
        string = ""
        while temp:
            if not temp.next:
                string += "(Key: "+str(temp.key)+", Value: "+str(temp.value)+")"
                break
            string += "(Key: "+str(temp.key)+", Value: "+str(temp.value)+")  "
            temp = temp.next
        return string 
