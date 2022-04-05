class Node:
    def __init__(self, value, next= None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def enqueue(self, value):
        node = Node(value)
        if self.front == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    # different way to do enqueue
    # def enqueue(self, value):
    #     node = Node(value)
    #     if self.rear:
    #         self.rear.next = node
    #     self.rear = node
    #     self.front = self.front or self.rear


    def dequeue(self):
        if self.front == None:
            raise Exception('Trying dequeue a empty queue')
        temp = self.front
        self.front = temp.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.isEmpty():
            raise Exception('Trying to peek from an empty queue')
        return self.front.value

class Graph:

    def __init__(self):
        self.adjacency_list = {}
        # key will be the node, value adj node with a value of the edge

    def add_node(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    def add_edge(self, vertex_1, vertex_2, weight=1):
        if vertex_1 and vertex_2 not in self.adjacency_list:
            raise Exception
        edge = Edge(vertex_2,weight)
        self.adjacency_list[vertex_1].append(edge)
            # Arguments: 2 nodes to be connected by the edge, weight (optional)
            # Returns: nothing
            # Adds a new edge between two nodes in the graph
            # If specified, assign a weight to the edge
            # Both nodes should already be in the Graph

    def get_node(self):
        return list(self.adjacency_list.keys())
            # Arguments: none
            # Returns all nodes in graph as a collection (set, list, or similar)

    def get_neighbor(self, vertex):
        return self.adjacency_list[vertex]
            # Arguments: node
            # Returns a collection of edges connected to the given node
                # Include the weight of connection in returned collection

    def size(self):
        return len(self.adjacency_list)
            # Arguments: none
            # Returns the total number of nodes in the graph

    def breadth_first(self,vertex):
        nodes = list()
        breadth = Queue()
        visited = set()
        breadth.enqueue(vertex)
        visited.add(vertex)
        while breadth:
            front = breadth.dequeue()
            nodes.append(front)
            for child in nodes:
                if child not in visited:
                    visited.add(child)
                    breadth.enqueue(child)
        return nodes

class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex,weight=1):
        self.vertex = vertex
        self.weight = weight
