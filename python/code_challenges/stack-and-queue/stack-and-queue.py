class Node:
  def __init__(self , value=None):
    self.value = value
    self.next = None

class Stack:
  def __init__(self,node=None):
    self.top = node
  
  def push(self, value):
    node = Node(value)
    node.next = self.top
    self.top = node

  def pop(self):
    temp = self.top
    self.top = self.top.next
    temp.next = None
    return temp.value
  
  def peek(self):
    if not self.is_empty():
      return self.top.value
 
  def is_empty(self):
    return not self.top    
  
class Queue:
  def __init__(self):
    self.front = None
    self.rear = None

  def enqueue(self, value):
    node = Node(value)
    self.rear.next = node
    self.rear = self.rear.next

  def dequeue(self):
    temp = self.front
    self.front = temp.next
    front.next = None
    return temp.value

  def peek(self):
    if not self.is_empty():
      return self.front.value

  def is_empty(self):
    return not self.front


if __name__ == "__main__":
