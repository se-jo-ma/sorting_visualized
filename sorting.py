def bubbleSort(array):
    def swap(i,j):
        array[i],array[j] = array[j],array[i]

    length = len(array)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x+1
        for i in range(1, length-x):
            if array[i-1] > array[i]:
                swap(i-1,i)
                swapped = True
        yield array

def heapify(array, length, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < length and array[i] < array[left]:
        largest = left
    if right < length and array[largest] < array[right]:
        largest = right

    if largest != i:
        array[i],array[largest] = array[largest],array[i]
        heapify(array, length, largest)

def heapSort(array):
    length = len(array)

    for i in range(length, -1, -1):
        heapify(array, length, i)
        yield array

    for i in range(length-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
        yield array

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >=0 and key < array[j] :
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
        return array


def partition(array,low,high):
    i = low-1
    pivot = array[high]

    for j in range(low,high):
        if array[j] <= pivot:
            i += 1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[high] = array[high], array[i+1]
    return i+1

def quick_sort(array, low, high):
    if low >= high:
        return
    pi = partition(array,low,high)

    yield array
    yield from quick_sort(array, low, pi-1)
    yield from quick_sort(array,pi+1, high)

def selection_sort(array):
    for i in range(len(array)):
        min = i

        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j
        array[min], array[i] = array[i], array[min]
        yield array

def shell_sort(array):
    length = len(array)
    mid = length // 2

    while mid > 0:
        for i in range(mid, length):
            temp = array[i]
            j = i
            while j >= mid and array[j-mid] > temp:
                array[j] = array[j-mid]
                j -= mid
            array[j] = temp
            yield array
        mid //= 2
