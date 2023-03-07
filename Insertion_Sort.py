#!/usr/bin/python3

def InsertionSort(arr, low, high):

    
    for i in range(1, high):
        l = i - 1
        key = arr[i]

        while l >= 0 and arr[l] > key:
            arr[l + 1] = arr[l]
            l -= 1

        arr[l + 1] = key


arr = [1, 3, 4, 6, 7, 8, 9]

InsertionSort(arr, 0, len(arr) - 1)

print(arr)



