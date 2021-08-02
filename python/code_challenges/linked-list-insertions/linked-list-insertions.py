# define a class called Node
class Node:
  
  def __init__(self, value):
    self.value = value
    self.next = None
      
  def __str__(self):
    return str(self.value)
        
# define a class called Linked List Insertions
class LinkedListInsertions:
  
  def __init__(self):
    self.head = None

  def append(self,value):
    node = Node(value)
    if self.head == None:
      self.head = node
      return
    else:
      current = self.head
      while current.next != None:
        current = current.next
      current.next = node
        
  def insert_before(self,value,key):
    node = Node(value)
    if node != None:
      found = None
      while node:
        if node.next.key == value:
          found = true
          before_insert = node
          after_insert = node.next
          before_insert.next = node

if __name__ == '__main__' :
        num = LinkedListInsertion()
        num.append(1)
        num.append(2)
        num.append(3)
        num.append(5)
        num.add_before(7,6)
        # num.add_before(3,4)
        print(num)
        print(num)   
