from typing import List


def read_text_file_to_lines(filename: str) -> List[str]:
    my_file = open(filename, "r")
    data = my_file.read()
    data_to_list = data.splitlines()
    my_file.close()
    return data_to_list

def get_array_from_line(line: str) -> List[int]:
    return [int(x) for x in line.split()]

def next_value_in_sequence(sequence: List[int]) -> int:
    differences = []
    for i in range(len(sequence)-1):
        differences.append(sequence[i+1] -sequence[i])
    square_of_array = sum(map(square_of_number, differences))
    if square_of_array > 0:
        return sequence[len(sequence)-1] + next_value_in_sequence(differences)
    elif square_of_array == 0:
        return sequence[len(sequence)-1]
    
def previous_value_in_sequence(sequence: List[int]) -> int:
    differences = []
    for i in range(len(sequence) - 1):
        differences.append(sequence[i+1] - sequence[i])
    square_of_array = sum(map(square_of_number, differences))
    if square_of_array > 0:
        return sequence[0] - previous_value_in_sequence(differences)
    elif square_of_array == 0:
        return sequence[0]

def square_of_number(n: int) -> int:
    return n * n

if __name__ == "__main__":
    lines = read_text_file_to_lines("day9\input.txt")

    sum_of_extrapolated_values = 0
    for line in lines:
        data = get_array_from_line(line)
        sum_of_extrapolated_values += next_value_in_sequence(data)

    print("PART 1")
    print(sum_of_extrapolated_values)
    
    print("PART 2")
    sum_of_extrapolated_previous_values = 0
    for line in lines:
        data = get_array_from_line(line)
        sum_of_extrapolated_previous_values += previous_value_in_sequence(data)
    print(sum_of_extrapolated_previous_values)
