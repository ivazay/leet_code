"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats
where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided
the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
"""


from typing import *


def numRescueBoats(people: List[int], limit: int) -> int:
    # v1
    # boats = []
    #
    # while people:
    #     hw = max(people)
    #     lw = min(people)
    #
    #     if hw == limit:
    #         boat = (people.pop(people.index(hw)),)
    #         boats.append(boat)
    #
    #     elif hw < limit:
    #         if hw + lw <= limit and len(people) > 1:
    #             boat = (people.pop(people.index(hw)), people.pop(people.index(lw)))
    #             boats.append(boat)
    #         else:
    #             boat = (people.pop(people.index(hw)),)
    #             boats.append(boat)
    #
    # return len(boats)

    people.sort()
    left = 0
    right = len(people) - 1
    boats = 0

    while right > left:

        if people[left] + people[right] <= limit:
            left += 1

        right -= 1
        boats += 1

    if right == left:
        boats += 1

    return boats


if __name__ == '__main__':
    assert numRescueBoats([1,2], 3) == 1
    assert numRescueBoats([3,2,2,1], 3) == 3
    assert numRescueBoats([3,5,3,4], 5) == 4