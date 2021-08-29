def insertion_sort(arr):
    for i in range (1, len(arr)):
        j = i-1
        key = list [i]
        while j >= 0 and key < arr[j]:
            list[j+1] = arr[j]
            j -= 1
        arr[j+1] = key   
    return arr
