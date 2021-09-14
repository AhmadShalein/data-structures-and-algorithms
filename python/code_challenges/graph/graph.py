class Vertex():
  def __init__(self,key):
    self.key = key
  
  def __str__(self):
    return str(self.key)

class Queue():
  def __init__(self):
    self.dq =deque()
  
  def enqueue(self,value):
    self.dq.appendleft(value)

  def dequeue(self):
    return self.dq.pop()
  
  def __len__ (self):
    return len(self.dq)

class Graph():
  def __init__(self):
    self._adjacency_list = {}
    

  def add_node(self ,value):
    new_v = Vertex(value)
    new_v=str(new_v)
    self._adjacency_list[new_v] = []
    return new_v
    

  def add_edge(self , start_vertex ,end_vertex ,weight =0):
    if start_vertex not in self._adjacency_list:
      raise KeyError('Start vertex is not found in the graph')
    if end_vertex not in self._adjacency_list:
      raise KeyError('end vertex is not found in the graph') 
    self._adjacency_list[start_vertex].append((str(end_vertex),weight))  

  def get_nodes(self):
    return self._adjacency_list.keys()
    
  
  def neighbors(self , vertex):
    return self._adjacency_list[vertex]
  
  def size(self):
    return len(self._adjacency_list)
   
  def print_graph(self):
    print(self._adjacency_list)
