#Lab 35
from collections import deque

class Vertex():
  def __init__(self,key):
    self.key = key
  
  def __str__(self):
    return str(self.key)

class Queue():
  def __init__(self):
    self.dq = deque()
  
  def enqueue(self,value):
    self.dq.appendleft(value)

  def dequeue(self):
    return self.dq.pop()
  
  def __len__ (self):
    return len(self.dq)

class Graph():
  def __init__(self):
    self._adjacency_list = {}
    
  def add_node(self,value):
    new_v = Vertex(value)
#     new_v = str(new_v)
    self._adjacency_list[new_v] = []
    return new_v
    
  def add_edge(self,start_vertex,end_vertex,weight =0):
    if start_vertex not in self._adjacency_list:
      raise KeyError('Start vertex is not found in the graph')
    if end_vertex not in self._adjacency_list:
      raise KeyError('end vertex is not found in the graph') 
    self._adjacency_list[start_vertex].append((str(end_vertex),weight))  

  def get_nodes(self):
    return self._adjacency_list.keys()
    
  def neighbors(self,vertex):
    return self._adjacency_list[vertex]
  
  def size(self):
    return len(self._adjacency_list)

#Lab 36
  def breath_first_search(self,start_vertex):
    output=[]
    queue = Queue()
    visited = set()
    queue.enqueue(start_vertex)
    visited.add(start_vertex)
    while len(queue):
      current_vertex = queue.dequeue()
      output.append(current_vertex)
      for i in self._adjacency_list[current_vertex]:
        if i[0] not in visited:
          i=i[0]
          visited.add(i)
          queue.enqueue(i)
    return output

#Lab 37
  def business_trip(self,cities:list):
    sum = 0
    flag = False
    for i in range(len(cities)-1):
        neighbors = self._adjacency_list[cities[i]]
        print(neighbors)
        for neighbor in neighbors:
          if cities[i+1] == neighbor[0]:
            sum += neighbor[1]
            flag = True
            break
          else:
            sum += 0
            flag = False
    if not flag:
      return False,'$0'     
    return True,'$'+ str(sum)
    
#Lab 38
  def graph_depth_first(self,node):
    visited = set()
    visited.add(node)
    depth_first_list = []
    def __DFS(node,visited,depth_first_list):
        visited.add(node)
        depth_first_list.append(node.value)
        neighbors = self.neighbors(node)
        if neighbors != 'Empty':
            for i in neighbors:
                if i.vertix not in visited :
                    __DFS(i.vertix,visited,depth_first_list)
    __DFS(node,visited,depth_first_list)
    return depth_first_list 

  def print_graph(self):
    print(self._adjacency_list)
