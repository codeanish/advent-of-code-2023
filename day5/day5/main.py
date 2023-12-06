
from typing import List
from mapping import Mapping
from multiprocessing import Pool
import os


def get_destination(source_number: int, mappings: List[Mapping]) -> int:
    # mappings will  be sorted, so can use binary search through the list
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

def get_ultimate_destination_with_map(seed: int, maps: List[List[Mapping]]) -> int:
    location = seed
    for mapping in maps:
        # change to binary search here
        for m in mapping:
            if location in range(m.source, m.end_range):
                location = m.destination + location - m.source
                break
    return location
        

class MapData:
    def __init__(self, first_seed: int, last_seed: int, maps: List[List[Mapping]]) -> None:
        self.first_seed = first_seed
        self.last_seed = last_seed
        self.maps = maps

def process_map_data(map_data: MapData) -> int:
    seed_location = {}
    i = 0
    for seed in range(map_data.first_seed, map_data.last_seed):
        if i % 1000000 == 0:
            print(i)
        seed_location[seed] = get_ultimate_destination_with_map(seed, map_data.maps)
        i +=1
    lowest_location = None
    for k, v in seed_location.items():
        if lowest_location is None:
            lowest_location = v
        if v < lowest_location:
            lowest_location = v
    return lowest_location

if __name__ == "__main__":
    lines = read_text_file_to_lines("day5\input.txt")
    seeds_line = lines[0]
    seeds = [int(n) for n in seeds_line.split(':')[1].strip().split()]

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

    seeds_to_soil_map.sort(key=lambda x: x.source),
    soil_to_fertilizer_map.sort(key=lambda x: x.source),
    fertilizer_to_water_map.sort(key=lambda x: x.source),
    water_to_light_map.sort(key=lambda x: x.source),
    light_to_temperature_map.sort(key=lambda x: x.source),
    temperature_to_humidity_map.sort(key=lambda x: x.source),
    humidity_to_location_map.sort(key=lambda x: x.source)

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
    
    # PART 1
    # for seed in seeds:
    #     seed_location[seed] = get_ultimate_destination(seed, maps)
    
    # PART 2

    pairs = list(zip(seeds[::2], seeds[1::2]))
    map_data = []
    cpu_threads = os.cpu_count()
    smallest_seed = 432563865
    largest_seed = 7719412738
    interval = (largest_seed - smallest_seed) // cpu_threads +1
    for i in range(cpu_threads):
        map_data.append(MapData(smallest_seed + interval * i, smallest_seed + interval * (i+1), maps))

    pool = Pool(cpu_threads)
    results = pool.map(process_map_data, map_data)
    print(min(results))