import math
from typing import List

# Calculate a quadratic equation for the function produced by the time
# y = a(x-b)(x-c)
# b = x_low
# c = x_high

# Substitute in x_low and x_high
# y = a(x)(x-total_time)

# Substitute in x_1
# total_time - 1 = a(1)(1-total_time)
# total_time - 1 = a(1-total_time)
# a = (total_time -1)/(1-total_time)

# Substitute in a
# y = [(total_time-1)/(1-total_time)] * (x)(x-total_time)

# Solve for intercepts distance
# distance = [(total_time-1)/(1-total_time)] * (x)*(x-total_time)
# distance = -x^2 + x*total_time


# x(x-total_time) = distance / [(total_time-1)/(1-total_time)]
# x^2 - x*total_time = distance / [(total_time-1)/(1-total_time)]
# x^2 - 7x = 9 / [6/-6]
# x^2 - 7x = -9/6
# x^2 - 7x + 9/6 = 0
def get_different_ways_you_can_win(total_time: int, distance: int) -> int:
    # distance = -x^2 + x*total_time
    # ax^2 + bx + c = 0
    # (-b +- sqrt(b^2 -4ac)) / 2a
    # a = -1
    # b = total_time
    # c = distance
    low_intercept = (total_time - ((total_time ** 2) - 4 * distance)**0.5)/2
    high_intercept = (total_time + ((total_time ** 2) - 4 * distance)**0.5)/2
    return (int(high_intercept-1) if high_intercept.is_integer() else math.floor(high_intercept)) + 1 - (int(low_intercept + 1) if low_intercept.is_integer() else math.ceil(low_intercept))


def read_text_file_to_lines(filename: str) -> List[str]:
    my_file = open(filename, "r")
    data = my_file.read()
    data_to_list = data.splitlines()
    my_file.close()
    return data_to_list

if __name__ == "__main__":
    data = read_text_file_to_lines('day6\input.txt')

    times = data[0].split(':')[1].strip().split()
    distances = data[1].split(':')[1].strip().split()
    inputs = []
    for idx, x in enumerate(times):
        inputs.append((int(x), int(distances[idx])))

    # # PART 1
    print("************** PART 1 **************")
    results = []
    for input in inputs:
        results.append(get_different_ways_you_can_win(input[0], input[1]))
    print(math.prod(results))
    
    # # PART 2
    print("************** PART 2 **************")
    time = ''
    distance = ''
    for idx, x in enumerate(times):
        time += x
        distance += distances[idx]
    print(get_different_ways_you_can_win(int(time), int(distance)))