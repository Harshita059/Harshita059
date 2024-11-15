def newton_sqrt(number):
    guess = number / 2.0  # Initial guess
    for _ in range(10):  # Perform 10 iterations
        guess = (guess + number / guess) / 2.0
    return guess

# Example usage
num = 49
print(f"The square root of {num} is approximately {newton_sqrt(num):.6f}")
