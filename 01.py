def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [int(line.rstrip()) for line in f.readlines()]
    return lines


def part_1(lines):
    return sum([1 for i in range(len(lines)-1) if lines[i+1] - lines[i] > 0])


def part_2(lines):
    windows = []
    for i in range(len(lines)-2):
        window = lines[i] + lines[i+1] + lines[i+2]
        windows.append(window)
    return part_1(windows)


if __name__ == "__main__":
    file_path = "input_files/01_test.txt"
    assert part_1(read_lines(file_path)) == 7
    assert part_2(read_lines(file_path)) == 5
    print(f"Tests passed")

    file_path = "input_files/01.txt"
    print(f"Answer Part 1: {part_1(read_lines(file_path))}")
    print(f"Answer Part 2: {part_2(read_lines(file_path))}")
