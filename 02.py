def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.rstrip() for line in f.readlines()]
    directions = [line.split()[0] for line in lines]
    distances = [int(line.split()[1]) for line in lines]
    return directions, distances


def part_1(directions, distances):
    pos_x, pos_y = 0, 0
    for direction, distance in zip(directions, distances):
        if direction == "forward":
            pos_x += distance
        elif direction == "up":
            pos_y -= distance
        elif direction == "down":
            pos_y += distance
    return pos_x * pos_y


def part_2(directions, distances):
    pos_x, pos_y, aim = 0, 0, 0
    for direction, distance in zip(directions, distances):
        if direction == "forward":
            pos_x += distance
            pos_y += distance * aim
        elif direction == "up":
            aim -= distance
        elif direction == "down":
            aim += distance
    return pos_x * pos_y


if __name__ == "__main__":
    file_path = "input_files/02_test.txt"
    assert part_1(*read_lines(file_path)) == 150
    assert part_2(*read_lines(file_path)) == 900
    print(f"Tests passed")

    file_path = "input_files/02.txt"
    print(f"Answer Part 1: {part_1(*read_lines(file_path))}")
    print(f"Answer Part 2: {part_2(*read_lines(file_path))}")
