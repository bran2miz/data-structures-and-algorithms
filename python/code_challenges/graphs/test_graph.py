from graph import Graph, Vertex, Edge
import pytest


# Node can be successfully added to the graph
def test_add_vertex():
    graph = Graph()
    add_vertex = graph.add_node('a')
    expected = 'a'
    actual = add_vertex.value
    assert actual == expected

# The proper size is returned, representing the number of nodes in the graph
def test_graph_size():
    graph= Graph()
    graph.add_node('a')
    graph.add_node('b')
    expected = 2
    actual = graph.size()
    assert actual == expected

# An empty graph properly returns null
def test_get_node_graph_is_empty():
    graph = Graph()
    expected = []
    actual = graph.get_node()
    assert actual == expected

# An edge can be successfully added to the graph
def test_add_edge():
    graph = Graph()
    vertex_1 = graph.add_node('a')
    vertex_2 = graph.add_node('b')
    graph.add_edge(vertex_1 ,vertex_2, 4)
    assert True

# A collection of all nodes can be properly retrieved from the graph
# @pytest.mark.skip('pending')
def test_get_all_nodes():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    expected = 3
    actual = len(graph.get_node())
    assert actual == expected

# All appropriate neighbors can be retrieved from the graph
# @pytest.mark.skip('pending')
def test_all_neighbors():
    graph = Graph()
    vertex_1 = graph.add_node('a')
    vertex_2 = graph.add_node('b')
    graph.add_edge(vertex_1, vertex_2, 4)
    neighbors = graph.get_neighbor(vertex_1)
    assert len(neighbors) == 1
    edge = neighbors[0]
    assert edge.weight == 4
    assert edge.vertex == vertex_2

# A graph with only one node and edge can be properly returned

def test_one_node_one_edge():
    graph = Graph()
    vertex_1 = graph.add_node('a')
    graph.add_edge(vertex_1, vertex_1, 30)
    neighbors = graph.get_neighbor(vertex_1)
    assert len(neighbors) == 1
    edge = neighbors[0]
    assert edge.weight == 30
    assert edge.vertex == vertex_1


# Neighbors are returned with the weight between nodes included

# @pytest.mark.skip('pending')
def test_neighbors_weight():
    graph = Graph()
    vertex_1 = graph.add_node('a')
    vertex_2 = graph.add_node('b')
    graph.add_edge(vertex_1, vertex_2, 4)
    neighbors = graph.get_neighbor(vertex_1)
    assert len(neighbors) == 1
    neighbor_values = neighbors[0]
    assert neighbor_values.vertex.value == 'b'
    assert neighbor_values.weight == 4

def test_graph_breadth_first():
    g = Graph()
    v1=g.add_node('a')
    v2=g.add_node('b')
    v3=g.add_node('c')
    v4=g.add_node('d')
    v5=g.add_node('e')

    g.add_edge(v1,v2)
    g.add_edge(v2,v4)
    g.add_edge(v4,v5)
    g.add_edge(v1,v5)
    g.add_edge(v1,v3)
    g.add_edge(v3,v5)

    expected = g.breadth_first(v1)
    actual = ['a', 'b', 'd', 'e', 'c']
    assert actual == expected
