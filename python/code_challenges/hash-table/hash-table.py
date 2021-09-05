class HashTable():
  def __init__(self ,size = 1024):
    """initialization hash table"""
    self.max = size #length of list
    self.arr = [[] for i in range(self.max)] 
    # or [None]*self.size\ we store key value pairs in each index [('Key',value),('Key',value)]

  def get_hash(self, key):
    """function to return the hash value using ASCII code"""
    h = 0
    for char in key:
        h += ord(char)
    hash_index= h % self.max 
    return hash_index
 
  def add(self ,key ,value):
    """Function the store key value pairs in the key index of list"""
    h = self.get_hash(key)
    found = False
    # we have to loop in the linked list to check if the key is found then update its value 
    for idx, element in enumerate(self.arr[h]):
      if len(element)==2 and element[0] == key:
          self.arr[h][idx] = (key,value)
          found = True
    if not found: # if not found store it 
      self.arr[h].append((key,value))

  def get(self, key):
    """function that return the value stored in the key index"""
    h = self.get_hash(key)
    for element in self.arr[h]:
      if element[0] == key:
        return element[1] # return the value

  def contains(self, key):
    h = self.get_hash(key)
    found = False
    # we have to loop in the linked list to check if the key is found then update its value 
    for idx, element in enumerate(self.arr[h]):
      if len(element)==2 and element[0] == key:
        found = True
    return found

  def delete(self , key):
    """function that set the value of key to None"""
    h = self.get_hash(key)
    for idx , element in enumerate(self.arr[h]):
      if element[0] == key:
        del self.arr[h][idx]
