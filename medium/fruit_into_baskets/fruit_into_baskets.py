"""
You are visiting a farm that has a single row of fruit trees arranged from left to right.
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no
limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree
(including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length
"""


def total_fruit(fruits: list[int]) -> int:
    max_size = 0

    for num in range(len(fruits)):
        basket = set()
        right = num

        while right < len(fruits):
            if fruits[right] not in basket and len(basket) == 2:
                break
            basket.add(fruits[right])
            right += 1
        max_size = max(max_size, right - num)

    return max_size


if __name__ == '__main__':
    assert total_fruit([1, 2, 1]) == 3
    assert total_fruit([0, 1, 2, 2]) == 3
    assert total_fruit([1, 2, 3, 2, 2]) == 4
