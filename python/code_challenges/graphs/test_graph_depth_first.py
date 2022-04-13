from graph_depth_first_search import Graph


def test_depth_first_is_empty():
    graph = Graph()
    actual = str(graph.depth_first(None))
    expected = f'[None]'
    assert actual == expected

def test_depth_first_one():
    graph = Graph()

    v_1 = graph.add_node('A')
    v_2 = graph.add_node('B')
    v_3 = graph.add_node('C')

    graph.add_edge(v_1, v_2, 4)
    graph.add_edge(v_2, v_3, 5)
    graph.add_edge(v_3, v_1, 7)

    actual = str(graph.depth_first(v_1))
    expected = f'[Vertex(A), Vertex(B), Vertex(C)]'
    assert actual == expected

def test_depth_first_two():
    graph = Graph()
    v_1 = graph.add_node('A')
    v_2 = graph.add_node('B')
    v_3 = graph.add_node('C')
    v_4 = graph.add_node('D')
    v_5 = graph.add_node('E')
    v_6 = graph.add_node('F')
    v_7 = graph.add_node('G')
    v_8 = graph.add_node('H')

    graph.add_edge(v_1,v_4, 10)
    graph.add_edge(v_1, v_2, 4)
    graph.add_edge(v_2, v_4, 18)
    graph.add_edge(v_2, v_3, 200)
    graph.add_edge(v_3, v_7, 50)
    graph.add_edge(v_4, v_6, 46)
    graph.add_edge(v_4, v_8, 72)
    graph.add_edge(v_4, v_5, 87)
    graph.add_edge(v_6, v_8, 90)

    actual = str(graph.depth_first(v_1))
    expected = f'[Vertex(A), Vertex(B), Vertex(C), Vertex(G), Vertex(D), Vertex(E), Vertex(H), Vertex(F)]'
    assert actual == expected

def test_depth_first_three():
    graph = Graph()
    v_1 = graph.add_node('A')
    v_2 = graph.add_node('B')
    v_3 = graph.add_node('C')

    actual = str(graph.depth_first(v_1))
    expected = f'[Vertex(A)]'
    assert actual == expected
