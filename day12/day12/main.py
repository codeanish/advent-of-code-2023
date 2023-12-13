from multiprocessing import Pool
import os
from typing import List, Tuple
import itertools

def read_text_file_to_lines(filename: str) -> List[str]:
    my_file = open(filename, "r")
    data = my_file.read()
    data_to_list = data.splitlines()
    my_file.close()
    return data_to_list

def valid_solution(option: str, smallest_possible_solution: str) -> bool:
    if option == smallest_possible_solution:
        return True
    option_groupings = [a for a in option.split('.') if a]
    smallest_groupings = [a for a in smallest_possible_solution.split('.') if a]
    for idx, i in enumerate(smallest_groupings):
        if option_groupings[idx] != i:
            return False
    return True

def get_combinations_of_missing_indexes(missing_indexes: List[int], number_of_options: int) -> List[Tuple[int]]:
    return list(itertools.combinations(missing_indexes, number_of_options))

def number_of_combinations_of_arrangement(line: str) -> int:
    records = line.split()
    springs_representation = records[0]
    contiguous_groups_of_damaged_springs = [int(a) for a in records[1].split(',')]
    smallest_possible_solution = ""
    for damaged_springs in contiguous_groups_of_damaged_springs:
        smallest_possible_solution += damaged_springs * '#'
        smallest_possible_solution += '.'
    smallest_possible_solution = smallest_possible_solution[:-1]
    if len(smallest_possible_solution) == len(springs_representation):
        return 1

    matches = 0
    missing_pipes = sum(contiguous_groups_of_damaged_springs) - springs_representation.count('#')
    indexes_of_missing_values = []
    for idx, i in enumerate(springs_representation):
        if i == "?":
            indexes_of_missing_values.append(idx)

    pipe_index_options = get_combinations_of_missing_indexes(indexes_of_missing_values, missing_pipes)
    for option in pipe_index_options:
        test_spring_representation = springs_representation
        for i in range(missing_pipes):
            test_spring_representation = test_spring_representation[:option[i]] + '#' + test_spring_representation[option[i] + 1:]
        test_spring_representation = test_spring_representation.replace('?', '.')
        if valid_solution(test_spring_representation, smallest_possible_solution):
            matches += 1
    return matches


def transform_row_to_part_2_row(row: str):
    records = row.split()
    multiple = 5
    springs = records[0]
    part_2_springs = ""
    groups = records[1]
    part_2_groups = ""
    for i in range(multiple):
        if i < multiple - 1:
            part_2_springs += springs + "?"
            part_2_groups += groups + ","
        else:
            part_2_springs += springs
            part_2_groups += groups

    return f"{part_2_springs} {part_2_groups}"

cache = {}

def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in cfg else 1
    
    key = (cfg, nums)
    
    if key in cache:
        return cache[key]

    result = 0
    
    if cfg[0] in ".?":
        result += count(cfg[1:], nums)
        
    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            result += count(cfg[nums[0] + 1:], nums[1:])

    cache[key] = result
    return result

total = 0

for line in open("day12\input.txt"):
    cfg, nums = line.split()
    nums = tuple(map(int, nums.split(",")))
    
    cfg = "?".join([cfg] * 5)
    nums *= 5
    
    total += count(cfg, nums)

print(total)

# if __name__ == "__main__":

#     data = read_text_file_to_lines("day12\input.txt")
#     result = 0
#     part_2_data = [transform_row_to_part_2_row(row) for row in data]
#     print(data[0])
#     print("?".join([data[0].split()[0]] * 5))
#     print(part_2_data[0])
#     # [print(row) for row in part_2_data]
#     # print(part_2_data)
#     # for row in data:
#     #     part_2_row = transform_row_to_part_2_row(row)
#     #     result += number_of_combinations_of_arrangement(part_2_row)
    
#     # cpu_threads = os.cpu_count()
#     # pool = Pool(1)
#     # subset_results = []
#     # # print(data[:10])
#     # total_loops = len(part_2_data) // cpu_threads
#     # results = 0
#     # for i in range(total_loops + 1):
#     #     print(i)
#     #     subset = part_2_data[cpu_threads * i: cpu_threads * (i+1)]
#     #     subset_results.append(pool.map(number_of_combinations_of_arrangement, subset))
#     # for subset_result in subset_results:
#     #     results += sum(subset_result)
#     # print(results)
