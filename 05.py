import numpy as np


def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.rstrip().split(" -> ") for line in f.readlines()]
        lines2 = [[item.split(",") for item in coordinate] for coordinate in lines]
    return lines2


def longest(l1: np.ndarray, l2: np.ndarray):
    """Return the longest of two arrays"""
    if len(l1) >= len(l2):
        return l1
    else:
        return l2


def count_overlaps(lines: list, allow_diag: bool):
    grid = np.zeros(shape=(SIZE, SIZE))
    for i, l in enumerate(lines):
        x1, y1 = int(l[0][0]), int(l[0][1])
        x2, y2 = int(l[1][0]), int(l[1][1])

        xx = longest(np.arange(x1, x2 + 1, 1), np.arange(x1, x2 - 1, -1))
        yy = longest(np.arange(y1, y2 + 1, 1), np.arange(y1, y2 - 1, -1))

        # add lines if horizontal or vertical
        if len(xx) != len(yy):
            for x in xx:
                for y in yy:
                    grid[x][y] += 1

        if allow_diag:
            if len(xx) == len(yy):
                for x, y in zip(xx, yy):
                    grid[x][y] += 1

    return (grid >= 2).sum()


if __name__ == "__main__":
    SIZE = 10
    file_path = "input_files/05_test.txt"
    assert count_overlaps(read_lines(file_path), False) == 5
    assert count_overlaps(read_lines(file_path), True) == 12
    print(f"Tests passed")

    SIZE = 1000
    file_path = "input_files/05.txt"
    print(f"Answer Part 1: {count_overlaps(read_lines(file_path), False)}")
    print(f"Answer Part 2: {count_overlaps(read_lines(file_path), True)}")
