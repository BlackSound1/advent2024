def is_strictly_increasing(numbers: list[int]) -> bool:
    """Check if a list of numbers is strictly decreasing."""
    return all(x < y for x, y in zip(numbers, numbers[1:]))


def is_strictly_decreasing(numbers: list[int]) -> bool:
    """Check if a list of numbers is strictly decreasing."""
    return all(x > y for x, y in zip(numbers, numbers[1:]))


def is_monotonic(numbers: list[int]) -> bool:
    """Check if a list of numbers is monotonically increasing or decreasing."""
    return is_strictly_increasing(numbers) or is_strictly_decreasing(numbers)


def difference_rule(numbers: list[int]) -> bool:
    """
    Check if a list of numbers has pairwise differences of at most 3.

    Don't need to check the 'at-least-1' rule because our monotonicity rule
    doesn't allow repeated numbers
    """
    return all(abs(x - y) <= 3 for x, y in zip(numbers, numbers[1:]))


def main():
    with open("actual-data.txt", 'r') as f:
        lines = f.readlines()

    monotonic_lists = []

    # Fill up a list of monotonic lines (where repeated numbers DO NOT count toward monotonicity)
    for line in lines:
        line_as_nums = [int(num) for num in line.split(' ')]
        if is_monotonic(line_as_nums):
            monotonic_lists.append(line_as_nums)

    safe_lists = []

    # Go through these monotonic lists to find ones that meet the difference rule
    for ls in monotonic_lists:
        if difference_rule(ls):
            safe_lists.append(ls)

    print("Result:", len(safe_lists))


if __name__ == "__main__":
    main()
