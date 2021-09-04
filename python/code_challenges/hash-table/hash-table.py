class Node():
  def __init__(self, value=None):
    self.value = value
    self.next = None

  def __add__(self, other):
    return Node(self.value + other.value)

  def __str__(self):
    return str(self.value)


class LinkedList():
  def __init__(self):
    self.head = None

  def insert(self, value):
    node = Node(value)
    if self.head:
      node.next = self.head
    self.head = node

  def includes(self,vlaue):
     current=self.head
     while current:
         if vlaue ==current.value[0]:
            return True
         current=current.next
     return False

  def append(self,value):
    new_node=Node(value)
    if self.head == None:
      self.head = new_node
    else:
      current=self.head
      while current.next:
        current=current.next
      current.next=new_node

class HashTable:

  def __init__(self, size = 1024):
    
    self.size = size
    self._buckets = [None] *self.size

  def hash(self,key:str)->int:
    value=0
    for x in key:
      value += ord(x)
    index = (value * 7) % self.size   
    return index

  def add(self,key,value):

    index = self.hash(key) 

    if not self._buckets[index]:
      self._buckets[index] = LinkedList()
    self._buckets[index].append([key,value])

  def find(self,key):
    index = self.hash[key]
    return index
    

  def contains(self,key):
    index=self.hash(key)
    if self._buckets[index]:
      return self._buckets[index].includes(key)
    else:
      return False
