from utils import difference_rule, is_monotonic, problem_dampener


def main():
    with open("actual-data.txt", 'r') as f:
        reports = f.readlines()

    unsafe_reports = []
    safe_reports = []
    monotonic_reports = []

    # Find monotonic reports (where repeated numbers DO NOT count toward monotonicity)
    for report in reports:
        report_as_nums = [int(num) for num in report.split(' ')]

        if is_monotonic(report_as_nums):
            monotonic_reports.append(report_as_nums)
        else:
            unsafe_reports.append(report_as_nums)

    # Go through these monotonic reports to find ones that meet the difference rule
    for report in monotonic_reports:
        if difference_rule(report):
            safe_reports.append(report)
        else:
            unsafe_reports.append(report)

    # Go through the unsafe reports and apply the problem dampener to it.
    # If a report is now safe, add it to the safe_reports
    for report in unsafe_reports:
        if problem_dampener(report):
            safe_reports.append(report)

    print("Result:", len(safe_reports))


if __name__ == "__main__":
    main()
