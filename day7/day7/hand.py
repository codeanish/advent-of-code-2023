class Hand:
    def __init__(self, hand: str) -> None:
        self.hand = hand

    def __repr__(self) -> str:
        return self.hand

    card_values_part1 = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }

    card_values = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 1,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }

    # five_of_a_kind      = 50000000000 # len 1
    # four_of_a_kind      = 4000000000 # len 2
    # full_house          = 250000000 # len 2
    # three_of_a_kind     = 15000000 # len 3
    # two_pair            = 1000000 # len 3
    # one_pair            = 100000 # len 4
    # high_card           = 1 # len 5

    five_of_a_kind      = 6000000 # len 1
    four_of_a_kind      = 5000000 # len 2
    full_house          = 4000000 # len 2
    three_of_a_kind     = 3000000 # len 3
    two_pair            = 2000000 # len 3
    one_pair            = 1000000 # len 4
    high_card           = 0 # len 5
    
    def value(self) -> int:
        my_cards = {}
        for card in self.card_values:
            if card in self.hand:
                my_cards[card] = self.hand.count(card)
        score = 0        
        multiplier = 0

        if len(my_cards) == 1:
            multiplier = self.five_of_a_kind
        elif len(my_cards) == 2:
            card_list = list(my_cards)
            first_card = card_list[0]
            if my_cards[first_card] == 2 or my_cards[first_card] == 3:
                if my_cards.get('J'):
                    multiplier = self.five_of_a_kind
                else:
                    multiplier = self.full_house
            else:
                if my_cards.get('J'):
                    multiplier = self.five_of_a_kind
                else:
                    multiplier = self.four_of_a_kind
        elif len(my_cards) == 3:
            for card in my_cards:
                if my_cards[card] == 3:
                    if my_cards.get('J'):
                        multiplier = self.four_of_a_kind
                    else:
                        multiplier = self.three_of_a_kind
                    break
                if my_cards[card] == 2:
                    jacks = my_cards.get('J')
                    if jacks == 1:
                        multiplier = self.full_house
                    elif jacks == 2:
                        multiplier = self.four_of_a_kind
                    else:
                        multiplier = self.two_pair
                    break
        elif len(my_cards) == 4:
            for card in my_cards:
                if my_cards[card] == 2:
                    if my_cards.get('J'):
                        multiplier = self.three_of_a_kind
                    else:
                        multiplier = self.one_pair
        else:
            if my_cards.get('J'):
                multiplier = self.one_pair
            else:
                multiplier = self.high_card

        for i in range(5):
            # The reason for the * 20 is to be more than the highest card value
            # first position * 10000, 1000, 100, 10, 1
            score += 15**(4-i) * self.card_values[self.hand[i]]
        score += multiplier
        return score

