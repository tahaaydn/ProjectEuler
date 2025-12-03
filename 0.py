"""
A number is a perfect square, or a square number, if it is the square of a positive integer.
For example, 25 is a square number because 5**2 = 5 * 5 = 25; it is also an odd square.

The first 5 square numbers are: 1, 4, 9, 16, 25, and the sum of the odd squares is 1 + 9 + 25 = 35.

Among the first 783 thousand square numbers, what is the sum of all the odd squares?
"""

def sum_of_squares(limit: int) -> int:
    sum = 0
    for i in range(1, limit):
        square = i * i
        if square % 2 == 1:
            sum += square
    return sum

# ---

if __name__ == "__main__":
    result = sum_of_squares(783001)
    print(result)
