
from typing import List
from mapping import Mapping
from multiprocessing import Pool
import os


def get_destination(source_number: int, mappings: List[Mapping]) -> int:
    for mapping in mappings:
        if source_number in range(mapping.source, mapping.source + mapping.range):
            return mapping.destination + source_number - mapping.source
    return source_number

def get_ultimate_destination(source_number: int, mappings: List[List[Mapping]]) -> int:
    destination_number = source_number
    for mapping in mappings:
        destination_number = get_destination(destination_number, mapping)
    return destination_number

def read_text_file_to_lines(filename: str) -> List[str]:
    my_file = open(filename, "r")
    data = my_file.read()
    data_to_list = data.splitlines()
    my_file.close()
    return data_to_list

if __name__ == "__main__":
    lines = read_text_file_to_lines("day5\input.txt")
    seeds_line = lines[0]
    # print(seeds_line)
    seeds = [int(n) for n in seeds_line.split(':')[1].strip().split()]

    # print(seeds)
    seeds_to_soil_block = False
    soil_to_fertilizer_block = False
    fertilizer_to_water_block = False
    water_to_light_block = False
    light_to_temperature_block = False
    temperature_to_humidity_block = False
    humidity_to_location_block = False
    seeds_to_soil_map = []
    soil_to_fertilizer_map = []
    fertilizer_to_water_map = []
    water_to_light_map = []
    light_to_temperature_map = []
    temperature_to_humidity_map = []
    humidity_to_location_map = []
    for line in lines:
        if line == "seed-to-soil map:":
            seeds_to_soil_block = True
        elif line == "soil-to-fertilizer map:":
            soil_to_fertilizer_block = True
        elif "fertilizer-to-water" in line:
            fertilizer_to_water_block = True
        elif "water-to-light" in line:
            water_to_light_block = True
        elif "light-to-temperature" in line:
            light_to_temperature_block = True
        elif "temperature-to-humidity" in line:
            temperature_to_humidity_block = True
        elif "humidity-to-location" in line:
            humidity_to_location_block = True
        elif len(line) == 0:
            seeds_to_soil_block = False
            soil_to_fertilizer_block = False
            fertilizer_to_water_block = False
            water_to_light_block = False
            light_to_temperature_block = False
            temperature_to_humidity_block = False
            humidity_to_location_block = False
        else:
            values = line.split()
            if seeds_to_soil_block:
                seeds_to_soil_map.append(Mapping(int(values[0]), int(values[1]), int(values[2])))
            elif soil_to_fertilizer_block:
                soil_to_fertilizer_map.append(Mapping(int(values[0]), int(values[1]), int(values[2])))
            elif fertilizer_to_water_block:
                fertilizer_to_water_map.append(Mapping(int(values[0]), int(values[1]), int(values[2])))
            elif water_to_light_block:
                water_to_light_map.append(Mapping(int(values[0]), int(values[1]), int(values[2])))
            elif light_to_temperature_block:
                light_to_temperature_map.append(Mapping(int(values[0]), int(values[1]), int(values[2])))
            elif temperature_to_humidity_block:
                temperature_to_humidity_map.append(Mapping(int(values[0]), int(values[1]), int(values[2])))
            elif humidity_to_location_block:
                humidity_to_location_map.append(Mapping(int(values[0]), int(values[1]), int(values[2])))

    maps = [
        seeds_to_soil_map,
        soil_to_fertilizer_map,
        fertilizer_to_water_map,
        water_to_light_map,
        light_to_temperature_map,
        temperature_to_humidity_map,
        humidity_to_location_map
        ]
    seed_location = {}
    

    cpu_count = os.cpu_count()
    pool = Pool(cpu_count)

    # PART 1
    for seed in seeds:
        seed_location[seed] = get_ultimate_destination(seed, maps)
    
    # PART 2

    pairs = list(zip(seeds[::2], seeds[1::2]))
    print(pairs)
    # for pair in pairs:
    #     for seed in range(pair[0], pair[0] + pair[1]):
    #         seed_location[seed] = get_ultimate_destination(seed, maps)

    lowest_location = None
    for k, v in seed_location.items():
        if lowest_location is None:
            lowest_location = v
        if v < lowest_location:
            lowest_location = v
    print(lowest_location)