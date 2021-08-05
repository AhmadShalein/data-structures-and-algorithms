class Node:
  def __init__(self , value=None):
    self.value= value
    self.next=None

class Stack:
  def __init__(self,node=None):
    self.top=node
  
  def push(self, value):
    node= Node(value)
    node.next = self.top
    self.top = node

  def pop(self):
    temp=self.top
    self.top=self.top.next
    temp.next=None
    return temp.value
  
  def peek(self):
    if not self.isEmpty():
      return self.top.data
    raise EmptyStackException("stack is empty")
 
  def is_empty(self):
    return not self.top    
    
class Queue:
  def __init__(self):
    self.front = None
    self.rear = None

  def enqueue(self, value):
    pass

  def dequeue(self):
    pass

  def is_empty(self):
    if (not self.rear and self.front) or (self.rear and not self.front):
      raise Exception("Something is fishy here")
    return not self.rear
