"""
Given an integer number n, return the difference between the product
of its digits and the sum of its digits.

Constraints:
1 <= n <= 10^5
"""


def subtract_product_and_sum(n: int) -> int:
    product, summ = 1, 0

    for num in str(n):
        product *= int(num)
        summ += int(num)
    return product - summ


if __name__ == "__main__":
    assert subtract_product_and_sum(243) == 15
    assert subtract_product_and_sum(4421) == 21
    assert subtract_product_and_sum(243) == 15
