from collections import defaultdict
"""
Creating a different implementation of graph.
I am using a dictionary of dictionaries as the representation of the graph.
Within the defaultdictionary, the key is all the exsisting verticies. The value is a dictionary where the key is the pointed node and the value is its weight.
This is a one-way pointing graph.

The reasoning for this approach is that it is as efficient as possible so it can scale and we will not have to traverse through every possible vertix like
a static graph using a matrix.

We do not use a list of lists because when accessing a node, we do not want to traverse through the entire list to find it.

Its limitations is that we are restricted to one route from Node A to Node B. You can not have multiple routes from Node A to Node B.

You are allowed to have a Node to point to itself.
"""
class WeightedGraph:
    def __init__(self):
        self.graph = defaultdict(dict)

    # O(1) creates vertex NodeA and sets the edge connection between NodeA and NodeB with its weight.
    # If nodeB does not exsist in the graph, it creates the key in the graph where it points to no other Node.
    def add(self,nodeA,nodeB,weight):
        self.graph[nodeA].update({ nodeB:weight })
        if self.graph.get(nodeB,"-1") == "-1":
            self.graph[nodeB]
        return

    # O(n) string represenation of the graph.
    def __str__(self):
        return str(self.graph)

    # O(K) where K = the number of verticies within the graph.
    # Returns the number of verticies within the graph.
    def get_verticies(self):
        return list(self.graph.keys())

    # O(K) where K = the number of verticies within the graph.
    # Returns the count of verticies within the graph.
    def get_vert_counts(self):
        return len(self.graph.keys())

    # O(1) checks to see if there is an edge between NodeA and NodeB.
    def has_edge(self,nodeA,nodeB):
        if self.graph.get(nodeA,"-1") == "-1":
            return False
        if self.graph[nodeA].get(nodeB,"-1") == "-1":
            return False
        return True

    # O(k) where K = the number of verticies within the graph.
    # Clears the graph and all its connected edges.
    def clear(self):
        self.graph.clear()
        return

if __name__ == "__main__":
    graph = WeightedGraph()

    print(graph)
    graph.add(1,2,5)
    graph.add(1,3,3)
    graph.add(2,3,4)
    print(graph)
    graph.add(2,3,5)
    print(graph)
    print(graph.get_verticies())
    graph.add(3,3,1)
    print(graph)
    print(graph.get_vert_counts())
    print(graph.has_edge(4,1))
    print(graph.has_edge(3,2))
    print(graph.has_edge(1,2))
    graph.clear()
    print(graph)
    graph.add(1,2,5)
    print(graph)