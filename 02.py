def read_lines():
    with open("input_files/02.txt", "r", encoding="utf-8") as f:
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
    dirs, dists = read_lines()
    print(f"Answer Part 1: {part_1(dirs, dists)}")
    print(f"Answer Part 2: {part_2(dirs, dists)}")
