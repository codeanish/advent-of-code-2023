from day3.main import find_part_numbers

def test_find_part_numbers_no_parts_one_line():
    part_numbers = find_part_numbers(["123....456"])
    assert len(part_numbers) == 0

def test_find_part_numbers_one_value():
    part_numbers = find_part_numbers(["123*"])
    assert len(part_numbers) == 1
    assert part_numbers[0] == 123

def test_find_part_numbers_one_line():
    part_numbers = find_part_numbers(["123.456*"])
    assert len(part_numbers) == 1
    assert part_numbers[0] == 456

def test_find_part_numbers_two_lines_symbol_below():
    part_numbers = find_part_numbers(["123.", "...*"])
    assert len(part_numbers) == 1
    assert part_numbers[0] == 123

def test_find_part_numbers_two_lines_symbol_above():
    part_numbers = find_part_numbers(["...*", "123."])
    assert len(part_numbers) == 1
    assert part_numbers[0] == 123

def test_find_part_numbers_sample_input():
    sample_input = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    ]
    part_numbers = find_part_numbers(sample_input)
    assert len(part_numbers) == 8

def test_find_part_numbers_first_few_lines():
    sample_input = [
        "...........441.................367................296........................................567..47.....45.................947.............",
        "...606..........888.....................508..........*892................+..=138.381..967...............*....%......926...........218.......",
        "....*......116..*..............747............-....................777..460..........*.......549......127...595.......*..290........*.968..."
    ]
    answer = [296,45,606,888,892,138,967,926,218,460,127,595]
    part_numbers = find_part_numbers(sample_input)
    assert len(part_numbers) == len(answer)
    assert sum(part_numbers) == sum(answer)

def test_find_part_numbers_edge_case_1():
    sample_input = [
        "862*766......@...545.......*4............706.....................................887.395....=.731......47.........................942.949..."
    ]
    answer = [862,766,4]
    part_numbers = find_part_numbers(sample_input)
    assert len(part_numbers) == len(answer)
    assert sum(part_numbers) == sum(answer)

def test_find_part_numbers_edge_case_2():
    sample_input = [
        ".=806"
    ]
    answer = [806]
    part_numbers = find_part_numbers(sample_input)
    assert len(answer) == len(part_numbers)
    assert sum(answer) == sum(part_numbers)