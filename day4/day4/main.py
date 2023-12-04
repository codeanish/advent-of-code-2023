
from typing import List


def get_winning_numbers_match(winning_numbers: List[int], my_numbers: List[int]) -> List[int]:
    winning_set = set(winning_numbers)
    my_numbers_set = set(my_numbers)
    return list(winning_set & my_numbers_set)

def get_score_from_matching_numbers(matching_numbers: List[int]) -> int:
    score = 0
    for i in matching_numbers:
        if score == 0:
            score += 1
        else:
            score *= 2
    return score

def read_text_file_to_lines(filename: str) -> List[str]:
    my_file = open(filename, "r")
    data = my_file.read()
    data_to_list = data.splitlines()
    my_file.close()
    return data_to_list

def get_winning_numbers(card: str) -> List[int]:
    numbers = card.split(':')[1]
    winning_numbers = numbers.split('|')[0].strip().split()
    return winning_numbers

def get_my_numbers(card: str) -> List[int]:
    numbers = card.split(':')[1]
    my_numbers = numbers.split('|')[1].strip().split()
    return my_numbers

def get_total_cards(cards: dict[int,int]) -> int:
    my_cards = {k: 1 for k,v in cards.items()}
    for key in cards:
        matches = cards[key]
        for i in range(0, matches):
            my_cards[key + 1 + i] += 1 * my_cards[key]
    return sum(my_cards.values())
    

if __name__ == "__main__":
    cards = read_text_file_to_lines("day4\input.txt")
    my_cards = {}
    for idx, card in enumerate(cards):
        winning_numbers = get_winning_numbers(card)
        my_numbers = get_my_numbers(card)
        matching_numbers = get_winning_numbers_match(winning_numbers, my_numbers)
        my_cards[idx + 1] = len(matching_numbers)

    print(get_total_cards(my_cards))