# CIS 103: Introduction to Programming
# Homework 5: Implementing Sorting Algorithms (Problem 2)
# Instructor: Md Ali
#Ndubuisi Mbamalu
# Date: 10/11/2024

# a) Bubble Sort
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
 #Track whether any swaps were made.
        swapped = False
        for j in range(0, n - i - 1):

#Swap when the element found is greater than the next element
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
#When no elements were swapped, the list is already sorted
        if not swapped:
            break
    return lst

#Example
#Unsorted list
unsorted_list = [64, 34, 25, 12, 22, 11, 90]

#Sorting the list using bubble sort
sorted_list = bubble_sort(unsorted_list)
print (sorted_list)

# b)Merge Sort
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    #Divide the list into two halves
    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])

    #Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0

    #Compare elements and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    #Append any remaining elements from both halves
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

#Unsorted list
unsorted_list = [38, 27, 43, 3, 9, 82, 10]

#Sorting the list using merge sort
sorted_list = merge_sort(unsorted_list)
print(sorted_list)

# c)Comparing Time Complexity
import time
import random

# Bubble sort implementation
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

# Merge sort implementation
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

#Driver code to compare performance of bubble sort and merge sort
def compare_sort_algorithms():
    list_sizes = [1000, 10000, 100000]
    for size in list_sizes:
        # Generate random list
        unsorted_list = random.sample(range(1, size * 10), size)

        print(f"List size: {size}")

        #Time bubble sort
        bubble_list = unsorted_list.copy()
        start_time = time.time()
        bubble_sort(bubble_list)
        end_time = time.time()
        print(f"Bubble Sort took: {end_time - start_time:.6f} seconds")

        #Time merge sort
        merge_list = unsorted_list.copy()
        start_time = time.time()
        merge_sort(merge_list)
        end_time = time.time()
        print(f"Merge Sort took: {end_time - start_time:.6f} seconds")
        print("-" * 40)

#Run the performance comparison
compare_sort_algorithms()


