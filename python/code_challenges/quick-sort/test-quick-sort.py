from quick-sort.quick-sort import quick-sort

def test-quick-sort():
    assert quick_sort([8,4,23,42,16,15],0,5) == [8,15,4,23,16,42]
    #Reverse-sorted
    assert quick_sort([20,18,12,8,5,-2],0,5) == [-2,18,20,8,12,5]
    #Few uniques
    assert quick_sort([5,12,7,5,5,7],0,5) == [5,7,7,12,5,5]
    #Nearly-sorted
    assert quick_sort([2,3,5,7,13,11],0,5) == [2,11,3,5,7,13]
