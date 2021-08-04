class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
  
    def __str__(self):
        result= ''
        current = self.head
        while current:
            result += f'{{{current.value}}}->'
            current = current.next
            if current == None:
                result += 'NULL'
        
        return result
    
    def __len__(self):
      counter = 0
      current = self.head

      while current:
        counter += 1
        current = current.next

      return counter

def zip_lists(list1,list2):
    if not list1:
        return list2
    elif not list2:
        return list1
    list = LinkedList()
    current1=list1.head
    current2=list2.head
    while current1 or current2:
        if current1:
            list.insert(current1.value)
            current1=current1.next
        if current2:
            list.insert(current2.value)
            current2=current2.next
    return list
 
if __name__=='__main__':
    list1=LinkedList()
    list2=LinkedList()
    list1.insert(1)
    list1.insert(3)
    list1.insert(5)
    list1.insert(7)
    list2.insert(2)
    list2.insert(4)
    list2.insert(6)
    outcome=zip_lists(list1,list2)
    print(outcome)
