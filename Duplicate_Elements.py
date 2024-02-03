"""
Question One (1) Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""

# Create a function named sort_array_num
def sort_array_nums(list):
    # Create a for loop that is used to search for duplicates and remove them in the list
    for arr in list:
        if list.count(arr) > 1:
            list.remove(arr)

        else:
            continue

# Function call
list=[1, 2, 2, 3, 4, 5, 4, 1]
sort_array_num(list)

print(list)