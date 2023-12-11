


from typing import List, Tuple


def read_text_file_to_lines(filename: str) -> List[str]:
    my_file = open(filename, "r")
    data = my_file.read()
    data_to_list = data.splitlines()
    my_file.close()
    return data_to_list

def expand_universe(lines: List[str]) -> List[str]:
    empty_columns = [*range(len(lines[0]))]
    universe = []
    for i in range(len(lines[0])):
        for line in lines:
            if line[i] == '#':
                if i in empty_columns:
                    empty_columns.remove(i)
    new_lines = []
    empty_columns.sort()
    for line in lines:
        new_line = ""
        current_index = 0
        length = len(line)
        for column in empty_columns:
            if column < length:
                new_line += line[current_index:column] + line[column] + line[column]
            current_index = column+1
        new_line += line[current_index:]
        new_lines.append(new_line)
    for line in new_lines:
        if '#' in line:
            universe.append(line)
        else:
            universe.append(line)
            universe.append(line)
    return universe

def coordinates_of_galaxies(universe: List[str]) -> List[Tuple[int,int]]:
    galaxies = []
    for idy, line in enumerate(universe):
        for idx, char in enumerate(line):
            if char == '#':
                galaxies.append((idy, idx))
    return galaxies

def distances_between_all_galaxies_with_expansion(galaxies: List[Tuple[int,int]], empty_rows: List[int], empty_columns: List[int], expansion_rate: int) -> int:
    total_distance = 0
    for idy, g0_coordinates in enumerate(galaxies):
        for idx, g1_coordinates in enumerate(galaxies[idy:]):
            y_distance = abs(g0_coordinates[0] - g1_coordinates[0])
            x_distance = abs(g0_coordinates[1] - g1_coordinates[1])
            for row in empty_rows:
                if (g0_coordinates[0] < row and g1_coordinates[0] > row) or (g1_coordinates[0] < row and g0_coordinates[0] > row):
                    y_distance += expansion_rate - 1
            for column in empty_columns:
                if (g0_coordinates[1] < column and g1_coordinates[1] > column) or (g1_coordinates[1] < column and g0_coordinates[1] > column):
                    x_distance += expansion_rate - 1
            total_distance += x_distance + y_distance
    return total_distance

def distances_between_all_galaxies(galaxies: List[Tuple[int,int]]) -> int:
    total_distance = 0
    for idy, g0_coordinates in enumerate(galaxies):
        for idx, g1_coordinates in enumerate(galaxies[idy:]):
            total_distance += abs(g0_coordinates[0] - g1_coordinates[0]) + abs(g0_coordinates[1] - g1_coordinates[1])
    return total_distance

def get_empty_columns(lines: List[str]) -> list[int]:
    empty_columns = [*range(len(lines[0]))]
    for i in range(len(lines[0])):
        for line in lines:
            if line[i] == '#':
                if i in empty_columns:
                    empty_columns.remove(i)
    return empty_columns

def get_empty_rows(lines: List[str]) -> list[int]:
    empty_rows = []
    for idy, line in enumerate(lines):
        if '#' in line:
            continue
        else:
            empty_rows.append(idy)
    return empty_rows

if __name__ == "__main__":
    data = read_text_file_to_lines("day11\input.txt")
    empty_columns = get_empty_columns(data)
    print(empty_columns)
    empty_rows = get_empty_rows(data)
    print(empty_rows)
    galaxy_coordinates = coordinates_of_galaxies(data)
    distances = distances_between_all_galaxies_with_expansion(galaxy_coordinates, empty_rows, empty_columns, 1000000)
    print(distances)
    # universe = expand_universe(data)
    # galaxies = coordinates_of_galaxies(universe)
    # print(distances_between_all_galaxies(galaxies))
    # 15488166 Too low