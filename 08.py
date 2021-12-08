import time
from collections import defaultdict


def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.rstrip().split(" | ") for line in f.readlines()]
        lines2 = [[item.split(" ") for item in coordinate] for coordinate in lines]
    return lines2


def part_1(lines):
    digits = [digit for lst in [line[1] for line in lines] for digit in lst]
    counter = 0
    for digit in digits:
        if len(digit) in {2, 3, 4, 7}:
            counter += 1
    return counter


def decode_entry(patterns):
    lengths = defaultdict(list)
    for pattern in patterns:
        lengths[len(pattern)].append(pattern)

    # start by identifying which segments belong to 1,7 and 4
    pattern_dict = {1: lengths[2][0], 4: lengths[4][0], 7: lengths[3][0], 8: lengths[7][0]}
    # continue with identifying sub-patterns
    pattern_dict[3] = lengths[5][[set(pattern_dict[7]) <= set(item) for item in lengths[5]].index(True)]
    pattern_dict[6] = lengths[6][[set(pattern_dict[7]) <= set(item) for item in lengths[6]].index(False)]
    pattern_dict[9] = lengths[6][[set(pattern_dict[3]) <= set(item) for item in lengths[6]].index(True)]
    pattern_dict[5] = lengths[5][[set(pattern_dict[6]) >= set(item) for item in lengths[5]].index(True)]
    pattern_dict[0] = lengths[6][[set(pattern_dict[5]) <= set(item) for item in lengths[6]].index(False)]
    pattern_dict[2] = lengths[5][[set(pattern_dict[9]) >= set(item) for item in lengths[5]].index(False)]
    return pattern_dict


def part_2(lines):
    res = 0
    for line in lines:
        pattern_dict = decode_entry(["".join(sorted(pattern)) for pattern in line[0]])
        pattern_dict_inverted = {v: k for k, v in pattern_dict.items()}

        digit_pattern = ["".join(sorted(pattern)) for pattern in line[1]]
        output_number = int("".join([str(pattern_dict_inverted[d]) for d in digit_pattern]))
        res += output_number
    return res


if __name__ == "__main__":
    file_path = "input_files/08_test.txt"
    start_time = time.time()
    assert part_1(read_lines(file_path)) == 26
    assert part_2(read_lines(file_path)) == 61229
    print(f"Tests passed ({(time.time() - start_time) * 1000:.2f} ms)")

    file_path = "input_files/08.txt"
    start_time = time.time()
    print(f"Answer Part 1: {part_1(read_lines(file_path))}\t ({(time.time() - start_time) * 1000:.2f} ms)")
    start_time = time.time()
    print(f"Answer Part 2: {part_2(read_lines(file_path))}\t ({(time.time() - start_time) * 1000:.2f} ms)")
