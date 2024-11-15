# Linear Search Function
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if found
    return -1  # Return -1 if not found

# Binary Search Function
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if found
        elif arr[mid] < target:
            left = mid + 1  # Search right
        else:
            right = mid - 1  # Search left
    return -1  # Return -1 if not found

# Example Usage
numbers = [5, 3, 8, 6, 2]
target = 8

# Linear Search
print("Linear Search:")
index = linear_search(numbers, target)
if index != -1:
    print(f"Found {target} at index {index}")
else:
    print(f"{target} not found")

# Binary Search
numbers.sort()  # Binary Search requires sorted list
print("\nBinary Search:")
print(f"Sorted list: {numbers}")
index = binary_search(numbers, target)
if index != -1:
    print(f"Found {target} at index {index}")
else:
    print(f"{target} not found")
