from pprint import pprint as pp


def read_input(file_path, change_prize):
    """
    """
    claw_machines = []
    with open(file_path, mode='rt', encoding='utf-8') as f:
        i = 1
        for line in f:
            # Buttons A B
            if i == 1 or i == 2:
                if i == 1:
                    claw_machine = {}
                line_items = line.strip("\n").split(":")
                x = int(line_items[1].split(",")[0].lstrip(' X+'))
                y = int(line_items[1].split(",")[1].lstrip(' Y+'))
                claw_machine[line_items[0]] = tuple([x, y])
                i += 1
            # Prize
            elif i == 3:
                line_items = line.strip("\n").split(":")
                x = int(line_items[1].split(",")[0].lstrip(' X='))
                y = int(line_items[1].split(",")[1].lstrip(' Y='))
                if change_prize == True:
                    claw_machine[line_items[0]] = tuple([10000000000000 + x, 10000000000000 + y])
                else:
                    claw_machine[line_items[0]] = tuple([x, y])
                i += 1
            else:
                claw_machines.append(claw_machine)
                i = 1
        claw_machines.append(claw_machine)

    return claw_machines


def get_machine_min_game_cost(claw_machines):
    """
    """
    machine_game_min_cost = {}

    for machine_id, machine in enumerate(claw_machines):

        button_a__x  = machine['Button A'][0]
        button_a__y  = machine['Button A'][1]
        button_b__x  = machine['Button B'][0]
        button_b__y  = machine['Button B'][1]
        prize__x  = machine['Prize'][0]
        prize__y  = machine['Prize'][1]

        button_a__count = (prize__x * button_b__y - prize__y * button_b__x) / (button_b__y * button_a__x - button_b__x * button_a__y)
        button_b__count = (prize__x * button_a__y - prize__y * button_a__x) / (button_a__y * button_b__x - button_b__y * button_a__x)

        # print(button_a__count, button_b__count)

        if button_a__count == int(button_a__count) and button_b__count == int(button_b__count):
            machine_game_min_cost[machine_id] = int(button_a__count * 3 + button_b__count * 1)
        else:
            machine_game_min_cost[machine_id] = 0

    return machine_game_min_cost


def part1(file_path):
    """
    """
    claw_machines = read_input(file_path, change_prize = False)
    # pp(claw_machines)

    machine_game_min_cost = get_machine_min_game_cost(claw_machines)
    # print(machine_game_min_cost)

    print("Answer part 1:")
    print(f"Total of all minimum prizes of all games in: {sum(min_cost for min_cost in machine_game_min_cost.values())}")


def part2(file_path):
    """
    """
    claw_machines = read_input(file_path, change_prize = True)
    # pp(claw_machines)

    machine_game_min_cost = get_machine_min_game_cost(claw_machines)
    # print(machine_game_min_cost)

    print("Answer part 2:")
    print(f"Total of all minimum prizes of all games in: {sum(min_cost for min_cost in machine_game_min_cost.values())}")


if __name__ == "__main__":

    part1("day_13/day_13_input.txt")
    part2("day_13/day_13_input.txt")
