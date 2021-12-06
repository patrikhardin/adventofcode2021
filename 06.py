from collections import Counter
import time


def read_lines(file_path):
    """Read the first line and return a Counter with the initial state"""
    with open(file_path, "r", encoding="utf-8") as f:
        return Counter(map(int, f.readline().rstrip().split(",")))


def count_fishes(fish_counter: Counter, days: int):
    for day in range(days):
        fish_0 = fish_counter[0]  # store number of reproducing fish
        for i in range(max(fish_counter.keys()) + 1):  # update Counter keys by shifting the values left
            fish_counter[i] = fish_counter.get(i + 1, 0)  # set 0 if key does not exist
        fish_counter[6] += fish_0  # the zero fish reset to 6
        fish_counter[8] += fish_0  # they also generate an 8 each
    return sum(fish_counter.values())


if __name__ == "__main__":
    file_path = "input_files/06_test.txt"
    start_time = time.time()
    assert count_fishes(read_lines(file_path), 80) == 5934
    assert count_fishes(read_lines(file_path), 256) == 26984457539
    print(f"Tests passed ({(time.time() - start_time) * 1000:.2f} ms)")

    file_path = "input_files/06.txt"
    start_time = time.time()
    print(f"Answer Part 1: {count_fishes(read_lines(file_path), 80)}\t ({(time.time() - start_time) * 1000:.2f} ms)")
    start_time = time.time()
    print(f"Answer Part 1: {count_fishes(read_lines(file_path), 256)}\t ({(time.time() - start_time) * 1000:.2f} ms)")
