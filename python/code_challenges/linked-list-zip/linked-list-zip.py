def zip_lists(list1,list2):
    
    if not list1:
        return list2
    elif not list2:
        return list1
    
    list = LinkedList()
    current_one=list1.head
    current_two=list2.head
    
    while current1 or current2:
        if current1:
            list.append(current1.value)
            current1=current1.next
        if current2:
            list.append(current2.value)
            current2=current2.next
    return list
 
if __name__=='__main__':
  
    list1=LinkedList()
    list2=LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)
    list1.append(7)
    list2.append(2)
    list2.append(4)
    list2.append(6)
    outcome=zip_lists(list1,list2)
    print(outcome)
