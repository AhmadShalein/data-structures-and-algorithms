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

  def insert(self,value):
    node = Node(value)
    if self.head:
      node.next = self.head
    self.head = node
      
  def includes(self,value):
    current = self.head
    value_exists = False
      
    while current is False:
      if current.data == value:
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
         
        
if __name__ == "__main__":
  ll = LinkedList()
  ll.insert("Ahmad")
  ll.insert("Dario")
  print(ll)
  print(ll.includes("Ahmad"))
  print(ll.includes("Dario"))