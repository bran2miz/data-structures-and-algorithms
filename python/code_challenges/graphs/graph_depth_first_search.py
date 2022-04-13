from stack import Stack

class Node:
    def __init__(self, value, next= None):
        self.value = value
        self.next = next

class Vertex():

    def __init__(self, value=None):
        self.value = value

    def __repr__(self):
        return f'Vertex({self.value})'

class Edge():

    def __init__(self, vertex_1, vertex_2=None, weight=0):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.weight = weight


class Graph():
    def __init__(self) -> None:
        self.adjacency_list = {}

    def add_node(self, value):

        vertex = Vertex(value)

        self.adjacency_list[vertex] = []

        return vertex

    def add_edge(self, vertex_1, vertex_2=None, weight=None):

        edge = Edge(vertex_1, vertex_2, weight)

        if vertex_1 in self.adjacency_list:
            if vertex_2 in self.adjacency_list or vertex_2 is None:
                self.adjacency_list[vertex_1].append(edge)
            else:
                # exceptions are raised if the given node cannot be found in the graph
                raise Exception('undefined ending vertex..')
        else:
                raise Exception('undefined starting vertex')

    def get_nodes(self):
        lists = []

        for vertex in self.adjacency_list:
                lists.append(vertex)

        return lists

    def get_neighbors(self, vert):
        lists = []

        for edge in self.adjacency_list[vert]:
                lists.append(edge)
        return lists

    def depth_first(self, vertex):

        if vertex == None:
            return [None]
        elif len(self.get_neighbors(vertex)) == 0:
            return [vertex]

        lists = []
        stack = Stack()

        stack.push(vertex)

        while not stack.is_empty():
            temp = stack.pop()
            if temp in lists:
                pass
            else:
                lists.append(temp)
                children = self.get_neighbors(temp)
                if len(children) > 0:
                    for edge in children:
                        stack.push(edge.vertex_2)

        return lists

    def size(self):
        return len(self.adjacency_list)
