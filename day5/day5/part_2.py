with open("day5\input.txt", "r") as file:
    data = file.readlines()

seeds = [int(i) for i in data[0].strip().split(": ")[1].split(" ")]
mappings = []
for line in data[2:]:
    line = line.strip()
    if line.endswith(":"):
        # Create new mapping
        mappings.append([])
    elif len(line) > 0:
        # Add mapping line to the previous mapping
        mappings[-1].append([int(i) for i in line.split(" ")])

res = 2**64
for start_of_range, length_of_range in zip(seeds[::2], seeds[1::2]):
    ranges = [(start_of_range, start_of_range + length_of_range - 1)]
    # Iterate through the different mappings in order
    for typemappings in mappings:
        newranges = []
        for low, high in ranges:
            found = False
            for map_destination, map_source, map_range in typemappings:
                if low >= map_source and high < map_source + map_range:
                    newranges.append((low - map_source + map_destination, high - map_source + map_destination))
                    found = True
                elif low < map_source and high >= map_source and high < map_source + map_range:
                    ranges.append((low, map_source - 1))
                    newranges.append((map_destination, map_destination + high - map_source))
                    found = True
                elif low < map_source + map_range and high >= map_source + map_range and low >= map_source:
                    ranges.append((map_source + map_range, high))
                    newranges.append((map_destination + low - map_source, map_destination + map_range - 1))
                    found = True
                elif low < map_source and high >= map_source + map_range:
                    ranges.append((low, map_source - 1))
                    newranges.append((map_destination, map_destination + map_range - 1))
                    ranges.append((map_source + map_range, high))
                    found = True
                if found == True:
                    break
            if found == False:
                newranges.append((low, high))
        ranges = newranges.copy()
    res = min(res, min(ranges)[0])
print(res)