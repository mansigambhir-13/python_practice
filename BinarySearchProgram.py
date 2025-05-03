[1,2,3,4,5,6,7,8,9,10]
# Binary Search Program
# This program implements a binary search algorithm to find the index of a target value in a sorted list.
# It uses recursion to divide the list into halves until the target is found or the search space is exhausted.
# The program also includes a main function to demonstrate the binary search with a sample list and target value.
# The binary search algorithm has a time complexity of O(log n), making it efficient for large lists.
# The program is written in Python and is easy to understand and modify for different use cases.
# Binary Search Function

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 7))   # Output: 3
print(binary_search(arr, 4))   # Output: -1



def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Base case: target not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


# Main function to demonstrate binary search    

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7

    # Iterative binary search
    result_iterative = binary_search(arr, target)
    if result_iterative != -1:
        print(f"Element {target} found at index {result_iterative} (Iterative)")
    else:
        print(f"Element {target} not found (Iterative)")

    # Recursive binary search
    result_recursive = binary_search_recursive(arr, target, 0, len(arr) - 1)
    if result_recursive != -1:
        print(f"Element {target} found at index {result_recursive} (Recursive)")
    else:
        print(f"Element {target} not found (Recursive)")