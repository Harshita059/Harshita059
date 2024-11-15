def find_max(numbers):
    max_num = numbers[0]  # Start with the first number
    for num in numbers:
        if num > max_num:
            max_num = num  # Update max if a larger number is found
    return max_num

# Example usage
numbers = [5, 12, 7, 3, 15, 10]
print(f"The maximum number is: {find_max(numbers)}")
