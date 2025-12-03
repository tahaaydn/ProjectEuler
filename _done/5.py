"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time
import math

def timer(func):
    def wrapper(*args, **kwargs):
        nonlocal total
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        total += duration
        print(f"Execution time: {duration:.2e}   Total: {total:.2e}")
        return result

    total = 0
    return wrapper

# ---

# @timer
# def no_remainder(limit: int) -> int:
#     number = limit
#     while True:
#         if all(number % i == 0 for i in range(2, limit + 1)):
#             return number
#         number += limit
 
@timer
def no_remainder_math(limit: int) -> int:
    result = 1
    for i in range(2, limit + 1):
        result = math.lcm(result, i)
    return result

# ---

if __name__ == "__main__":
    result = no_remainder_math(20)
    # result = no_remainder(20)

    print(result)

# no_remainder      Execution time: 3.32~      Total: 3.32~
# no_remainder_math Execution time: 6.68e-06   Total: 6.68e-06
