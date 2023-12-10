from typing import List

from puzzle_map import PuzzleMap


def read_text_file_to_lines(filename: str) -> List[str]:
    my_file = open(filename, "r")
    data = my_file.read()
    data_to_list = data.splitlines()
    my_file.close()
    return data_to_list




if __name__ == "__main__":
    data = read_text_file_to_lines("day10\example_1.txt")
    puzzle_map = PuzzleMap(data)
    # print(puzzle_map.get_adjoining_pipes(77,34))
    loop = puzzle_map.get_loop()
    print(loop)
    