
from typing import List
import numpy

SYMBOLS = {'*', '#', '+', '$', '@', '%', '-', '=', '/', '&'}
GEAR_COGS = {'*'}

def find_part_numbers(engine_schematic: List[str]) -> List[int]:
    part_numbers = []
    for idx_y, y in enumerate(engine_schematic):
        current_number = ""
        first_x_idx = None
        last_x_idx = None
        for idx_x, x in enumerate(y):
            if x.isdigit():
                if first_x_idx is None:
                    first_x_idx = idx_x
                current_number += x
            elif len(current_number) > 0:
                last_x_idx = idx_x - 1
                if any_adjacent_symbols(idx_y, first_x_idx, last_x_idx, engine_schematic, SYMBOLS):
                    part_numbers.append(int(current_number))                
                current_number = ""
                first_x_idx, last_x_idx = None, None
        if current_number:
            if any_adjacent_symbols(idx_y, first_x_idx, len(y) -1, engine_schematic, SYMBOLS):
                part_numbers.append(int(current_number))
    return part_numbers

def find_gear_ratios(engine_schematic: List[str]) -> List[int]:
    gear_ratios = {}
    for idx_y, y in enumerate(engine_schematic):
        current_number = ""
        first_x_idx = None
        last_x_idx = None
        for idx_x, x in enumerate(y):
            if x.isdigit():
                if first_x_idx is None:
                    first_x_idx = idx_x
                current_number += x
            elif len(current_number) > 0:
                last_x_idx = idx_x - 1
                cog = any_adjacent_symbols(idx_y, first_x_idx, last_x_idx, engine_schematic, GEAR_COGS)
                if cog:
                    if gear_ratios.get(cog):
                        gear_ratios[cog] += [int(current_number)]
                    else:
                        gear_ratios[cog] = [int(current_number)]
                current_number = ""
                first_x_idx, last_x_idx = None, None
        if current_number:
            cog = any_adjacent_symbols(idx_y, first_x_idx, len(y) -1, engine_schematic, GEAR_COGS)
            if cog:
                if gear_ratios.get(cog):
                    gear_ratios[cog] += [int(current_number)]
                else:
                    gear_ratios[cog] = [int(current_number)]
    return gear_ratios

def any_adjacent_symbols(y_idx: int, first_x_idx: int, last_x_idx: int, engine_schematic: List[str], symbols: set) -> tuple[int,int]:
    if y_idx - 1 >= 0:
        previous_line = engine_schematic[y_idx - 1]
        for x in range(max(first_x_idx-1,0), min(last_x_idx + 2, len(previous_line))):
            if previous_line[x] in symbols:
                return (y_idx-1, x)

    current_line = engine_schematic[y_idx]
    if current_line[max(first_x_idx -1, 0)] in symbols:
        return (y_idx, max(first_x_idx -1, 0))
    if current_line[min(last_x_idx + 1, len(current_line) - 1)] in symbols:
        return (y_idx, min(last_x_idx + 1, len(current_line) - 1))
    
    if len(engine_schematic) > y_idx + 1:
        next_line = engine_schematic[y_idx + 1]
        for x in range(max(first_x_idx-1,0), min(last_x_idx + 2, len(next_line))):
            if next_line[x] in symbols:
                return (y_idx + 1, x)
    return None

def read_text_file_to_lines(filename: str) -> List[str]:
    my_file = open(filename, "r")
    data = my_file.read()
    data_to_list = data.splitlines()
    my_file.close()
    return data_to_list

if __name__ == "__main__":
    engine_schematic = read_text_file_to_lines("day3\input.txt")
    gear_ratios = find_gear_ratios(engine_schematic)
    sum = 0
    for gear_ratio in gear_ratios:
        if len(gear_ratios[gear_ratio]) == 2:
            sum += numpy.prod(gear_ratios[gear_ratio])
    print(sum)
