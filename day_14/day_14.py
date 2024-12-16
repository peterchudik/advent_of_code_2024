from pprint import pprint as pp


def read_input(file_path):
    """
    """
    robots = {}
    with open(file_path, mode='rt', encoding='utf-8') as f:
        robot_id = 1
        for line in f:
            position = tuple(int(i) for i in line.strip('\n').split()[0].lstrip('p=').split(','))
            velocity = tuple(int(i) for i in line.strip('\n').split()[1].lstrip('v=').split(','))
            robots[robot_id] = {
                'start_at' : position,
                'velocity' : velocity,
            }
            robot_id += 1

    return robots


def move_robots(robots : dict, space : tuple, seconds : int):
    """
    """
    space_x, space_y = space

    for robot_id, robot in robots.items():
        velocity_x, velocity_y = robot['velocity']
        start_at_x, start_at_y = robot['start_at']

        # move by
        move_by_x = ((abs(velocity_x) * seconds) % space_x) * int((velocity_x / abs(velocity_x)))
        move_by_y = ((abs(velocity_y) * seconds) % space_y) * int((velocity_y / abs(velocity_y)))

        # get current
        current_at_x = start_at_x + move_by_x
        current_at_y = start_at_y + move_by_y

        # teleport at X walls
        if current_at_x < 0:
            current_at_x = space_x + current_at_x
        elif current_at_x >= space_x:
            current_at_x = current_at_x - space_x

        # teleport at Y walls
        if current_at_y < 0:
            current_at_y = space_y + current_at_y
        elif current_at_y >= space_y:
            current_at_y = current_at_y - space_y

        robots[robot_id]['current_position'] = (current_at_x, current_at_y)

    return robots


def robot_count_in_quadrants(robots : dict, space : tuple):
    """
    """
    space_x, space_y = space
    if space_x % 2 == 0 or space_y % 2 == 0:
        raise NotImplementedError

    q1_count, q2_count, q3_count, q4_count = 0, 0, 0, 0

    for robot in robots.values():
        at_x, at_y = robot['current_position']
        # q1
        if 0 <= at_x < (space_x // 2) and 0 <= at_y < (space_y // 2):
            q1_count += 1
        # q2
        elif (space_x // 2) < at_x < space_x and 0 <= at_y < (space_y // 2):
            q2_count += 1
        # q3
        elif 0 <= at_x < (space_x // 2) and (space_y // 2) < at_y < space_y:
            q3_count += 1
        # q4
        elif (space_x // 2) < at_x < space_x and (space_y // 2) < at_y < space_y:
            q4_count += 1

    return q1_count, q2_count, q3_count, q4_count


def detect_christmas_tree(robots, space):
    """
    the idea is that christmass tree is formed at minimum safety factor, meaning most robots in 1 sector
    also assuming robot positions are repeating no later than after (space size x * space size y) seconds
    """
    min_safety_factor = None
    min_safety_factor_at = 0
    space_x, space_y = space

    for i in range(1, space_x*space_y+1):
        move_robots(robots, space, i)
        q1, q2, q3, q4 = robot_count_in_quadrants(robots, space)
        current_sf = q1 * q2 * q3 * q4
        if min_safety_factor is None or min_safety_factor >= current_sf:
            min_safety_factor = current_sf
            min_safety_factor_at = i

    return min_safety_factor, min_safety_factor_at


def part1(file_path):
    """
    """
    space = (101, 103)
    number_of_seconds = 100

    robots = read_input(file_path)
    robots = move_robots(robots, space, number_of_seconds)

    q1, q2, q3, q4 = robot_count_in_quadrants(robots, space)

    print("Answer part 1:")
    print(f"Safety factor is : {q1 * q2 * q3 * q4}")


def part2(file_path):
    """
    """
    space = (101, 103)

    robots = read_input(file_path)
    min_safety_factor, min_safety_factor_at = detect_christmas_tree(robots, space)

    print("Answer part 2:")
    print(f"Christmas tree is formed at minimum safety factor {min_safety_factor} after {min_safety_factor_at} seconds")


if __name__ == "__main__":

    part1("day_14/day_14_input.txt")
    part2("day_14/day_14_input.txt")
