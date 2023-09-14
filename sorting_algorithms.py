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


arr = [0, 3, 10, -2, 9, 23, -90, 8]


def Quick_Sort(arr):
    arr = arr[:]
    if len(arr) < 2:
        return arr

    arr_right = []
    arr_left = []
    pivot_idx = int(len(arr) / 2)
    pivot = arr.pop(pivot_idx)
    for i in range(len(arr)):
        if pivot < arr[i]:
            arr_right.append(arr[i])
        else:
            arr_left.append(arr[i])
    arr_addright = []
    arr_right = Quick_Sort(arr_right)
    arr_left = Quick_Sort(arr_left)
    arr = arr_left + [pivot] + arr_right
    return arr
Quick_Sort(arr)


# function test of all algoritms
def test(sorting_function, num_of_tests):
    for _ in tqdm(range(num_of_tests)):
        random_length = random.randint(0, 200)
        random_list = [random.randint(-20000, 20000) for _ in range(random_length)]
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


test(Quick_Sort, 10)
