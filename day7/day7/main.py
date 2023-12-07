from typing import List, Tuple

from hand import Hand


def read_text_file_to_lines(filename: str) -> List[str]:
    my_file = open(filename, "r")
    data = my_file.read()
    data_to_list = data.splitlines()
    my_file.close()
    return data_to_list

def get_rounds(lines : List[str]):
    rounds = []
    for line in lines:
        values = line.split()
        rounds.append((Hand(values[0]),values[1]))
    return rounds

def quick_sort(rounds: List[Tuple[Hand,int]]) -> List[Tuple[Hand,int]]:
    if len(rounds) <= 1:
        return rounds
    # Takes the last value from the array and removes it from the array
    pivot_value = rounds.pop()
    left_elements = []
    right_elements = []
    for round in rounds:
        if round[0].value() <= pivot_value[0].value():
            left_elements.append(round)
        else:
            right_elements.append(round)
    return quick_sort(left_elements) + [pivot_value] + quick_sort(right_elements)

if __name__ == "__main__":
    data = read_text_file_to_lines("day7\input.txt")
    rounds = get_rounds(data)
    sorted_rounds = quick_sort(rounds)
    # for round in sorted_rounds:
    #     print(round)
    score = 0
    for idx, round in enumerate(sorted_rounds):
        # print(f"Hand = {round[0]}, Bet = {round[1]}")
        score += (idx + 1) * int(round[1])
    print(score)
    h2 = Hand("QQQQ2")
    # # h4 = Hand("K5KKK")
    h1 = Hand("JKKK2")
    # # h3 = Hand("K2KKK")
    # # # print(h1.value())
    print(f"h1 {h1} = {h1.value()}")
    print(f"h2 {h2} = {h2.value()}")
    # print(f"h3 = {h3.value()}")
    # print(f"h4 = {h4.value()}")
    
    # 251038998 Too low
    # 251058093
    # 251153507 Too high

    # Part 2 249723387 Too Low
    # Part 2 249781879