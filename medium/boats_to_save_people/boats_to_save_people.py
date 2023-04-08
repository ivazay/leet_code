from typing import *


def numRescueBoats(people: List[int], limit: int) -> int:
    people.sort()
    start = 0
    end = len(people) - 1
    boats = 0

    while end > start:

        if people[start] + people[end] <= limit:
            start += 1

        end -= 1
        boats += 1

    if end == start:
        boats += 1

    return boats


if __name__ == '__main__':
    assert numRescueBoats([1,2], 3) == 1
    assert numRescueBoats([3,2,2,1], 3) == 3
    assert numRescueBoats([3,5,3,4], 5) == 4