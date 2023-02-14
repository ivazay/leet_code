"""
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
Return the average salary of employees excluding the minimum and maximum salary.
Answers within 10-5 of the actual answer will be accepted.

Constraints:
3 <= salary.length <= 100
1000 <= salary[i] <= 106
All the integers of salary are unique.
"""


def average(salary: list[int]) -> float:
    salary.remove(max(salary))
    salary.remove(min(salary))

    return sum(salary) / float(len(salary))


if __name__ == "__main__":
    assert average([4000, 3000, 1000, 2000]) == 2500.00
    assert average([1000, 2000, 3000]) == 2000.00
    assert average([4000, 3000, 1000]) == 3000.00
