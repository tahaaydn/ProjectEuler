"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
is_prime = lambda n: all(n%i != 0 for i in range(2, int(n**.5)+1))

def prime_factorization(number: int) -> int:
    prime_factors = []
    for i in range(2, int(number**.5)+1):
        if number % i == 0:
            if is_prime(i):
                number /= i
                prime_factors.append(i)
    return prime_factors, max(prime_factors)

# ---

if __name__ == "__main__":
    primes, result = prime_factorization(600851475143)
    print(primes, result)