def read_input(file_path):
    """
    """
    input_map = []

    with open(file_path, mode='rt', encoding='utf-8') as f:
        for line in f:
            line_items = line.strip("\n")
            input_map.append(list(int(i) for i in line_items))
    
    return input_map


def find_way(input_map, line_id, column_id, from_number, output_set : set, output_list : list):

    if line_id < 0 or column_id < 0:
        return 0
    else:
        try:
            current_number = input_map[line_id][column_id]
        except IndexError:
            return 0
        if from_number == 8 and current_number == 9:
            output_set.add(tuple([line_id, column_id]))
            output_list.append(1)
            return 1
        elif current_number == from_number + 1:
            # up
            find_way(input_map, line_id - 1, column_id, current_number, output_set, output_list)
            # down
            find_way(input_map, line_id + 1, column_id, current_number, output_set, output_list)
            # right
            find_way(input_map, line_id, column_id + 1, current_number, output_set, output_list)
            # left
            find_way(input_map, line_id, column_id - 1, current_number, output_set, output_list)
        else:
            return 0


def start_from_all_0(input_map):

    total_score = 0
    total_trails = 0

    for line_id, _ in enumerate(input_map):
        for column_id, _ in enumerate(input_map):
            output_set = set()
            output_list = []
            if input_map[line_id][column_id] == 0:
                find_way(input_map, line_id, column_id, -1, output_set, output_list)
                score = len(output_set)
                total_score += score
                trails = len(output_list)
                total_trails += trails

    return total_score, total_trails


def part1(file_path):
    """
    """
    input_map = read_input(file_path)

    total_score, _ = start_from_all_0(input_map)

    print("Answer part 1:")
    print(f"Total score is: {total_score}")


def part2(file_path):
    """
    """
    input_map = read_input(file_path)

    _, total_trails = start_from_all_0(input_map)

    print("Answer part 2:")
    print(f"Total trails : {total_trails}")


if __name__ == "__main__":

    part1("day_10/day_10_input.txt")
    part2("day_10/day_10_input.txt")
