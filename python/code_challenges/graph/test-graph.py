import bytest
from graph.graph import *

def test_graph():
  graph = Graph()
  v1 = graph.add_node('A')
  v2 = graph.add_node('B')
  v3 = graph.add_node('C')
  v4 = graph.add_node('D')
  v5 = graph.add_node('E')
  graph.add_edge(v1,v2,1)
  graph.add_edge(v1,v3,2)
  graph.add_edge(v2,v4,4)
  graph.add_edge(v3,v4,8)
  graph.add_edge(v3,v5,3)
  graph.add_edge(v4,v5,5)
  assert graph.size() == 5
  assert graph.get_nodes() == dict_keys(['A', 'B', 'C', 'D', 'E'])
  assert graph.neighbors(v1) == [('B', 1), ('C', 2)]
  assert graph.neighbors(v2) == [('D', 4)]
  assert graph.neighbors(v3) == [('D', 8), ('E', 3)]
  assert graph.neighbors(v4) == [('E', 5)]
  assert graph.neighbors(v5) == []
  assert graph.print_graph() == {'A': [('B', 1), ('C', 2)], 'B': [('D', 4)], 'C': [('D', 8), ('E', 3)], 'D': [('E', 5)], 'E': []}
    
def test_breath_first_search():
  graph = Graph()
  v1 = graph.add_node('A')
  v2 = graph.add_node('B')
  v3 = graph.add_node('C')
  v4 = graph.add_node('D')
  v5 = graph.add_node('E')
  graph.add_edge(v1,v2,1)
  graph.add_edge(v1,v3,2)
  graph.add_edge(v2,v4,4)
  graph.add_edge(v3,v4,8)
  graph.add_edge(v3,v5,3)
  graph.add_edge(v4,v5,5)
  graph.add_edge(v2,v1,10)
  assert graph.breath_first_search(v1) == ['A', 'B', 'C', 'D', 'E']
  assert graph.breath_first_search(v2) == ['B', 'D', 'A', 'E', 'C']
  assert graph.breath_first_search(v3) == ['C', 'D', 'E', 'A', 'B']
  assert graph.breath_first_search(v4) == ['D', 'E', 'C', 'A', 'B']
  assert graph.breath_first_search(v5) == ['E', 'C', 'D', 'A', 'B']
    
def test_business_trip():
  graph = Graph()
  v1 = graph.add_node('Pandora')
  v2 = graph.add_node('Arendelle')
  v3 = graph.add_node('Metroville')
  v4 = graph.add_node('Monstropolis')
  v5 = graph.add_node('Narnia')
  v6 = graph.add_node('Naboo')
  graph.add_edge(v1,v2,150)
  graph.add_edge(v1,v3,82)
  graph.add_edge(v2,v3,99)
  graph.add_edge(v2,v4,42)
  graph.add_edge(v3,v4,105)
  graph.add_edge(v3,v5,37)
  graph.add_edge(v3,v6,26)
  graph.add_edge(v4,v6,73)
  graph.add_edge(v5,v6,250)
  cities_one_two_three = [v1,v2,v3]
  assert graph.business_trip(cities) == (True, '$249')

def test_graph_depth_first():
  graph = Graph()
  v1 = graph.add_node('a')
  v2 = graph.add_node('b')
  v3 = graph.add_node('c')
  v4 = graph.add_node('d')
  v5 = graph.add_node('e')
  v6 = graph.add_node('f')
  v7 = graph.add_node('g')
  v8 = graph.add_node('h')
  graph.add_edge(v1, v2)
  graph.add_edge(v1, v4)
  graph.add_edge(v2,v1)
  graph.add_edge(v2,v3)
  graph.add_edge(v2,v4)
  graph.add_edge(v3,v2)
  graph.add_edge(v3,v7)
  graph.add_edge(v4,v1)
  graph.add_edge(v4,v2)
  graph.add_edge(v4,v5)
  graph.add_edge(v4,v8)
  graph.add_edge(v4,v6)
  graph.add_edge(v6,v4)
  graph.add_edge(v6,v8)
  graph.add_edge(v8,v6)
  graph.add_edge(v8,v4)
  graph.add_edge(v5,v4)
  assert graph.graph_depth_first(v1) == ['a', 'b', 'c', 'g', 'd', 'e', 'h', 'f']
