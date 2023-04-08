"""
Given an integer array nums, return the largest perimeter of a triangle
with a non-zero area, formed from three of these lengths. If it is impossible to
form any triangle of a non-zero area, return 0.

Constraints:
3 <= nums.length <= 104
1 <= nums[i] <= 106
"""


def largest_perimeter(nums: list[int]) -> int:
    nums.sort(reverse=True)

    while len(nums) >= 3:
        a, b, c = nums[0], nums[1], nums[2]
        if a + b > c and a + c > b and b + c > a:
            return a + b + c
        else:
            nums.remove(nums[0])
    return 0


if __name__ == "__main__":
    assert largest_perimeter([2, 1, 2]) == 5
    assert largest_perimeter([1, 2, 1, 10]) == 0
