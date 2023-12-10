from typing import List, Tuple

from puzzle_map import PuzzleMap

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

def read_text_file_to_lines(filename: str) -> List[str]:
    my_file = open(filename, "r")
    data = my_file.read()
    data_to_list = data.splitlines()
    my_file.close()
    return data_to_list


if __name__ == "__main__":
    data = read_text_file_to_lines("day10\input.txt")
    puzzle_map = PuzzleMap(data)
    # print(puzzle_map.get_adjoining_pipes(77,34))
    # starting_coordinates = puzzle_map.get_starting_coordinates()
    loop = puzzle_map.get_loop()
    # find a point on an edge of the loop, then traverse the loop, 
    # points to one side of the line are not included, points to the other side of the line are included
    contained_points = 0
    # Replace all points not on loop with '.'
    for idy, line in enumerate(puzzle_map.matrix):
        for idx, point in enumerate(line):
            if (idx, idy) not in loop:
                puzzle_map.matrix[idy][idx] = '.'
    for idy, line in enumerate(puzzle_map.matrix):
        for idx, point in enumerate(line):
            if puzzle_map.odd_pipe_crossings((idx, idy)):
                # print((idx,idy))
                if (idx,idy) not in loop:        
                    contained_points += 1
    
    print(contained_points)
    # print(loop)

    # northernmost_points = []
    # for point in loop:
    #     if len(northernmost_points) == 0:
    #         northernmost_points.append(point)
    #         continue
    #     if point[1] < northernmost_points[0][1]:
    #         northernmost_points = [point]
    #     if point[1] == northernmost_points[0][1]:
    #         northernmost_points.append(point)
    # starting_point = northernmost_points[0]
    # for point in northernmost_points:
    #     if point[0] < starting_point[0]:
    #         starting_point = point
    # # print(northernmost_points)
    # print(starting_point)
    # adjoining_points = puzzle_map.get_adjoining_pipes(starting_point[0], starting_point[1])
    # # next point = point where x(new) = x+1
    # print(adjoining_points)
    # current_point = None
    # if adjoining_points[0][0] > starting_point[0]:
    #     current_point = adjoining_points[0]
    # else:
    #     current_point = adjoining_points[1]
    # previous_point = starting_point
    # previous_points = [starting_point]
    # while current_point[0] != starting_point[0] or current_point[1] != starting_point[1]:
    #     print(current_point)
    #     next_point = puzzle_map.get_next_point(current_point, previous_point)
    #     previous_point = current_point
    #     current_point = next_point
        

    # loop.append(starting_coordinates)
    # x = []
    # y = []
    # for item in loop:
    #     x.append(item[0])
    #     y.append(item[1])
    # x_np = np.array(x)
    # y_np = np.array(y)
    # fig, ax = plt.subplots()
    # ax.plot(x_np, y_np, linewidth=2.0)
    # plt.show()
    # print(loop)
    