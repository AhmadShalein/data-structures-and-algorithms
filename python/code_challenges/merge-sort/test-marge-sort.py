from merge-sort.merge-sort import mergesort

def test-merge-sort():
    assert mergesort([8,4,23,42,16,15]) == [4,8,15,16,23,42]
    #Reverse-sorted
    assert mergesort([20,18,12,8,5,-2]) == [-2,5,8,12,18,20]
    #Few uniques
    assert mergesort([5,12,7,5,5,7]) == [5,5,5,7,7,12]
    #Nearly-sorted
    assert mergesort([2,3,5,7,13,11]) == [2, 3, 5, 7, 11, 13]
