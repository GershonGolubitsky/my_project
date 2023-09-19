from tqdm import tqdm
import random
import numpy as np


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
    print(a)
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


def test(sorting_function, num_of_tests):
    for _ in tqdm(range(num_of_tests)):
        random_length = random.randint(0, 2000)
        random_list = [random.randint(0, 2000) for _ in range(random_length)]
        to_test = sorting_function(random_list)
        expected = sorted(random_list)
        if to_test != expected:
            print("FAIL!")
            print("your output is:", to_test)
            print("the expected output is:", expected)
            print("try debugging using this input:", random_list)
            return False

    print("You are a king!!")

#     return True

test(merge_sort, 1000)
