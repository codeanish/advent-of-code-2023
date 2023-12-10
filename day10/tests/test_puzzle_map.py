
from day10.puzzle_map import PuzzleMap


def test_create_puzzle_map():
    data = [".....",".S-7.",".|.|.",".L-J.","....."]
    puzzle_map = PuzzleMap(data)
    assert puzzle_map.get_value_at_coordinates(1,1) == 'S'
    assert puzzle_map.get_value_at_coordinates(0,0) == '.'
    assert puzzle_map.get_value_at_coordinates(3,4) == '.'
    assert puzzle_map.get_value_at_coordinates(3,3) == 'J'

def test_find_starting_coordinates():
    data = [".....",".S-7.",".|.|.",".L-J.","....."]
    puzzle_map = PuzzleMap(data)
    starting_coordinates = puzzle_map.get_starting_coordinates()
    assert starting_coordinates[0] == 1
    assert starting_coordinates[1] == 1

def test_get_adjoining_pipes():
    data = [".....",".S-7.",".|.|.",".L-J.","....."]
    puzzle_map = PuzzleMap(data)
    adjoining_pipes = puzzle_map.get_adjoining_pipes(1,1)
    expected_adjoining_pipes = [(1,2),(2,1)]
    for pipe in adjoining_pipes:
        assert pipe in expected_adjoining_pipes
