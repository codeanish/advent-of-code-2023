
from day4.main import get_my_numbers, get_score_from_matching_numbers, get_total_cards, get_winning_numbers, get_winning_numbers_match


def test_get_winning_numbers_match():
    assert get_winning_numbers_match([1,2,3], [3,4,5]) == [3]
    assert get_winning_numbers_match([1,2,3], [4,5,6]) == []
    assert get_winning_numbers_match([1,2,3], [1,2,3]) == [1,2,3]

def test_get_winning_numbers_match_example():
    assert get_winning_numbers_match([41,48,83,86,17], [83,86,6,31,17,9,48,53]).sort() == [48,83,86,17].sort()

def test_get_score_from_matching_numbers():
    assert get_score_from_matching_numbers([48,83,86,17]) == 8

def test_get_winning_numbers():
    card = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    winning_numbers = get_winning_numbers(card)
    assert winning_numbers.sort() == [41,48,83,68,17].sort()

def test_get_my_numbers():
    card = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    my_numbers = get_my_numbers(card)
    assert my_numbers.sort() == [83,86,6,31,17,9,48,53].sort()

def test_get_total_cards():
    cards = []
    cards.append("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    cards.append("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19")
    cards.append("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1")
    cards.append("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83")
    cards.append("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36")
    cards.append("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")
    my_cards = {}
    for idx, card in enumerate(cards):
        winning_numbers = get_winning_numbers(card)
        my_numbers = get_my_numbers(card)
        matching_numbers = get_winning_numbers_match(winning_numbers, my_numbers)
        my_cards[idx + 1] = len(matching_numbers)
    assert get_total_cards(my_cards) == 30