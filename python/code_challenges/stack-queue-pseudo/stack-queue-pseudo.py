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

class PseudoQueue:
  def __init__(self):
    self.stack_1 = Stack()
    self.stack_2 = Stack()

  def enqueue(self, value):
    self.stack_1.push(value)

  def dequeue(self):
    if self.stack_2.is_empty():
        if self.stack_1.is_empty():
            raise IndexError("Can't dequeue from empty queue!")
      
        while not self.stack_1.is_empty():
            last_stack_1_item = self.stack_1.pop()
            self.stack_2.push(last_stack_1_item) 

    return self.stack_2.pop()

if __name__ =="__main__":
    q = PseudoQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(4)
    print(q.dequeue())
