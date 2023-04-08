def average(salary: list[int]) -> float:
    salary.remove(max(salary))
    salary.remove(min(salary))

    return sum(salary) / float(len(salary))


if __name__ == "__main__":
    assert average([4000, 3000, 1000, 2000]) == 2500.00
    assert average([1000, 2000, 3000]) == 2000.00
    assert average([4000, 3000, 1000]) == 3000.00
