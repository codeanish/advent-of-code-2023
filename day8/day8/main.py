


from typing import Dict, List, Tuple


def read_text_file_to_lines(filename: str) -> List[str]:
    my_file = open(filename, "r")
    data = my_file.read()
    data_to_list = data.splitlines()
    my_file.close()
    return data_to_list

def build_node_map(node_data: List[str]) -> Dict[str, Tuple[str,str]]:
    nodes = {}
    for node in node_data:
        node_string = node.split('=')
        key = node_string[0].strip()
        value = node_string[1].strip().replace('(', '').replace(')','').split(',')
        nodes[key] = (value[0].strip(),value[1].strip())
    return nodes

def part_1(nodes: Dict[str, Tuple[str,str]], directions: str) -> int:
    end_key = 'ZZZ'
    current_key = 'AAA'

    # strange implementation below to allow for infinite looping over directions
    length_of_directions = len(directions)
    steps = 0
    # No guaranteed break condition, pray for nice input
    while current_key != end_key:
        current_node = nodes[current_key]
        direction = directions[steps % length_of_directions]
        if direction == 'R':
            current_key = current_node[1]
        elif direction == 'L':
            current_key = current_node[0]
        steps += 1
    return steps

def part_2_brute_force(nodes: Dict[str, Tuple[str,str]], directions: str) -> int:
    keys = list(nodes.keys())
    current_keys = list(filter(lambda x: x[2] == 'A', keys))
    print(current_keys)
    steps = 0
    length_of_directions = len(directions)
    while not all_keys_at_end(current_keys):
        direction = directions[steps % length_of_directions]
        next_keys = []
        for key in current_keys:
            if direction == 'R':
                next_keys.append(nodes[key][1])
            elif direction == 'L':
                next_keys.append(nodes[key][0])
        current_keys = next_keys
        steps += 1
    print(steps)


            

def all_keys_at_end(keys: list[str]) -> bool:
    for key in keys:
        if key[2] != 'Z':
            return False
    return True



if __name__ == "__main__":
    data = read_text_file_to_lines("day8\input.txt")
    directions = data[0]
    data = data[2::]
    nodes = build_node_map(data)

    # part_2_brute_force(nodes, directions)

    # steps = part_1(nodes, directions)
    # print(f"Number of steps = {steps}")