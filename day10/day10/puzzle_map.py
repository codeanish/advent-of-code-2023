from typing import List, Tuple


class PuzzleMap:
    def __init__(self, input: List[str]) -> None:
        data = []
        for line in input:
            line_array = []
            for char in line:
                line_array.append(char)
            data.append(line_array)
        self.matrix = data

    def get_value_at_coordinates(self, x: int, y: int) -> str:
        return self.matrix[y][x]
    
    def get_starting_coordinates(self) -> Tuple[int,int]:
        for idy, line in enumerate(self.matrix):
            for idx, column in enumerate(line):
                if column == 'S':
                    return (idx,idy)

    def get_loop(self) -> List[Tuple[int,int]]:
        starting_coordinates = self.get_starting_coordinates()
        adjoining_pipes = self.get_adjoining_pipes(starting_coordinates[0], starting_coordinates[1])
        s_type = self.what_is_s(adjoining_pipes)
        self.matrix[starting_coordinates[1]][starting_coordinates[0]] = s_type
        previous_pipe = starting_coordinates
        current_pipe = adjoining_pipes[0]
        loop = []
        loop.append(current_pipe)
        while current_pipe[0] != starting_coordinates[0] or current_pipe[1] != starting_coordinates[1]:
            adjoining_pipes = self.get_adjoining_pipes(current_pipe[0], current_pipe[1])
            if adjoining_pipes[0][0] != previous_pipe[0] or adjoining_pipes[0][1] != previous_pipe[1]:
                previous_pipe = current_pipe
                current_pipe = adjoining_pipes[0]
            else:
                previous_pipe = current_pipe
                current_pipe = adjoining_pipes[1]
            loop.append(current_pipe)
        return loop

    def get_next_point(self, current_point: Tuple[int,int], previous_point: Tuple[int,int]):
        adjoining_pipes = self.get_adjoining_pipes(current_point[0], current_point[1])
        if adjoining_pipes[0][0] != previous_point[0] or adjoining_pipes[0][1] != previous_point[1]:
            return adjoining_pipes[0]
        else:
            return adjoining_pipes[1]


    def odd_pipe_crossings(self, point: Tuple[int,int]):
        nodes_left, nodes_right, nodes_up, nodes_down = [], [], [], []

        for i in range(0, point[0]):
            nodes_left.append((i, point[1]))
        for i in range(point[0] + 1, len(self.matrix[0])):
            nodes_right.append((i, point[1]))
        for i in range(0, point[1]):
            nodes_up.append((point[0], i))
        for i in range(point[1] + 1, len(self.matrix)):
            nodes_down.append((point[0], i))

        left_crossings = 0
        last_direction_up = None
        for node in nodes_left:
            value = self.get_value_at_coordinates(node[0], node[1])
            if value == '|':
                left_crossings += 1
            elif value == 'F' or value == '7':
                if last_direction_up:
                    left_crossings += 1
                    last_direction_up = None
                else:
                    if last_direction_up is None:
                        last_direction_up = False
                    else: 
                        last_direction_up = None
            elif value == 'L' or value == 'J':
                if last_direction_up == False:
                    left_crossings += 1
                    last_direction_up = None
                else:
                    if last_direction_up is None:
                        last_direction_up = True
                    else: 
                        last_direction_up = None
        
        right_crossings = 0
        last_direction_up = None
        for node in nodes_right:
            value = self.get_value_at_coordinates(node[0], node[1])
            if value == '|':
                right_crossings += 1
            elif value == 'F' or value == '7':
                if last_direction_up:
                    right_crossings += 1
                    last_direction_up = None
                else:
                    if last_direction_up is None:
                        last_direction_up = False
                    else: 
                        last_direction_up = None
            elif value == 'L' or value == 'J':
                if last_direction_up == False:
                    right_crossings += 1
                    last_direction_up = None
                else:
                    if last_direction_up is None:
                        last_direction_up = True
                    else: 
                        last_direction_up = None
        
        last_direction_left = None
        up_crossings = 0
        for node in nodes_up:
            value = self.get_value_at_coordinates(node[0],node[1])
            if value == '-':
                up_crossings += 1
            elif value == 'L' or value == 'F':
                if last_direction_left:
                    up_crossings += 1
                    last_direction_left = None
                else:
                    if last_direction_left is None:
                        last_direction_left = False
                    else:
                        last_direction_left = None
            elif value == 'J' or value == '7':
                if last_direction_left == False:
                    up_crossings += 1
                    last_direction_left = None
                else:
                    if last_direction_left is None:
                        last_direction_left = True
                    else:
                        last_direction_left = None
        
        last_direction_left = None
        down_crossings = 0
        for node in nodes_down:
            value = self.get_value_at_coordinates(node[0],node[1])
            if value == '-':
                down_crossings += 1
            elif value == 'L' or value == 'F':
                if last_direction_left:
                    down_crossings += 1
                    last_direction_left = None
                else:
                    if last_direction_left is None:
                        last_direction_left = False
                    else:
                        last_direction_left = None
            elif value == 'J' or value == '7':
                if last_direction_left == False:
                    down_crossings += 1
                    last_direction_left = None
                else:
                    if last_direction_left is None:
                        last_direction_left = True
                    else:
                        last_direction_left = None


        if left_crossings % 2 == 1 and right_crossings % 2 == 1 and up_crossings % 2 == 1 and down_crossings % 2 == 1:
            return True
        return False
            

            

    # def get_length_of_loop(self) -> int:
    #     starting_coordinates = self.get_starting_coordinates()
    #     adjoining_pipes = self.get_adjoining_pipes(starting_coordinates[0], starting_coordinates[1])
    #     s_type = self.what_is_s(adjoining_pipes)
    #     self.matrix[starting_coordinates[1]][starting_coordinates[0]] = s_type
    #     previous_pipe = starting_coordinates
    #     current_pipe = adjoining_pipes[0]
    #     length = 1
    #     while current_pipe[0] != starting_coordinates[0] or current_pipe[1] != starting_coordinates[1]:
    #         adjoining_pipes = self.get_adjoining_pipes(current_pipe[0], current_pipe[1])
    #         if adjoining_pipes[0][0] != previous_pipe[0] or adjoining_pipes[0][1] != previous_pipe[1]:
    #             previous_pipe = current_pipe
    #             current_pipe = adjoining_pipes[0]
    #         else:
    #             previous_pipe = current_pipe
    #             current_pipe = adjoining_pipes[1]
    #         length += 1
    #     return length
                
    def what_is_s(self, adjoining_pipes: List[Tuple[int,int]]):
        first_pipe = adjoining_pipes[0]
        second_pipe = adjoining_pipes[1]
        if first_pipe[0] == second_pipe[0]:
            return '|'
        if first_pipe[1] == second_pipe[1]:
            return '-'
        if first_pipe[0] - 1 == second_pipe[0] and first_pipe[1] + 1 == second_pipe[1]:
            return 'F'
        if first_pipe[0] - 1 == second_pipe[0] and first_pipe[1] - 1 == second_pipe[1]:
            return 'L'
        if first_pipe[0] + 1 == second_pipe[0] and first_pipe[1] + 1 == second_pipe[1]:
            return '7'
        if first_pipe[0] + 1 == second_pipe[0] and first_pipe[1] - 1 == second_pipe[1]:
            return 'J'
        

    def get_adjoining_pipes(self, x: int, y: int):
        length_of_y = len(self.matrix)
        length_of_x = len(self.matrix[0])
        current_value = self.get_value_at_coordinates(x,y)
        square_above, square_below, square_left, square_right = None, None, None, None
        if x >= 0:
            square_left = self.matrix[y][x-1]
        if x + 1 < length_of_x:
            square_right = self.matrix[y][x+1]
        if y - 1 >= 0:
            square_above = self.matrix[y-1][x]
        if y + 1 < length_of_y:
            square_below = self.matrix[y+1][x]
        adjoining_pipes = []
        if square_left and current_value != '|' and current_value != 'L' and current_value != 'F':
            if square_left == '-' or square_left == 'F' or square_left == 'L':
                adjoining_pipes.append((x-1, y))
        if square_right and current_value != '|' and current_value != 'J' and current_value != '7':
            if square_right == '-' or square_right == 'J' or square_right == '7':
                adjoining_pipes.append((x+1, y))
        if square_above and current_value != '-' and current_value != 'F' and current_value != '7':
            if square_above == '|' or square_above == 'F' or square_above == '7':
                adjoining_pipes.append((x, y-1))
        if square_below and current_value != '-' and current_value != 'L' and current_value != 'J':
            if square_below == '|' or square_below == 'L' or square_below == 'J':
                adjoining_pipes.append((x, y+1))
        return adjoining_pipes
    
def read_text_file_to_lines(filename: str) -> List[str]:
    my_file = open(filename, "r")
    data = my_file.read()
    data_to_list = data.splitlines()
    my_file.close()
    return data_to_list

if __name__ == "__main__":
    data = read_text_file_to_lines("day10\example_part_2.txt")
    # data = [".....",".S-7.",".|.|.",".L-J.","....."]
    # data = ["..F7.",".FJ|.","SJ.L7","|F--J","LJ..."]
    puzzle_map = PuzzleMap(data)
    puzzle_map.odd_pipe_crossings((14,3))
    # adjoining_pipes = puzzle_map.get_adjoining_pipes(1,1)
    # s_type = puzzle_map.what_is_s(adjoining_pipes)
    # print(adjoining_pipes)
    # print(s_type)
    # length = puzzle_map.get_length_of_loop()
    # print(length // 2)