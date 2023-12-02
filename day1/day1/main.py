
from typing import List

def sum_of_calibration_values(lines: List[str]) -> int:
    sum = 0
    for line in lines:
        sum += get_calibration_value(line)
    return sum

def read_text_file_to_lines(filename: str) -> List[str]:
    my_file = open(filename, "r")
    data = my_file.read()
    data_to_list = data.splitlines()
    my_file.close()
    return data_to_list

TEXT_TO_NUMBERS = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

def get_calibration_value(line: str) -> int:
    left, right = None, None
    left_buffer, right_buffer = "", ""
    length = len(line)
    for i in range(0, length):
        if left is not None and right is not None:
            break
        if left is None:
            if line[i].isdecimal():
                left = line[i]
            else:
                left_buffer += line[i]
            if left_buffer in TEXT_TO_NUMBERS:
                left = str(TEXT_TO_NUMBERS[left_buffer])
            elif left_buffer[1:] in TEXT_TO_NUMBERS:
                left = str(TEXT_TO_NUMBERS[left_buffer[1:]])
            elif left_buffer[2:] in TEXT_TO_NUMBERS:
                left = str(TEXT_TO_NUMBERS[left_buffer[2:]])
            if len(left_buffer) == 5:
                left_buffer = left_buffer[1:]
        if right is None:
            if line[length - i - 1].isdecimal():
                right = line[length - i - 1]
            else:
                right_buffer = line[length - i - 1] + right_buffer
            if right_buffer in TEXT_TO_NUMBERS:
                right = str(TEXT_TO_NUMBERS[right_buffer])
            elif right_buffer[:-1] in TEXT_TO_NUMBERS:
                right = str(TEXT_TO_NUMBERS[right_buffer[:-1]])
            elif right_buffer[:-2] in TEXT_TO_NUMBERS:
                right = str(TEXT_TO_NUMBERS[right_buffer[:-2]])
            if len(right_buffer) == 5:
                right_buffer = right_buffer[:-1]
    if left is None or right is None:
        return 0
    return int(left + right)


if __name__ == "__main__":
    # print(get_calibration_value("twonexxxtwone"))
    lines = read_text_file_to_lines("day1\input.txt")
    print(sum_of_calibration_values(lines))
    # print(replace_text_numbers_with_digits("twonexxxtwone"))
    # print(replace_text_numbers_with_digits("xtwon"))
