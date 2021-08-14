def test-stack-queue-animal-shelter-dog:
  animal_shelter = AnimalShelter()
  dog_one = Dog("MILO")
  dog_two = Dog("MAX")
  dog_three = Dog("KOBE")
  animal_shelter.enqueue(dog_one)
  animal_shelter.enqueue(dog_two)
  animal_shelter.enqueue(dog_three)
  assert animal_shelter.dog == MILO MAX KOBE
  animal_shelter.dequeue("dog")
  assert animal_shelter.dog == MAX KOBE

def test-stack-queue-animal-shelter-cat:
  animal_shelter = AnimalShelter()
  cat_one = Cat("Oliver")
  cat_two = Cat("Leo")
  cat_three = Cat("Loki")
  animal_shelter.enqueue(cat_one)
  animal_shelter.enqueue(cat_two)
  animal_shelter.enqueue(cat_three)
  assert animal_shelter.cat == Oliver Leo Loki
  animal_shelter.dequeue("cat")
  assert animal_shelter.cat == Leo Loki
