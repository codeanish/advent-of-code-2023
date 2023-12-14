from typing import List


def read_text_file_to_lines(filename: str) -> List[str]:
    my_file = open(filename, "r")
    data = my_file.read()
    data_to_list = data.splitlines()
    my_file.close()
    return data_to_list


def horizontal_line_of_symmetary(lines: List[str]) -> int:
    previous_line = None
    current_line = None
    # Won't work if there are multiple sets of matching lines
    for idx, line in enumerate(lines):
        if current_line != None:
            previous_line = current_line
            current_line = line
        else:
            current_line = line
        
        if current_line == previous_line:
            # Represents the number of horizontal lines
            return idx
    return 0



if __name__ == "__main__":
    lines = read_text_file_to_lines("day13/example_horizontal.txt")
    total = 0
    total += (100 * horizontal_line_of_symmetary(lines))
    print(total)