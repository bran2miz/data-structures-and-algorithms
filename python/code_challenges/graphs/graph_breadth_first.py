# class Node:
#     def __init__(self, value, next= None):
#         self.value = value
#         self.next = next

# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None

#     def isEmpty(self):
#         return self.front == None

#     def enqueue(self, value):
#         node = Node(value)
#         if self.front == None:
#             self.front = node
#             self.rear = node
#         else:
#             self.rear.next = node
#             self.rear = node
#     # different way to do enqueue
#     # def enqueue(self, value):
#     #     node = Node(value)
#     #     if self.rear:
#     #         self.rear.next = node
#     #     self.rear = node
#     #     self.front = self.front or self.rear


#     def dequeue(self):
#         if self.front == None:
#             raise Exception('Trying dequeue a empty queue')
#         temp = self.front
#         self.front = temp.next
#         temp.next = None
#         return temp.value

#     def peek(self):
#         if self.isEmpty():
#             raise Exception('Trying to peek from an empty queue')
#         return self.front.value

# class Graph:

#     def __init__(self):
#         self.adjacency_list = {}
#         self.nodes = []
#         # key will be the node, value adj node with a value of the edge

#     def add_node(self, value):
#         vertex = Vertex(value)
#         self.nodes.append(vertex)
#         self.adjacency_list[vertex] = {
#             'nodes': [],
#             'edges': []
#         }
#         return vertex

#     def add_edge(self, vertex_1, vertex_2, weight=1):
#         add_edge = Edge(vertex_1, vertex_2, weight)
#         try:
#             self.adjacency_list[vertex_1]['nodes'].append([vertex_2,weight])
#             self.adjacency_list[vertex_1]['edges'].append(add_edge)
#         except Exception:
#             print('Vertex not in the Graph')
#         try:
#             self.adjacency_list[vertex_2]['nodes'].append([vertex_1, weight])
#             self.adjacency_list[vertex_2]['edges'].append(add_edge)
#         except Exception:
#             print('Vertex not in the graph')
#             # Arguments: 2 nodes to be connected by the edge, weight (optional)
#             # Returns: nothing
#             # Adds a new edge between two nodes in the graph
#             # If specified, assign a weight to the edge
#             # Both nodes should already be in the Graph

#     def get_node(self):
#         return self.nodes
#             # Arguments: none
#             # Returns all nodes in graph as a collection (set, list, or similar)

#     def get_neighbor(self, vertex):
#         try:
#             return self.adjacency_list[vertex]['edges']
#         except Exception:
#             print('not in graph')
#             # Arguments: node
#             # Returns a collection of edges connected to the given node
#                 # Include the weight of connection in returned collection

#     def size(self):
#         return len(self.nodes)
#             # Arguments: none
#             # Returns the total number of nodes in the graph

#     def breadth_first(self,vertex = None):
#         if not vertex:
#             return []
#         queue = Queue()
#         lists = []
#         visited = set()

#         queue.enqueue(vertex)
#         visited.add(vertex)

#         while not queue.isEmpty():
#             front = queue.dequeue()
#             neighbor = self.get_neighbor(front)
#             lists.append(front)

#             for child in neighbor:
#                 if child.vertex_1 == front:
#                     if child.vertex_2 not in visited:
#                         queue.enqueue(child.vertex_2)
#                         visited.add(child.vertex_2)
#                 else:
#                     if child.vertex_1 not in visited:
#                         queue.enqueue(child.vertex_1)
#                         visited.add(child.vertex_1)
#         return lists

class Vertex():
    '''
    This class acts as a single vertex in a graph, containing just a value.
    '''
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return f'a node vertex with a value of {self.value}'

    def __repr__(self):
        return f'Vertex({self.value})'

class Edge():
    '''
    Class which tracks directed edges in a graph between two vertices, and their weight if one was given.
    '''
    def __init__(self, start_vert, end_vert=None, weight=0):
        self.start_vert = start_vert
        self.end_vert = end_vert
        self.weight = weight

    def __str__(self):
        return f'an edge between {self.start_vert} and {self.end_vert}, with a weight of {self.weight}'

    def __repr__(self):
        return f'Edge({self.start_vert, self.end_vert, self.weight})'

class Graph():
    '''
    A data structure implentation of a graph, or a collection of nodes each with a collection of edges which direct a connection between two vertices and track a weight value.
    '''
    def __init__(self) -> None:
        self.adj_list = {}

    def __str__(self):
        return (f'a graph defined as:\n{self.adj_list}')

    def __repr__(self):
        return (f'Graph({self.adj_list})')

    def add_node(self, value):
        '''
        Adds a new vertex to the graph.
        Input: value as any given value
        Output: the added node instance
        '''
        new_vert = Vertex(value)

        self.adj_list[new_vert.value] = []

        return new_vert

    def add_edge(self, start_vert, end_vert=None, weight=None):
        '''
        Adds a directed edge between two vertices to the graph. Also accepts a weight value for the edge.
        Input: start_vert as the starting node
               end_vert as the ending node
               weight as the weight value, default of None
        Output: None
        '''
        new_edge = Edge(start_vert, end_vert, weight)

        if start_vert.value in self.adj_list:
            if end_vert.value in self.adj_list or end_vert is None:
                self.adj_list[start_vert.value].append(new_edge)
            else:
                # exceptions are raised if the given node cannot be found in the graph
                raise Exception('ending vertex is not in graph!')
        else:
                raise Exception('starting vertex is not in graph!')

    def get_nodes(self):
        '''
        Returns a list of nodes in the graph.
        Input: None
        Output: a list of node values
        '''
        ret_list = []

        for vertex in self.adj_list:
                ret_list.append(vertex)

        return ret_list

    def get_neighbors(self, vert):
        '''
        Returns a list of edges belonging to a given vertex.
        Input: vert as an instance of a vertex that exists in the adjacency list.
        Output: a list of edges
        '''
        ret_list = []
        for edge in self.adj_list[vert]:
                ret_list.append(edge)
        return ret_list

    def breadth_first(self, vert):
        '''
        Given a node, returns a collection of breadth-first ordered nodes that can be reached from the given node.
        Input: Node
        Output: List of Nodes
        '''
        vert_queue = Queue()
        vert_queue.enqueue(vert)
        ret_list = []
        temp_adj_list = self.adj_list

        #continues enqueuing nodes in the order you encounter them, while loop continues until queue is empty
        while vert_queue.is_empty() is not True:
            temp = vert_queue.dequeue()

            # if the node is not in the adjacency list (or is None), we'll just return it in a list by itself
            if temp not in ret_list:
                ret_list.append(temp)

            if temp in temp_adj_list:
                # we create a clone adjency list (temp_adj_list) and use it to preserve original dat structure
                while len(temp_adj_list[temp]) != 0:
                    # takes the end_vert property from the edge to determine the node adjacency
                    added_vert = temp_adj_list[temp].pop(0).end_vert
                    vert_queue.enqueue(added_vert)
            else:
                return ret_list

        return ret_list

    def size(self):
        '''
        Returns how many nodes are in the graph.
        Input: None
        Output: integer value of items in graph
        '''
        return len(self.adj_list)


