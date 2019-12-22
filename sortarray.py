#!/usr/bin/python3
def sortarray(array):
    l = len(array)
    arr = list(array)
    maxi = arr[0]
    for i in range(l):
        if arr[i] > maxi:
            maxi = arr[i]
    for j in range(l):
        mini = maxi
        for i in range(l):
            if arr[i] is not None and mini > arr[i]:
                mini = arr[i]
                k = i
        arr[k] = None
        array[j] = mini
    return array
import array as arr
a = arr.array('i', [8, 50, 0, -11, 74, 2, 33, 9, 120])
print(sortarray(a))
