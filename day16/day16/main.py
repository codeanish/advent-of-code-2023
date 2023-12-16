from typing import  Optional

from direction import Direction

def read_text_file_to_lines(filename: str) -> list[str]:
    my_file = open(filename, "r")
    data = my_file.read()
    data_to_list = data.splitlines()
    my_file.close()
    return data_to_list


def get_next_coordinates(current_coordinates: tuple[int,int], x_length: int, y_length: int, direction: Direction) -> Optional[tuple[int,int]]:
    if direction == Direction.RIGHT:
        if current_coordinates[0] + 1 < x_length:
            return (current_coordinates[0] + 1, current_coordinates[1])
    elif direction == Direction.LEFT:
        if current_coordinates[0] - 1 >= 0:
            return (current_coordinates[0] - 1,current_coordinates[1])
    elif direction == Direction.UP:
        if current_coordinates[1] - 1 >= 0:
            return (current_coordinates[0], current_coordinates[1] - 1)
    elif direction == Direction.DOWN:
        if current_coordinates[1] + 1 < y_length:
            return (current_coordinates[0], current_coordinates[1] + 1)
    return None

completed_routes: list[tuple[tuple[int,int], Direction]] = []

def beam_route(grid: list[str], current_coordinates: tuple[int,int], direction: Direction) -> list[tuple[int,int]]:
    x_length = len(grid[0])
    y_length = len(grid)
    
    # If coordinates + direction already exist in route, don't bother looking again
    route: list[tuple[int,int]] = []

    while current_coordinates != None:
        route.append(current_coordinates)
        current_value = grid[current_coordinates[1]][current_coordinates[0]]
        if current_value == "|" and (direction == Direction.RIGHT or direction == Direction.LEFT) :
            if current_coordinates[1] - 1 >= 0:
                next_coordinates = (current_coordinates[0],current_coordinates[1] -1)
                if (next_coordinates, Direction.UP) not in completed_routes:
                    completed_routes.append((next_coordinates, Direction.UP))
                    route = route + beam_route(grid, next_coordinates, Direction.UP)
                else:
                    break
            if current_coordinates[1] + 1 < y_length:
                next_coordinates = (current_coordinates[0],current_coordinates[1] + 1)
                if (next_coordinates, Direction.DOWN) not in completed_routes:
                    completed_routes.append((next_coordinates, Direction.DOWN))
                    route = route + beam_route(grid, next_coordinates, Direction.DOWN)
                else:
                    break
            break
        elif current_value == "\\":
            if direction == Direction.RIGHT:
                direction = Direction.DOWN
            elif direction == Direction.LEFT:
                direction = Direction.UP
            elif direction == Direction.UP:
                direction = Direction.LEFT
            elif direction == Direction.DOWN:
                direction = Direction.RIGHT
        elif current_value == "/":
            if direction == Direction.RIGHT:
                direction = Direction.UP
            elif direction == Direction.LEFT:
                direction = Direction.DOWN
            elif direction == Direction.UP:
                direction = Direction.RIGHT
            elif direction == Direction.DOWN:
                direction = Direction.LEFT
        elif current_value == "-" and (direction == Direction.UP or direction == Direction.DOWN):
            if current_coordinates[0] - 1 >= 0:
                next_coordinates = (current_coordinates[0] - 1, current_coordinates[1])
                if (next_coordinates, Direction.LEFT) not in completed_routes:
                    completed_routes.append((next_coordinates, Direction.LEFT))
                    route = route + beam_route(grid, next_coordinates, Direction.LEFT)
                else:
                    break
            if current_coordinates[0] + 1 < x_length:
                next_coordinates = (current_coordinates[0] + 1, current_coordinates[1])
                if (next_coordinates, Direction.RIGHT) not in completed_routes:
                    completed_routes.append((next_coordinates, Direction.RIGHT))
                    route = route + beam_route(grid, next_coordinates, Direction.RIGHT)
                else:
                    break
            break
        current_coordinates = get_next_coordinates(current_coordinates, x_length, y_length, direction)
    

    return route

if __name__ == "__main__":
    lines = read_text_file_to_lines("day16/input.txt")
    x_length = len(lines[0])
    y_length = len(lines)
    
    starting_coordinates = (0,0)
    completed_routes.append((starting_coordinates, Direction.RIGHT))
    max_route = 0

    for x in range(x_length):
        starting_coordinates = (x,0)
        completed_routes = []
        completed_routes.append((starting_coordinates, Direction.DOWN))
        route = len(set(beam_route(lines, starting_coordinates, Direction.DOWN)))
        if route > max_route:
            max_route = route

    for x in range(x_length):
        starting_coordinates = (x, y_length - 1)
        completed_routes = []
        completed_routes.append((starting_coordinates, Direction.UP))
        route = len(set(beam_route(lines, starting_coordinates, Direction.UP)))
        if route > max_route:
            max_route = route

    for y in range(y_length):
        starting_coordinates = (0, y)
        completed_routes = []
        completed_routes.append((starting_coordinates, Direction.RIGHT))
        route = len(set(beam_route(lines, starting_coordinates, Direction.RIGHT)))
        if route > max_route:
            max_route = route

    for y in range(y_length):
        starting_coordinates = (x_length - 1, y)
        completed_routes = []
        completed_routes.append((starting_coordinates, Direction.LEFT))
        route = len(set(beam_route(lines, starting_coordinates, Direction.LEFT)))
        if route > max_route:
            max_route = route
    
    print(max_route)

    # for y in range(y_length):
    #     for x in range(x_length):
    #         if (x,y) in route:
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    #     print()
    # print(route)
    # print(len(set(route)))
    # print(set(route))
    # print(len(set(route)))

    # for line in lines:
    #     print(line)