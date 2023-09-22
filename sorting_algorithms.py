from tqdm import tqdm
import random
import numpy as np
import time
import matplotlib.pyplot as plt
from HeapSort import heap_sort


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


def counting_sort(arr):
    if len(arr) == 0:
        return arr
    min_element = min(arr)
    max_element = max(arr)
    auxiliary_arr = [0] * (max_element - min_element + 1)
    for value in arr:
        auxiliary_arr[value - min_element] += 1
    final_arr = [0] * len(arr)
    j = 0
    for i in range(len(auxiliary_arr)):
        for occur in range(auxiliary_arr[i]):
            final_arr[j] = i + min_element
            j += 1
    return final_arr


arr = [0, 3, 10, -2, 9, 23, 8]


def quick_sort(arr):
    a = arr[:]  # מעתיק את המערך ולא דורס מערך קלט
    if len(a) < 2:
        return a
    arr_right = []
    arr_left = []
    pivot_idx = int(len(a) / 2)
    pivot = a.pop(pivot_idx)
    for i in range(len(a)):
        if pivot < a[i]:
            arr_right.append(a[i])
        else:
            arr_left.append(a[i])
    arr_right = quick_sort(arr_right)
    arr_left = quick_sort(arr_left)
    a = arr_left + [pivot] + arr_right
    return a
    # return a


def bubble_sort_recursive(a, end):
    for i in range(1, end):
        if a[i] < a[i - 1]:
            a[i], a[i - 1] = a[i - 1], a[i]
    if end > 0:
        bubble_sort_recursive(a, end - 1)


def bubble_sort(a):
    bubble_sort_recursive(a, len(a))
    return a


mylist = [0, 0, 3, 10, -2.9, 9, 23, 8.3]


# print(bubble_sort(arr))
# print(arr)

def merge_sort(mylist):
    if len(mylist) > 1:
        arr_right = []
        arr_left = []
        pivot = int(len(mylist) / 2)
        for i in range(pivot, len(mylist)):
            if pivot <= i:
                arr_right.append(mylist[i])
        for i in range(pivot):
            if pivot > i:
                arr_left.append(mylist[i])
        merge_sort(arr_right)
        merge_sort(arr_left)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(arr_left) and j < len(arr_right):
            if arr_left[i] <= arr_right[j]:
                # The value from the left half has been used
                mylist[k] = arr_left[i]
                # Move the iterator forward
                i += 1
            else:
                mylist[k] = arr_right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(arr_left):
            mylist[k] = arr_left[i]
            i += 1
            k += 1

        while j < len(arr_right):
            mylist[k] = arr_right[j]
            j += 1
            k += 1
    return mylist


# merge_sort(mylist)


#  Test function to verify sorting algorithms
def test_sorting_algorithm(sort_func, n=10):
    # Perform n random test cases
    for _ in range(n):
        length = random.randint(10, 100)
        arr = [random.randint(100, 100_000) for _ in range(length)]
        expected = sorted(arr)
        # Verify that the sorted array matches the expected result
        assert sort_func(arr) == expected

    print("All test cases passed")


test_sorting_algorithm(insertion_sort)
length = 10
random.sample(range(length ** 3), length)


# Function to plot the performance of sorting algorithms
def plot_sorting_performance(algorithms):
    # Define the lengths of arrays for performance testing
    lengths = [100, 500, 1_000, 5_000, 10_000, 15_000, 20_000]
    for algo_name, algo_func in algorithms.items():
        print(algo_name)
        execution_times = []
        for length in lengths:
            print(algo_name, f'len: {length}')
            arr = random.sample(range(length ** 3), length)
            start_time = time.time()
            algo_func(arr)
            end_time = time.time()
            execution_times.append(end_time - start_time)

        # Plot the execution times for each array length
        plt.plot(lengths, execution_times, label=algo_name)

    plt.xlabel("Array Length")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.show()


# algorithms = {'insertion_sort':insertion_sort}

algorithms = {'insertion_sort': insertion_sort,
             'alfa_quick_sort': quick_sort,  'heap_sort': heap_sort,
             'counting_sort': counting_sort, 'merge_alfa': merge_sort}
plot_sorting_performance(algorithms)
