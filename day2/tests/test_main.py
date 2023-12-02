from day2.main import get_game_score, minimum_set_of_cubes_in_game
from day2.round import Round


def test_get_game_score():
    assert get_game_score("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == 1
    assert get_game_score("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue") == 2
    assert get_game_score("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red") == 0
    assert get_game_score("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red") == 0
    assert get_game_score("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green") == 5

def test_minimum_set_of_cubes_in_game():
    minimum_set = minimum_set_of_cubes_in_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert minimum_set.red == 4
    assert minimum_set.green == 2
    assert minimum_set.blue == 6

    minimum_set = minimum_set_of_cubes_in_game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
    assert minimum_set.red == 1
    assert minimum_set.green == 3
    assert minimum_set.blue == 4

    minimum_set = minimum_set_of_cubes_in_game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
    assert minimum_set.red == 20
    assert minimum_set.green == 13
    assert minimum_set.blue == 6

    minimum_set = minimum_set_of_cubes_in_game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
    assert minimum_set.red == 14
    assert minimum_set.green == 3
    assert minimum_set.blue == 15

    minimum_set = minimum_set_of_cubes_in_game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
    assert minimum_set.red == 6
    assert minimum_set.green == 3
    assert minimum_set.blue == 2