from utils import difference_rule, is_monotonic


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
