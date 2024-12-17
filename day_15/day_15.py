def read_input(file_path):
    """
    """
    warehouse = {}
    movements = []

    with open(file_path, mode='rt', encoding='utf-8') as f:
        y = 0
        for line in f:
            if line[0] == '#':
                for x, item in enumerate(i for i in line.strip('\n')):
                    warehouse[(x, y)] = item
                    if item == '@':
                        start_pos = (x, y)
                y += 1
                x += 1
            elif line[0] in ('<', '>', '^', 'v'):
                for i in line.strip('\n'):
                    movements.append(i)

    return warehouse, movements, start_pos


def print_warehouse(warehouse):
    """
    """
    len_x = len([k for k in warehouse.keys() if k[0]==0])
    len_y = len([k for k in warehouse.keys() if k[1]==0])

    for line_id in range(0, len_y):
        line = ''
        for column_id in range(0, len_x):
            line += warehouse[column_id, line_id]
        print(line)

    return None


def move_robot(warehouse, start_pos, direction):
    """
    """
    DIRECTIONS = {
        '<' : (-1,  0),
        '>' : ( 1,  0),
        '^' : ( 0, -1),
        'v' : ( 0,  1),
    }
    x_off = DIRECTIONS[direction][0]
    y_off = DIRECTIONS[direction][1]

    target_pos = (start_pos[0] + x_off, start_pos[1] + y_off)

    # cannot move if target is wall
    if warehouse[target_pos] == '#':
        return start_pos

    # can move if target is free space
    elif warehouse[target_pos] == '.':
        warehouse[start_pos] = '.'
        warehouse[target_pos] = '@'
        return target_pos

    # if target is box, check if box can be moved
    elif warehouse[target_pos] == 'O':
        check_next_pos = (target_pos[0] + x_off, target_pos[1] + y_off)
        # find first empty space before wall
        while True:
            if warehouse[check_next_pos] == '.':
                empty_space_pos = check_next_pos
                break
            elif warehouse[check_next_pos] == '#':
                empty_space_pos = None
                break
            check_next_pos = (check_next_pos[0] + x_off, check_next_pos[1] + y_off)
        # can move the box
        if empty_space_pos is not None:
            warehouse[start_pos] = '.'
            warehouse[target_pos] = '@'
            warehouse[empty_space_pos] = 'O'
            return target_pos
        # cannot move the box
        else:
            return start_pos


def part1(file_path):
    """
    """
    warehouse, movements, start_pos = read_input(file_path)
    # print_warehouse(warehouse)
    # print(f"Starting position : {start_pos}")
    # print(f"Movement : {movements}")
   
    for direction in movements:
        # print(f"Next move : {direction}")
        start_pos = move_robot(warehouse, start_pos, direction)
        # print_warehouse(warehouse)

    # print_warehouse(warehouse)

    print("Answer part 1:")
    print(f"Sum of all GPC coordinates of all boxes is :{sum(x + 100 * y for (x, y), item in warehouse.items() if item == 'O')}")


def part2(file_path):
    """
    """
    robots = read_input(file_path)

    print("Answer part 2:")


if __name__ == "__main__":

    part1("day_15/day_15_input.txt")
    # part2("day_15/day_15_input.txt")
