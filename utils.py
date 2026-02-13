def _is_strictly_increasing(numbers: list[int]) -> bool:
    """Check if a list of numbers is strictly decreasing."""
    return all(x < y for x, y in zip(numbers, numbers[1:]))


def _is_strictly_decreasing(numbers: list[int]) -> bool:
    """Check if a list of numbers is strictly decreasing."""
    return all(x > y for x, y in zip(numbers, numbers[1:]))


def is_monotonic(numbers: list[int]) -> bool:
    """Check if a list of numbers is monotonically increasing or decreasing."""
    return _is_strictly_increasing(numbers) or _is_strictly_decreasing(numbers)


def difference_rule(numbers: list[int]) -> bool:
    """
    Check if a list of numbers has pairwise differences of at most 3.

    Don't need to check the 'at-least-1' rule because our monotonicity rule
    doesn't allow repeated numbers
    """
    return all(abs(x - y) <= 3 for x, y in zip(numbers, numbers[1:]))


def problem_dampener(report: list[int]) -> bool:
    """
    Check if a report would be safe if 1 bad level were removed.

    Take the given input report and make several alt versions of it,
    each with a different level removed. Check if any of these
    alt versions are now safe.

    :param list[int] numbers: The report
    :return bool: Whether the report would be safe without one level
    """

    one_level_removed_reports = []

    for i in range(len(report)):
        one_level_removed = [
            level for j, level in enumerate(report) if j != i
        ]
        one_level_removed_reports.append(one_level_removed)

    return any(
        is_monotonic(report) and difference_rule(report) for report in one_level_removed_reports
    )
