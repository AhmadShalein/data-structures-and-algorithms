class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return " ".join(items)
    
    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next
    
    def dequeue(self):
        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
        
    def is_empty(self):
        if self.front:
            return False
        return True

class AnimalShelter():
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self, animal):
        if animal.kind == "cat":
          self.cat.enqueue(animal.nickname)
        elif animal.kind == "dog":
          self.dog.enqueue(animal.nickname)
      
    def dequeue(self, pref):
        if pref == "cat":
          self.cat.dequeue()
        elif pref == "dog":
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

    
if __name__ == "__main__":
    animal_shelter = AnimalShelter()
    dog_one = Dog("MILO")
    dog_two = Dog("MAX")
    dog_three = Dog("KOBE")
    animal_shelter.enqueue(dog_one)
    animal_shelter.enqueue(dog_two)
    animal_shelter.enqueue(dog_three)
    print(animal_shelter.dog)
    animal_shelter.dequeue("dog")
    print(animal_shelter.dog)
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return " ".join(items)
    
    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next
    
    def dequeue(self):
        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
        
    def is_empty(self):
        if self.front:
            return False
        return True

class AnimalShelter():
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self, animal):
        if animal.kind == "cat":
          self.cat.enqueue(animal.nickname)
        elif animal.kind == "dog":
          self.dog.enqueue(animal.nickname)
      
    def dequeue(self, pref):
        if pref == "cat":
          self.cat.dequeue()
        elif pref == "dog":
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

    
if __name__ == "__main__":
    animal_shelter = AnimalShelter()
    dog_one = Dog("MILO")
    dog_two = Dog("MAX")
    dog_three = Dog("KOBE")
    animal_shelter.enqueue(dog_one)
    animal_shelter.enqueue(dog_two)
    animal_shelter.enqueue(dog_three)
    print(animal_shelter.dog)
    animal_shelter.dequeue("dog")
    print(animal_shelter.dog)
    print("-----------------")
    cat_one = Cat("Oliver")
    cat_two = Cat("Leo")
    cat_three = Cat("Loki")
    animal_shelter.enqueue(cat_one)
    animal_shelter.enqueue(cat_two)
    animal_shelter.enqueue(cat_three)
    print(animal_shelter.cat)
    animal_shelter.dequeue("cat")
    print(animal_shelter.cat)
    cat_one = Cat("Oliver")
    cat_two = Cat("Leo")
    cat_three = Cat("Loki")
    animal_shelter.enqueue(cat_one)
    animal_shelter.enqueue(cat_two)
    animal_shelter.enqueue(cat_three)
    print(animal_shelter.cat)
    animal_shelter.dequeue("cat")
    print(animal_shelter.cat)
