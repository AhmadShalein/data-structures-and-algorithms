class AnimalShelter():
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self, animal):
        if animal.kind == "cat"
          self.cat.enqueue(animal.nickname)
        elif animal.kind == "dog"
          self.dog.enqueue(animal.nickname)
      
    def dequeue(self, pref):
        if pref == "cat"
          self.cat.dequeue()
        elif pref == "dog"
          self.dog.dequeue()
        else:
          return "null"
        
class Cat():
  def __init__(self,nickname):
    self.nickname = nickname
    self.kind = "cat"
    
class Dog():
  def __init__(self,nickname):
    self.nickname = nickname
    self.kind = "dog"
