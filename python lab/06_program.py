# Selection Sort Function
def selection_sort(arr):
    for i in range(len(arr)):
        # Find the minimum element in the unsorted part
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Insertion Sort Function
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements greater than key one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
numbers1 = [64, 25, 12, 22, 11]
numbers2 = [64, 25, 12, 22, 11]

# Selection Sort
print("Selection Sort:")
selection_sort(numbers1)
print(f"Sorted list: {numbers1}")

# Insertion Sort
print("\nInsertion Sort:")
insertion_sort(numbers2)
print(f"Sorted list: {numbers2}")
