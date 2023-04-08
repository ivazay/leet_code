"""
You are given two integers, x and y, which represent your current location
on a Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi]
represents that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or
the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from
your current location. If there are multiple, return the valid point with the smallest index.
If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).


Constraints:
1 <= points.length <= 10 ** 4
points[i].length == 2
1 <= x, y, ai, bi <= 10 ** 4
"""


def nearest_valid_point(x: int, y: int, points: list[list[int]]) -> int:
    distance: int = 10_000
    index: int = -1

    for i, nums in enumerate(points):
        x2, y2 = nums[0], nums[1]
        if x2 == x or y2 == y:
            if abs(x - x2) + abs(y - y2) < distance:
                distance = abs(x - x2) + abs(y - y2)
                index = i

    return index


if __name__ == "__main__":
    assert nearest_valid_point(3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]) == 2
    assert nearest_valid_point(3, 4, [[3, 4]]) == 0
    assert nearest_valid_point(3, 4, [[2, 3]]) == -1
