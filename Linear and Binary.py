# CIS 103: Introduction to Programming
# Homework 5: Searching, Sorting, and Complexity Analysis( problem 1)
# Instructor: Md Ali
#Ndubuisi mbamalu
# Date: 10/11/2024

# 1 Implementing Linear and Binary Search.
# a)Linear
def linear_search(lst, target):
    for index, element in enumerate(lst):
        if element == target:
            return index
    return -1
#For example the function was applied to the list [3, 5, 7, 9, 11] with the target element 7. The function returned 2, which is the index of 7 in the list. If the target is not found, the function will return -1.

# b)Binary
def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_element = lst[mid]
        if mid_element == target:
            return mid
        elif mid_element < target:
            left = mid + 1
        else:
            right = mid - 1

        return -1
    #The function was applied to the sorted list [1, 3, 5, 7, 9, 11, 13] with the target element 7. The function returned 3, which is the index of 7 in the list.

# c)Comparing Time Complexity
import time
import random

# Linear search implementation
def linear_search(lst, target):
    for index, element in enumerate(lst):
        if element == target:
            return index
    return -1

#Binary search implementation
def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_element = lst[mid]
        if mid_element == target:
            return mid
        elif mid_element < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

#Driver code to compare performance
def compare_search_algorithms():
    list_sizes = [1000, 10000, 100000]
    for size in list_sizes:
        #Generate random sorted list
        sorted_list = sorted(random.sample(range(1, size * 10), size))
        target = random.choice(sorted_list)

        print(f"List size: {size}")

        #Measure time for linear search
        start_time = time.time()
        linear_search(sorted_list, target)
        end_time = time.time()
        print(f"Linear Search took: {end_time - start_time:.6f} seconds")

        #Measure time for binary search
        start_time = time.time()
        binary_search(sorted_list, target)
        end_time = time.time()
        print(f"Binary Search took: {end_time - start_time:.6f} seconds")
        print("-" * 40)

        #compare performance
        compare_search_algorithms()

