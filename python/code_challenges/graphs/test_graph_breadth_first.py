from graph_breadth_first import Graph, Vertex, Edge
import pytest

@pytest.mark.skip(reason="pending")
def test_graph_breadth_first():
    graph = Graph()
    # test add_node method
    graph.add_node('apple')
    graph.add_node('pear')
    graph.add_node('orange')


    # test add_edge method
    node_1 = graph.nodes[0]
    node_2 = graph.nodes[1]
    node_3 = graph.nodes[2]

    graph.add_edge(node_1, node_2, 3)
    graph.add_edge(node_1, node_3, 4)
    graph.add_edge(node_2, node_3, 5)

    expected = graph.breadth_first(node_1)[0]
    actual = node_1
    assert actual == expected

    expected = graph.breadth_first(node_1)[1]
    actual = node_2
    assert actual == expected

    expected = graph.breadth_first(node_1)[2]
    actual = node_3
    assert actual == expected
    # assert graph.breadth_first(a)[0] == a
    # assert graph.breadth_first(a)[1] == b
    # assert graph.breadth_first(a)[2] == c
    # assert graph.breadth_first(b)[0] == b
    # assert graph.breadth_first(b)[1] == a
    # assert graph.breadth_first(b)[2] == c
    # assert graph.breadth_first(c)[0] == c
    # assert graph.breadth_first(c)[1] == a
    # assert graph.breadth_first(c)[2] == b
@pytest.mark.skip(reason="pending")
def test_graph_breadth_first_two():
    graph = Graph()
    # test add_node method
    graph.add_node('Pandora')
    graph.add_node('Arendelle')
    graph.add_node('Metroville')
    graph.add_node('Narnia')


    # test add_edge method
    node_1 = graph.nodes[0]
    node_2 = graph.nodes[1]
    node_3 = graph.nodes[2]
    node_4 = graph.nodes[3]

    graph.add_edge(node_1, node_2, 6)
    graph.add_edge(node_1, node_3, 10)
    graph.add_edge(node_2, node_3, 5)
    graph.add_edge(node_2, node_4, 16)
    graph.add_edge(node_3, node_4, 17)

    expected = graph.breadth_first(node_1)[0]
    actual = node_1
    assert actual == expected

    expected = graph.breadth_first(node_1)[1]
    actual = node_2
    assert actual == expected

    expected = graph.breadth_first(node_1)[2]
    actual = node_3
    assert actual == expected

    expected = graph.breadth_first(node_2)[0]
    actual = node_2
    assert actual == expected

    expected = graph.breadth_first(node_2)[1]
    actual = node_1
    assert actual == expected

    expected = graph.breadth_first(node_2)[2]
    actual = node_3
    assert actual == expected

    expected = graph.breadth_first(node_2)[3]
    actual = node_4
    assert actual == expected

    expected = graph.breadth_first(node_3)[0]
    actual = node_3
    assert actual == expected

    expected = graph.breadth_first(node_3)[1]
    actual = node_1
    assert actual == expected

    expected = graph.breadth_first(node_3)[2]
    actual = node_2
    assert actual == expected

@pytest.mark.skip(reason="pending")
def test_breadth_first_is_empty():
    graph = Graph()
    actual = graph.breadth_first()
    expected = []
    assert actual == expected
