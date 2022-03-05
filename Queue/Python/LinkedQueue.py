class Node:
    def __init__(self,data,node):
        self.data = data
        self.next = node

class Queue:
    # Initialize the queue empty.
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    # O(1) adds values to queue.
    def enqueue(self,data):
        if not self.length():
            self.last = Node(data,None)
            self.first = self.last
            self.size += 1
            return
        else:
            self.last.next= Node(data,None)
            self.last = self.last.next
            self.size += 1
    # 0(1) removes first value in queue.
    def dequeue(self):
        if not self.length():
            print("Queue Empty")
            return
        temp = self.first.data
        self.first = self.first.next
        self.size -= 1
        return temp

    # O(1) return length of queue.
    def length(self):
        return self.size

    # O(1) clears queue
    def clear(self):
        self.first = None
        self.last = None
        self.size = 0

    # O(1) returns first value in queue
    def peek(self):
        if not self.length():
            print("Queue Empty.")
            return
        return self.first.data

    # O(n) class representation of a string
    def __str__(self):
        if not self.length():
            string = "[]"
        else:
            temp = self.first
            string = "["
            while temp:
                if not temp.next:
                    string += str(temp.data)
                    break
                string += (str(temp.data)+", ")
                temp = temp.next
            string += "]"
        return string

# Running all methods and created Test Cases: 
# Printing Queue and checking Peek upon intialization,
# Adding and Removing one value from Queue, 
# Checking Queue with no objects, 
# Adding 10 values to Queue,
# Printing Queue, checking Length, and Peek,
# Removing 2 values from Queue,
# Checking Peek of Queue and Length,
# Clearing Queue,
# Checking Queue Length, Peek, Removing from Empty Queue, and Printing Queue  
import random
if __name__ == "__main__":
    queue = Queue()
    print("Current Queue:"+str(queue))
    print("Queue peek: "+str(queue.peek()))
    print("Queue enqueue: 1")
    queue.enqueue(1)
    print("Queue Length: "+str(queue.length()))
    print("Current Queue:"+str(queue))
    print("Queue dequeue: "+str(queue.dequeue()))
    print("Queue Length: "+str(queue.length()))
    print("Queue dequeue: "+str(queue.dequeue()))
    for _ in range(10):
        rand = random.randint(0,50)
        print("Adding Number: "+str(rand))
        queue.enqueue(rand)
    print("Current Queue: "+str(queue))
    print("Queue Length: "+str(queue.length()))
    print("Queue peek: "+str(queue.peek()))
    print("Queue dequeue: "+str(queue.dequeue()))
    print("Queue dequeue: "+str(queue.dequeue()))
    print("Queue Length: "+str(queue.length()))
    print("Current Queue: "+str(queue))
    print("Queue peek: "+str(queue.peek()))
    print("Clear Queue: ")
    queue.clear()
    print("Queue Length: "+str(queue.length()))
    print("Current Queue:"+str(queue))
    print("Queue dequeue: "+str(queue.dequeue()))
    print("Queue peek: "+str(queue.peek()))