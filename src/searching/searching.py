# Implements a recursive binary search —
def binary_search(arr, target, start, end):

    # Compute halfway using start and end...
    halfway = start + end // 2

    # If array is empty...
    if len(arr) == 0:
        return -1

    # If the item was not found anywhere in the list...
    elif start >= end:
        return -1

    # If the target is the halfway value...
    elif arr[halfway] == target:
        return halfway

    # If target is in lower half of array...
    elif target < arr[halfway]:
        return binary_search(arr, target, start, halfway)

    # If target is in upper half of array...
    else:
        return binary_search(arr, target, halfway + 1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
#def agnostic_binary_search(arr, target):
    # Your code here

