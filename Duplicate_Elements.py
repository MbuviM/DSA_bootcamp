"""
Question One (1) Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""

# Create a function named sort_array_num
def sort_array_nums(list):
    # Sort the arrays first
    list.sort()

    # Check if the list is empty or has only one element
    if len(list) <= 1:
        return list
    
    # Initialize the index of the unique elements
    unique_nums = 0
    # Create a for loop that is used to search for duplicates and remove them in the list
    for arr in range (1, len(list)):
        if list[arr] != list[unique_nums]:

            # Increment the index
            unique_nums += 1
            list[unique_nums] = list[arr] 

    # Indicates the number of unique elements in the list
    return unique_nums + 1

# Function call
list=[10, 20, 20, 30, 40, 50, 40, 10]
new_list = sort_array_nums(list)

# Print the modified list and its new length
print("Modified Array:", list[:new_list])
print("New Length:", new_list)
