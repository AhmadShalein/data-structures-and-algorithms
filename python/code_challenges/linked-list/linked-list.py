# define a class called Node
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
      
  def __add__(self, other):
    return Node(self.value + other.value)

  def __str__(self):
    return str(self.value)
        
# define a class called Linked List
class LinkedList:
  def __init__(self):
    self.head = None

  # Lab 5

  def insert(self,value):
    node = Node(value)
    if self.head:
      node.next = self.head
    self.head = node
      
  def includes(self,value):
    current = self.head
    value_exists = False
      
    while current is False:
      if current.value == value:
        value_exists = True
      else:
        current = current.next
      return value_exists
    
  def __str__(self):
    string = ""
    current = self.head
      
    while current:
      value = current.value
      if current.next is None:
        string +=f"( {value} ) -> NULL"
        break
        string += f"( {value} ) -> "
        current = current.next
      return string
 
  # Lab 6 
            
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
        
  def insertBefore(self,value,key):
    node = Node(value)
    prev = self.head
    current = self.head
    found = False
    while current:
        if current.value == key:
            prev.next = node
            node.next = current
            found = True
            break
        prev = current
        current = current.next
    if not found:
        raise Exception("key not found")
        
  def insertAfter(self,value,key):
    node = Node(value)
    current = self.head
    found = False
    while current:
        if current.value == key:
            node.next = current.next
            current.next = node
            found = True
            break
        current = current.next
    if not found:
        raise Exception("key not found")
          
if __name__ == "__main__":
  ll = LinkedList()
  
  # Lab 5

  ll.insert("Ahmad")
  ll.insert("Dario")
  print(ll)
  print(ll.includes("Ahmad"))
  print(ll.includes("Dario"))
    
  # Lab 6
  
  ll.append("A")
  ll.append("B")
  assert ll.head.value == "A"
  assert ll.head.next.value == "B"
  assert ll.head.next.next == None
  print(ll)
