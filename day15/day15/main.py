def read_text_file_split_csv(filename: str) -> list[str]:
    my_file = open(filename, "r")
    data = my_file.read()
    return data.split(',')

def run_hash_algorithm_on_string(input: str) -> int:
    # Determine the ASCII code for the current character of the string.
    # Increase the current value by the ASCII code you just determined.
    # Set the current value to itself multiplied by 17.
    # Set the current value to the remainder of dividing itself by 256.
    current_value = 0
    for i in input:
        current_value += ord(i)
        current_value *= 17
        current_value = current_value % 256
    return current_value




if __name__ == "__main__":
    data = read_text_file_split_csv("day15/input.txt")
    total = 0
    boxes = {}
    for i in range(256):
        boxes[i] = []
    # print(boxes)
    for element in data:
        if '=' in element:
            parts = element.split('=')
            label = parts[0]
            focal_length = parts[1]
            box = run_hash_algorithm_on_string(label)
            existing_labels_in_box = [list(key.keys())[0] for key in boxes[box]]
            if label in existing_labels_in_box:
                element_index = 0
                for lens in boxes[box]:
                    if list(lens.keys())[0] == label:
                        element_index = boxes[box].index(lens)
                boxes[box][element_index] = {label: int(focal_length)}
            else:
                boxes[box].append({label: int(focal_length)})
        if '-' in element:
            parts = element.split('-')
            label = parts[0]
            focal_length = parts[1]
            box = run_hash_algorithm_on_string(label)

            existing_labels_in_box = [list(key.keys())[0] for key in boxes[box]]
            if label in existing_labels_in_box:
                element_to_remove = {}
                for lens in boxes[box]:
                    if list(lens.keys())[0] == label:
                        element_to_remove = lens
                boxes[box].remove(element_to_remove)
    total = 0
    for x, box in enumerate(boxes):
        for i, element in enumerate(boxes[box]):
            total += (x+1) * (i+1) * list(element.values())[0]
            # print(i, end=" ")
            # print(element)
    print(total)