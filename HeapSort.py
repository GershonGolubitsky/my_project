from MinHeap import MinHeap

 # array = [5, 7, 6, 2, 3]


def heap_sort(array):
    # Run in array and extracts a minimal number
    heap = MinHeap(array[:])
    for i in range(len(array)):
        array[i] = heap.extract_minimum()
    return array
# a = [9, 8, -23, 5, 1, 0, 5, 4, 333, 298]
# heap_sort(a)
# print(a)
# print(MinHeap(a))


