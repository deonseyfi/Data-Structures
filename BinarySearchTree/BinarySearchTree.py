

class BSTNode():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add(self,data): #O(n)
        
        if data == self.data:
            return 

        else:
            if self.data == None:
                self.data = data
            elif data < self.data:
                if self.left is None:
                    self.left = BSTNode(data)
                else:
                    self.left.add(data)
            else:
                if self.right is None:
                    self.right = BSTNode(data)
                else:
                    self.right.add(data)
            
        
    def remove(self,data):
        print(self.data)
        print(data)
        if self.data == None:
            return self
        if data < self.data:
            print("Left")
            self.left = self.left.remove(data)
        elif data > self.data:
            print("Right")
            self.right = self.right.remove(data)

        else:
            print("Matching value")
            
            if self.left is None and self.right:
                t = self.right
                return t
            elif self.right is None and self.left:
      
                t = self.left
                return t
            elif self.right is None and self.left is None:
                return self.right
            else:
                min_val = self.right.findMin()
                self.data = min_val
                self.right.remove(min_val)
        return self

    def findMin(self):
        x = self

        while x:
            a = x
            x = x.left

        return a.data
            

    def getheight(self):
        height = 0
        if self is not None:
            if self.left is not None and self.right is not None:
                height = 1 + max(self.left.getheight(),self.right.getheight())
            elif self.left is None and self.right:
                height = 1+ self.right.getheight()
            elif self.right is None and self.left:
                height = 1 + self.left.getheight()
        return height

    def getNumberOfNodes(self):
        l_count = 0
        r_count = 0
        if self.left:
            l_count = self.left.getNumberOfNodes()
        if self.right:
            r_count = self.right.getNumberOfNodes()
        return 1 + l_count + r_count

    def printTreeLevelOrder(self):
        q = []
        q.append(self)
        while q:
            p = q.pop(0)
            print(p.data)
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)

    def printTreeInOrder(self):
        if self:
            if self.left:
                self.left.printTreeInOrder()
            print(self.data)
            if self.right:
                self.right.printTreeInOrder()


    def printTreePreOrder(self):
        if self:
            print(self.data)
            if self.left:
                self.left.printTreePreOrder()
            if self.right:
                self.right.printTreePreOrder()


    def printTreePostOrder(self):
        if self:
            if self.left:
                self.left.printTreePostOrder()
            if self.right:
                self.right.printTreePostOrder()
            print(self.data)
if __name__ == "__main__":
    x = BSTNode(10)
    x.add(2)
    x.add(11)
    x.add(7)
    x.add(1)
    x.add(6)
    x.add(5)
    x.add(4)
    x.add(8)
    print("Level Order")
    #x.printTreeLevelOrder()
    x.printTreePreOrder()
    print("Removing")
    x.remove(2)
    x.printTreeLevelOrder()

    
