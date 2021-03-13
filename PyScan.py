import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Helper Functions
def merge(numberList, start, mid, end):
    """Helper function for merge sort."""
    
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if numberList[leftIdx] < numberList[rightIdx]:
            merged.append(numberList[leftIdx])
            leftIdx += 1
        else:
            merged.append(numberList[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(numberList[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(numberList[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        numberList[start + i] = sorted_val
        yield numberList

def swap(numberList, i, j):
    if i != j:
        numberList[i], numberList[j] = numberList[j], numberList[i]

#Sorting Algorithms

def insertionsort(numberList):
    
    for i in range(1, len(numberList)):
        j = i
        while j > 0 and numberList[j] < numberList[j - 1]:
            swap(numberList, j, j - 1)
            j -= 1
            yield numberList
def bubblesort(numberList):

    if len(numberList) == 1:
        return

    swapped = True
    for i in range(len(numberList) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(numberList) - 1 - i):
            if numberList[j] > numberList[j + 1]:
                swap(numberList, j, j + 1)
                swapped = True
            yield numberList



def mergesort(numberList, start, end):
    
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort(numberList, start, mid)
    yield from mergesort(numberList, mid + 1, end)
    yield from merge(numberList, start, mid, end)
    yield numberList

def selectionsort(numberList):
  
    if len(numberList) == 1:
        return

    for i in range(len(numberList)):
        
        minVal = numberList[i]
        minIdx = i
        for j in range(i, len(numberList)):
            if numberList[j] < minVal:
                minVal = numberList[j]
                minIdx = j
            yield numberList
        swap(numberList, i, minIdx)
        yield numberList

def quicksort(numberList, start, end):
    
    if start >= end:
        return

    pivot = numberList[end]
    pivotIdx = start

    for i in range(start, end):
        if numberList[i] < pivot:
            swap(numberList, i, pivotIdx)
            pivotIdx += 1
        yield numberList
    swap(numberList, end, pivotIdx)
    yield numberList

    yield from quicksort(numberList, start, pivotIdx - 1)
    yield from quicksort(numberList, pivotIdx + 1, end)



