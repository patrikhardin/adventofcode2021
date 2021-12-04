import numpy as np


class BingoBoard:
    def __init__(self, board: np.ndarray, solved=False):
        self.board = board
        self.played_numbers = np.zeros(shape=(5, 5))
        self.solved = False
        assert board.shape == (5, 5)

    def __str__(self):
        return "I am a board!"

    def play_numbers(self, numbers: list):
        # Boolean array with True if the number has been played
        self.played_numbers = np.isin(self.board, numbers)

    def is_solved(self):
        # check if a row or column is all True
        solved_cols = np.all(self.played_numbers == 1, axis=0)
        solved_rows = np.all(self.played_numbers == 1, axis=1)
        return np.any((solved_cols + solved_rows) == 1)


def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip().replace("  ", " ") for line in f.readlines()]
    return lines


def play_bingo(lines):
    # clean up the input lines
    size = len(lines)
    idx_list = [idx + 1 for idx, val in enumerate(lines) if val == ""]
    res = [lines[i: j] for i, j in zip([0] + idx_list, idx_list + ([size] if idx_list[-1] != size else []))]

    # remove the last empty string element in each of the elements in res
    res_clean = []
    for lst in res:
        res_clean.append([item for item in lst if item])

    # divide into the numbers and the boards
    game_number_list = [int(n) for n in res_clean[0][0].split(",")]
    board_lists = res_clean[1:]

    # clean up the board lists
    board_arrays = []
    for board in board_lists:
        board_array = np.zeros(shape=(5, 5))
        for i, row in enumerate(board):
            for j, element in enumerate(row.split(" ")):
                board_array[i][j] = element
        board_arrays.append(board_array)

    # instantiate BingoBoards objects
    bingo_boards = [BingoBoard(board=a) for a in board_arrays]

    # now we play Bingo!
    # iterate through game_list and check every board for each increment

    assignment_sums = []
    for i in range(len(game_number_list)):
        current_numbers = game_number_list[:i+1]
        for j, bingo_board in enumerate(bingo_boards):
            bingo_board.play_numbers(current_numbers)
            if bingo_board.is_solved():
                # get (1) the last number and (2) Hadamard product of board and inverted played_numbers matrices
                last_number = current_numbers[-1]
                hadamard_prod = np.multiply(bingo_board.board, np.invert(bingo_board.played_numbers))
                board_sum = hadamard_prod.sum()
                assignment_sums.append(int(last_number * board_sum))
                bingo_boards.remove(bingo_board)

    return assignment_sums


if __name__ == "__main__":
    file_path = "input_files/04.txt"
    print(f"Answer Part 1: {play_bingo(read_lines(file_path))[0]}")
    print(f"Answer Part 2: {play_bingo(read_lines(file_path))[-1]}")