def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.rstrip() for line in f.readlines()]
    return lines


def most_common(lst):
    """Return the most common element. If equal, then return 1
    """
    if sum(lst) / len(lst) >= 0.5:
        return 1
    else:
        return 0


def concatenate(list_of_ints):
    list_of_strings = [str(i) for i in list_of_ints]
    return "".join(list_of_strings)


def generate_gamma_epsilon_rates(lines):
    gamma_rate = []
    epsilon_rate = []
    for i in range(bits):
        column_i = [int(line[i]) for line in lines]
        gamma_rate.append(most_common(column_i))
        epsilon_rate.append(1 - most_common(column_i))
    return gamma_rate, epsilon_rate


def part_1(lines):
    gamma_rate, epsilon_rate = generate_gamma_epsilon_rates(lines)
    gamma_rate_base_10 = int(concatenate(gamma_rate), 2)
    epsilon_rate_base_10 = int(concatenate(epsilon_rate), 2)
    return gamma_rate_base_10 * epsilon_rate_base_10


def remove_bad_lines(lines, gamma, pos):
    """Read lines and removes rows which do not correspond to the comparison list in the given pos
    """
    gamma_rate, epsilon_rate = generate_gamma_epsilon_rates(lines)
    if gamma:
        comparison_list = gamma_rate
    elif not gamma:
        comparison_list = epsilon_rate

    bad_lines = []
    for i, line in enumerate(lines):
        if int(line[pos]) != int(comparison_list[pos]):
            bad_lines.append(line)

    for i in bad_lines:
        lines.remove(i)
    return lines


def part_2(lines):
    co2_lines = lines.copy()
    o2_lines = lines.copy()

    for i in range(bits):
        if len(co2_lines) > 1:
            co2_lines = remove_bad_lines(co2_lines, True, i)

    for i in range(bits):
        if len(o2_lines) > 1:
            o2_lines = remove_bad_lines(o2_lines, False, i)

    return int(concatenate(co2_lines), 2) * int(concatenate(o2_lines), 2)


if __name__ == "__main__":
    bits = 5
    file_path = "input_files/03_test.txt"
    assert part_1(read_lines(file_path)) == 198
    assert part_2(read_lines(file_path)) == 230
    print(f"Tests passed")

    bits = 12
    file_path = "input_files/03.txt"
    print(f"Answer Part 1: {part_1(read_lines(file_path))}")
    print(f"Answer Part 2: {part_2(read_lines(file_path))}")
