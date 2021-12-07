import time


def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return [int(i) for i in f.readline().rstrip().split(",")]


def minimize_fuel(positions: list, linear: bool):
    res = {}
    for target in range(min(positions), max(positions)+1):
        distances = [abs(pos - target) for pos in positions]
        if linear:
            res[target] = sum(distances)
        else:
            res[target] = sum([d*(d+1)/2 for d in distances])  # sum of natural numbers)
    return int(min(res.values()))


if __name__ == "__main__":
    file_path = "input_files/07_test.txt"
    start_time = time.time()
    assert minimize_fuel(read_lines(file_path), True) == 37
    assert minimize_fuel(read_lines(file_path), False) == 168
    print(f"Tests passed ({(time.time() - start_time) * 1000:.2f} ms)")

    file_path = "input_files/07.txt"
    start_time = time.time()
    print(f"Answer Part 1: {minimize_fuel(read_lines(file_path), True)}\t ({(time.time() - start_time)*1000:.2f} ms)")
    start_time = time.time()
    print(f"Answer Part 2: {minimize_fuel(read_lines(file_path), False)}\t ({(time.time() - start_time)*1000:.2f} ms)")
