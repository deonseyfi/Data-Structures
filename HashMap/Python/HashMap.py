from SingleLinkedList import SingleLinkedList

class HashMap:
    def __init__(self):
        self.size = 50
        self.table = [SingleLinkedList() for _ in range(self.size)]
        self.inputs = 0

    # O(1) converts key to hash value in table of the map.
    def key_to_hash(self,key):
        return hash(key) % self.size

    # Best Case O(1) where there a Node doesnt exsist in the hashed key index.
    # Worst Case O(n) where there does exsists a Node in the hashed key index.
    def set(self,key,value):
        key_index = self.key_to_hash(key)
        if not self.table[key_index].length():
            self.table[key_index].add(key,value)
            self.inputs += 1
            return
        else:
            temp = self.table[key_index].head
            while temp:
                if temp.key == key:
                    temp.value = value
                    self.inputs += 1
                    return
                temp = temp.next
            self.table[key_index].add(key,value)
            self.inputs += 1
            return

    def get(self,key):
        key_index = self.key_to_hash(key)
        if not self.table[key_index].length(): 
            return "Key Not in HashMap."
        else:
            temp = self.table[key_index].head
            while temp:
                if temp.key == key:
                    return temp.value
                temp = temp.next
            return "Key Not in HashMap."


    # O(n) creates a string representation of the hashmap.
    def __str__(self):
        if not self.inputs:
            return "{}"
        string = "{\n"
        for index,val in enumerate(self.table):
            if val.length():
                string += "Hash Index: "+str(index)+"\n\n"
                string += (str(val) + "\n\n")
        string = string[:-1]
        string += "\n}"
        return string

if __name__ == "__main__":
    hashmap = HashMap()
    print(hashmap)
    hashmap.set(1,2)
    hashmap.set(3,4)
    hashmap.set(1,3)
    hashmap.set("string",1)
    print(hashmap)
    print(hashmap.get(1))
    print(hashmap.get(3))
    print(hashmap.get("string"))
    print(hashmap.get(51))

