"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time

def timer(func):
    def wrapper(*args, **kwargs):
        nonlocal total
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        total += duration
        print(f"Execution time: {duration}   Total: {total}")
        return result

    total = 0
    return wrapper

# ---

is_palindrome = lambda n: True if str(n)==str(n)[::-1] else False

@timer
def product_of_palindrome(max_number):
    biggest = 0
    for number1 in range(max_number, 1, -1):
        for number2 in range(max_number, 1, -1):
            product = number1 * number2
            if product >= biggest:
                if is_palindrome(product):
                    biggest = product
    return biggest

# ---

if __name__ == "__main__":
    result = product_of_palindrome(999)
    print(result)

# Execution time: 0.027~