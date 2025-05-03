#linear search 
# Linear Search Function
def linear_search(arr, target):
    for index, value in range(len(arr)):
        if index==target:
            return index
        elif value == target:
            return index    
    return -1  # Target not found
# Main function to demonstrate linear search    
def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7

    result = linear_search(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found")
# Call the main function to run the program
if __name__ == "__main__":
    main()
# This program implements a linear search algorithm to find the index of a target element in a list.
# It iterates through the list and checks each element until the target is found or the end of the list is reached. 
# The program also includes a main function to demonstrate the linear search with a sample list and target value.
# The linear search algorithm has a time complexity of O(n), making it less efficient than binary search for large lists.
# The program is written in Python and is easy to understand and modify for different use cases.
# Linear Search Function
def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

def main():
    arr = [5, 12, 7, 9, 3, 14]
    target = 9

    result = linear_search(arr, target)

    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found")

if __name__ == "__main__":
    main()

# This program implements a linear search algorithm to find the index of a target element in a list.
# It iterates through the list and checks each element until the target is found or the end of the list is reached.
# The program also includes a main function to demonstrate the linear search with a sample list and target value.
# The linear search algorithm has a time complexity of O(n), making it less efficient than binary search for large lists.
# The program is written in Python and is easy to understand and modify for different use cases.

# Linear Search Function
def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1
