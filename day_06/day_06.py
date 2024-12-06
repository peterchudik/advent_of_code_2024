import copy


def read_input(file_path):
    """
    """
    field = []

    with open(file_path, mode='rt', encoding='utf-8') as f:
        for line in f:
            line_items = list(line.strip("\n"))
            field.append(line_items)
    
    return field


def find_start_position(field):
    """
    """
    number_of_lines = len(field)
    number_of_columns = len(field[0])
    start_line = -1
    start_column = -1

    for line in range(0,number_of_lines):
        for column in range(0, number_of_columns):
            if field[line][column] in (['>','<','^','v']):
                start_line = line
                start_column = column
                break

    return start_line, start_column


GUARD_DIRECTIONS = {
    '^' : {'offset_line' : -1, 'offset_column' :  0, 'next_direction' : '>'},
    '>' : {'offset_line' :  0, 'offset_column' :  1, 'next_direction' : 'v'},
    'v' : {'offset_line' :  1, 'offset_column' :  0, 'next_direction' : '<'},
    '<' : {'offset_line' :  0, 'offset_column' : -1, 'next_direction' : '^'},
}


def walk_field(field : list):
    """
    """
    current_line, current_column = find_start_position(field)
    guard_direction = field[current_line][current_column]
    field[current_line][current_column] = set(guard_direction)

    distinct_positions = 1
    left_field = False

    while True:
        try:
            next_line = current_line + GUARD_DIRECTIONS[guard_direction]['offset_line']
            next_column = current_column + GUARD_DIRECTIONS[guard_direction]['offset_column']

            if next_line < 0 or next_column < 0:
                left_field = True
                break

            # next field is obstacle
            if field[next_line][next_column] == '#':
                guard_direction = GUARD_DIRECTIONS[guard_direction]['next_direction']

            # next field is not obstacle
            else:
                # visiting field first time
                if field[next_line][next_column] == '.':
                    distinct_positions += 1
                    field[next_line][next_column] = set(guard_direction)
                # visiting field not first time
                else:
                    # if comming from same direction again then in loop
                    if guard_direction in field[next_line][next_column]:
                        left_field = False
                        break
                    else:
                        field[next_line][next_column].add(guard_direction)

                current_line = next_line
                current_column = next_column

        except IndexError:
            left_field = True
            break
    
    return distinct_positions, left_field


def part1(file_path):
    """
    """
    field = read_input(file_path)
    distinct_positions, _ = walk_field(field)

    print("Answer part 1:")
    print(f"Number of distinct positions before leaving field : {distinct_positions}")


def gen_fields_with_obstacle(field):
    """
    """
    number_of_lines = len(field)
    number_of_columns = len(field[0])

    for line in range(0,number_of_lines):
        for column in range(0, number_of_columns):
            if field[line][column] == '.':
                field[line][column] = '#'
                yield copy.deepcopy(field)
                field[line][column] = '.'


def part2(file_path):
    """
    """
    field = read_input(file_path)

    obstacle_positions = 0
    for field_with_obstacle in gen_fields_with_obstacle(field):
        _, left_field = walk_field(field_with_obstacle)
        if left_field == False:
            obstacle_positions += 1

    print("Answer part 2:")
    print(f"Number of positions to place obstacle to never leave field : {obstacle_positions}")


if __name__ == "__main__":

    part1("day_06/day_06_input.txt")
    part2("day_06/day_06_input.txt")
