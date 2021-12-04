def read_lines():
    with open("input_files/01.txt", "r", encoding="utf-8") as f:
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
    print(f"Answer Part 1: {part_1(read_lines())}")
    print(f"Answer Part 2: {part_2(read_lines())}")
