class Node:
  def __init__(self , data=None):
    self.data = data
    self.next = None

class Stack:
  def __init__(self,node=None):
    self.top = node
  
  def push(self, value):
    node = Node(value)
    node.next = self.top
    self.top = node

  def pop(self):
    if self.top is None:
      return None
    value = self.top.data
    self.top = self.top.next
    return value
  
  def peek(self):
    if not self.is_empty():
      return self.top.data
 
  def is_empty(self):
    return not self.top    
  
class Queue:
  def __init__(self):
    self.front = None
    self.rear = None

  def enqueue(self, value):
    node = Node(value)
    if self.rear is None:
        self.front = node
        self.rear = node
    else:
        self.rear.next = node
        self.rear = node

  def dequeue(self):
    if self.front is None:
      return None
    value = self.front.data
    self.front = self.front.next
    return value

  def is_empty(self):
    return not self.front

  def peek(self):
    if not self.is_empty():
      return self.front.data

if __name__ == "__main__":
  print('test stack')

  stack = Stack()

  print(stack.is_empty())

  stack.push(1)
  stack.push(2)
  stack.push(3)

  print(stack.peek())
  print(stack.pop())
  print(stack.peek())
  print(stack.pop())

  print(stack.is_empty())


  print('testing queue')

  q = Queue()

  print(q.is_empty())
  
  q.enqueue(4)
  q.enqueue(5)
  q.enqueue(6)

  print(q.peek())
  print(q.dequeue())
  print(q.peek())
  print(q.dequeue())

  print(q.is_empty())
