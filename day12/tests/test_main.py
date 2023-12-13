from day12.main import number_of_combinations_of_arrangement, valid_solution, get_combinations_of_missing_indexes
import itertools

def test_number_of_combinations_of_arrangement():
    assert number_of_combinations_of_arrangement("???.### 1,1,3") == 1
    assert number_of_combinations_of_arrangement(".??..??...?##. 1,1,3") == 4
    assert number_of_combinations_of_arrangement("?#?#?#?#?#?#?#? 1,3,1,6") == 1
    assert number_of_combinations_of_arrangement("????.#...#... 4,1,1") == 1
    assert number_of_combinations_of_arrangement("????.######..#####. 1,6,5") == 4
    assert number_of_combinations_of_arrangement("?###???????? 3,2,1") == 10


def test_valid_solution():
    assert valid_solution(".##.#.......##.", "#.#.###") == False #1
    assert valid_solution(".##..#......##.", "#.#.###") == False #2
    assert valid_solution(".##........###.", "#.#.###") == False #3
    assert valid_solution(".#..##......##.", "#.#.###") == False #4
    assert valid_solution(".#..#......###.", "#.#.###") == True #5
    assert valid_solution(".#...#.....###.", "#.#.###") == True #6
    assert valid_solution("..#.##......##.", "#.#.###") == False #7
    assert valid_solution("..#.#......###.", "#.#.###") == True #8
    assert valid_solution("..#..#.....###.", "#.#.###") == True #9
    assert valid_solution("....##.....###.", "#.#.###") == False #10

def test_get_combinations_of_missing_indexes():
    items = get_combinations_of_missing_indexes([1,2,5,6,10], 3)
    assert len(list(items)) == 10