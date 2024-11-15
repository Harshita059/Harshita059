def power(base, exponent):
    result = 1
    while exponent > 0:
        # If the exponent is odd, multiply the result by the base
        if exponent % 2 == 1:
            result *= base
        # Square the base and halve the exponent
        base *= base
        exponent //= 2
    return result

# Example usage
base = 2
exponent = 10
print(f"{base} raised to the power {exponent} is {power(base, exponent)}")
