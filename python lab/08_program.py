def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def first_n_primes(n):
    primes = []
    num = 2  # Start checking from the first prime number
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Example usage
n = 10
print(f"The first {n} prime numbers are: {first_n_primes(n)}")
