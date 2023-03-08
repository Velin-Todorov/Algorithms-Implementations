#!/usr/bin/python3

"""
This is implementation of QuickSort using Hoare Partitioning Scheme
"""


def partition(arr, low, high):
    
    i = low 
    j = high
    
    pivot = arr[(low + high) // 2]

    while True:
       
        while arr[i] < pivot:
            i += 1
        
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quickSort(arr, low, high):
    
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot)
        quickSort(arr, pivot + 1, high)


array = [10, 11, 12, 14, 15, 20, 19, 30, 1, 2, 7]
l = 0
h = len(array) - 1

quickSort(array, l, h)

print(array)
