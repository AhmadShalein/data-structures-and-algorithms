def test_zip_lists():
    list1=LinkedList()
    list2=LinkedList()
    list1.insert(1)
    list1.insert(3)
    list1.insert(5)
    list1.insert(7)
    list2.insert(2)
    list2.insert(4)
    list2.insert(6)
    assert zip_lists(list1,list2) == '{1}->{2}->{3}->{4}->{5}->{6}->{7}->NULL'
