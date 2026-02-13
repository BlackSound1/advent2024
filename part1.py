from utils import difference_rule, is_monotonic


def main():
    with open("actual-data.txt", 'r') as f:
        reports = f.readlines()

    monotonic_reports = []
    safe_reports = []

    # Find monotonic reports (where repeated numbers DO NOT count toward monotonicity)
    for report in reports:
        line_as_nums = [int(num) for num in report.split(' ')]
        if is_monotonic(line_as_nums):
            monotonic_reports.append(line_as_nums)

    # Go through these monotonic reports to find ones that meet the difference rule
    for report in monotonic_reports:
        if difference_rule(report):
            safe_reports.append(report)

    print("Result:", len(safe_reports))


if __name__ == "__main__":
    main()
