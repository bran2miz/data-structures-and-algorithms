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
        self.nodes = []
        # key will be the node, value adj node with a value of the edge

    def add_node(self, value):
        vertex = Vertex(value)
        self.nodes.append(vertex)
        self.adjacency_list[vertex] = {
            'nodes': [],
            'edges': []
        }
        return vertex

    def add_edge(self, vertex_1, vertex_2, weight=1):
        add_edge = Edge(vertex_1, vertex_2, weight)
        try:
            self.adjacency_list[vertex_1]['nodes'].append([vertex_2,weight])
            self.adjacency_list[vertex_1]['edges'].append(add_edge)
        except Exception:
            print('Vertex not in the Graph')
        try:
            self.adjacency_list[vertex_2]['nodes'].append([vertex_1, weight])
            self.adjacency_list[vertex_2]['edges'].append(add_edge)
        except Exception:
            print('Vertex not in the graph')
            # Arguments: 2 nodes to be connected by the edge, weight (optional)
            # Returns: nothing
            # Adds a new edge between two nodes in the graph
            # If specified, assign a weight to the edge
            # Both nodes should already be in the Graph

    def get_node(self):
        return self.nodes
            # Arguments: none
            # Returns all nodes in graph as a collection (set, list, or similar)

    def get_neighbor(self, vertex):
        try:
            return self.adjacency_list[vertex]['edges']
        except Exception:
            print('not in graph')
            # Arguments: node
            # Returns a collection of edges connected to the given node
                # Include the weight of connection in returned collection

    def size(self):
        return len(self.nodes)
            # Arguments: none
            # Returns the total number of nodes in the graph

    def breadth_first(self,vertex = None):
        if not vertex:
            return []
        queue = Queue()
        lists = []
        visited = set()

        queue.enqueue(vertex)
        visited.add(vertex)

        while not queue.isEmpty():
            front = queue.dequeue()
            neighbor = self.get_neighbor(front)
            lists.append(front)

            for child in neighbor:
                if child.vertex_1 == front:
                    if child.vertex_2 not in visited:
                        queue.enqueue(child.vertex_2)
                        visited.add(child.vertex_2)
                else:
                    if child.vertex_1 not in visited:
                        queue.enqueue(child.vertex_1)
                        visited.add(child.vertex_1)
        return lists


class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex_1,vertex_2,weight=1):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.weight = weight

