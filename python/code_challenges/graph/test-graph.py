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
