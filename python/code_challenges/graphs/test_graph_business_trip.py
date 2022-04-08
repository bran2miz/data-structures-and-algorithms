from graph_business_trip import graph_business_trip
from graph_breadth_first import Graph

def test_business_trip():
    graph = Graph()
    pd = graph.add_node('Pandora')
    met = graph.add_node('MetroVille')
    narnia = graph.add_node('Narnia')
    arendelle = graph.add_node('Arendelle')
    naboo = graph.add_node('Naboo')
# 82 +37 + 136 = 119 + 136 =255
    graph.add_edge(pd, met, 82)
    graph.add_edge(met, pd, 82)
    graph.add_edge(met, narnia, 37)
    graph.add_edge(narnia, met, 37)
    graph.add_edge(narnia, arendelle, 136)
    graph.add_edge(arendelle, narnia, 136)
    graph.add_edge(arendelle, naboo, 115)
    graph.add_edge(naboo, arendelle, 115)

    arr = ['Pandora', 'MetroVille','Narnia', 'Arendelle']
    actual = graph_business_trip(graph, arr)
    expected = [True, '$255']
    assert actual == expected

def test_business_trip_false():
    graph = Graph()
    pd = graph.add_node('Pandora')
    met = graph.add_node('MetroVille')
    narnia = graph.add_node('Narnia')
    arendelle = graph.add_node('Arendelle')
    naboo = graph.add_node('Naboo')
# 82 +37 + 136 = 119 + 136 =255
    graph.add_edge(pd, met, 82)
    graph.add_edge(met, pd, 82)
    graph.add_edge(met, narnia, 37)
    graph.add_edge(narnia, met, 37)
    graph.add_edge(narnia, arendelle, 136)
    graph.add_edge(arendelle, narnia, 136)
    graph.add_edge(arendelle, naboo, 115)
    graph.add_edge(naboo, arendelle, 115)

    arr = ['Pandora', 'MetroVille','Narnia', 'Taboo']
    actual = graph_business_trip(graph, arr)
    expected = [False, '$0']
    assert actual == expected

def test_business_trip_empty_arr():
    graph = Graph()
    pd = graph.add_node('Pandora')
    met = graph.add_node('MetroVille')
    narnia = graph.add_node('Narnia')
    arendelle = graph.add_node('Arendelle')
    naboo = graph.add_node('Naboo')
# 82 +37 + 136 = 119 + 136 =255
    graph.add_edge(pd, met, 82)
    graph.add_edge(met, pd, 82)
    graph.add_edge(met, narnia, 37)
    graph.add_edge(narnia, met, 37)
    graph.add_edge(narnia, arendelle, 136)
    graph.add_edge(arendelle, narnia, 136)
    graph.add_edge(arendelle, naboo, 115)
    graph.add_edge(naboo, arendelle, 115)

    arr = []
    actual = graph_business_trip(graph, arr)
    expected = [False, '$0']
    assert actual == expected

def test_empty_graph():
    graph = Graph()
    pd = graph.add_node('Pandora')

    arr = ['Pandora', 'MetroVille','Narnia', 'Taboo']
    actual = graph_business_trip(graph, arr)
    expected = [False, '$0']
    assert actual == expected

def test_graph_business_round_trip():
    graph = Graph()
    pd = graph.add_node('Pandora')
    met = graph.add_node('MetroVille')
    narnia = graph.add_node('Narnia')
    arendelle = graph.add_node('Arendelle')
    naboo = graph.add_node('Naboo')
# 82 +37 + 136 = 119 + 136 =255
    graph.add_edge(pd, met, 82)
    graph.add_edge(met, pd, 82)
    graph.add_edge(met, narnia, 37)
    graph.add_edge(narnia, met, 37)
    graph.add_edge(narnia, arendelle, 136)
    graph.add_edge(arendelle, narnia, 136)
    graph.add_edge(arendelle, naboo, 115)
    graph.add_edge(naboo, arendelle, 115)

    arr = ['Pandora', 'MetroVille','Narnia', 'Arendelle', 'Naboo',  'Arendelle', 'Narnia', 'MetroVille', 'Pandora']

    actual = graph_business_trip(graph, arr)
    expected = [True, '$740']
    assert actual == expected
