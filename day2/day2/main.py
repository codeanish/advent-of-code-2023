from typing import List
from round import Round, build_round

def get_game_score(game: str):
    split_game = game.split(":")
    rounds = split_game[1]
    split_rounds = rounds.split(';')
    for round in split_rounds:
        if not build_round(round.strip()).is_round_valid():
            return 0
    return int(split_game[0].split(' ')[1])

def minimum_set_of_cubes_in_game(game: str):
    split_game = game.split(":")
    rounds = split_game[1]
    split_rounds = rounds.split(';')
    red, green, blue = 0, 0, 0
    for round in split_rounds:
        my_round = build_round(round.strip())
        red = max(red, my_round.red)
        green = max(green, my_round.green)
        blue = max(blue, my_round.blue)
    return Round(red=red, green=green, blue=blue)

def read_text_file_to_lines(filename: str) -> List[str]:
    my_file = open(filename, "r")
    data = my_file.read()
    data_to_list = data.splitlines()
    my_file.close()
    return data_to_list

if __name__ == "__main__":
    games = read_text_file_to_lines("day2\input.txt")
    score = 0
    for game in games:
        min_set = minimum_set_of_cubes_in_game(game)
        score += min_set.red * min_set.green * min_set.blue
    print(score)
