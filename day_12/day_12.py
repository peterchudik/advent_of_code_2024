from pprint import pprint as pp
import copy

def read_input(file_path):
    """
    """
    farm = []

    with open(file_path, mode='rt', encoding='utf-8') as f:
        for line in f:
            farm.append(list(c for c in line.strip("\n")))
   
    return farm


def find_garden(garden_id : str, line_id : int, column_id : int, farm_found : list, gardens : dict, farm : list):
    """
    """
    if line_id < 0 or column_id < 0:
        return None
    elif line_id >= len(farm_found) or column_id >= len(farm_found[0]):
        return None
    elif farm_found[line_id][column_id] != garden_id[0]:
        return None
    else:
        # fence_count = get_fence_count(farm, line_id, column_id)
        gardens[garden_id].append(tuple([line_id, column_id]))
        farm_found[line_id][column_id] = '.'
        # move left
        find_garden(garden_id, line_id, column_id - 1, farm_found, gardens, farm)
        # move right
        find_garden(garden_id, line_id, column_id + 1, farm_found, gardens, farm)
        # move up
        find_garden(garden_id, line_id - 1, column_id, farm_found, gardens, farm)
        # move down
        find_garden(garden_id, line_id + 1, column_id, farm_found, gardens, farm)

    return None


def find_all_gardens(farm):
    """
    """
    gardens = {}
    farm_found = copy.deepcopy(farm)

    for line_id, line_item in enumerate(farm):
        for column_id, column_item in enumerate(line_item):

            if farm_found[line_id][column_id] == '.':
                continue
            else:
                garden_id = column_item + '_' + str(line_id) + '_' + str(column_id)
                gardens[garden_id] = []
                find_garden(garden_id, line_id, column_id, farm_found, gardens, farm)
    
    return gardens


def get_fence_cost(gardens):
    """
    """
    fence_cost_total = 0
    fence_cost_total_per_side = 0

    for _, garden_coordinates in gardens.items():
        fence_count = 0
        corner_count = 0
        for coordinate in garden_coordinates:

            # get fence count
            line_id, column_id = coordinate
            if (line_id, column_id - 1) not in garden_coordinates:
                fence_count += 1
            if (line_id, column_id + 1) not in garden_coordinates:
                fence_count += 1
            if (line_id - 1, column_id) not in garden_coordinates:
                fence_count += 1
            if (line_id + 1, column_id) not in garden_coordinates:
                fence_count += 1
            
            # get corner count
            # outer corner
            if (line_id, column_id - 1) not in garden_coordinates and (line_id - 1, column_id) not in garden_coordinates:
                corner_count += 1
            if (line_id - 1, column_id) not in garden_coordinates and (line_id, column_id + 1) not in garden_coordinates:
                corner_count += 1
            if (line_id, column_id + 1) not in garden_coordinates and (line_id + 1, column_id) not in garden_coordinates:
                corner_count += 1
            if (line_id + 1, column_id) not in garden_coordinates and (line_id, column_id - 1) not in garden_coordinates:
                corner_count += 1

            # inner corner
            if (line_id, column_id - 1) in garden_coordinates and (line_id - 1, column_id) in garden_coordinates and (line_id - 1, column_id - 1) not in garden_coordinates:
                corner_count += 1
            if (line_id - 1, column_id) in garden_coordinates and (line_id, column_id + 1) in garden_coordinates and (line_id - 1, column_id + 1) not in garden_coordinates:
                corner_count += 1
            if (line_id, column_id + 1) in garden_coordinates and (line_id + 1, column_id) in garden_coordinates and (line_id + 1, column_id + 1) not in garden_coordinates:
                corner_count += 1
            if (line_id + 1, column_id) in garden_coordinates and (line_id, column_id - 1) in garden_coordinates and (line_id + 1, column_id - 1) not in garden_coordinates:
                corner_count += 1

        fence_cost_total += fence_count * len(garden_coordinates)
        fence_cost_total_per_side += corner_count * len(garden_coordinates)

    return fence_cost_total, fence_cost_total_per_side


def part1(file_path):
    """
    """
    farm = read_input(file_path)

    gardens = find_all_gardens(farm)

    fence_cost_total, _ = get_fence_cost(gardens)

    print("Answer part 1:")
    print(f"Total price of fencing all gardens on the farm is {fence_cost_total}")


def part2(file_path):
    """
    """
    farm = read_input(file_path)

    gardens = find_all_gardens(farm)

    _, fence_cost_total_per_side = get_fence_cost(gardens)

    print("Answer part 1:")
    print(f"Total price of fencing all gardens on the farm is {fence_cost_total_per_side}")


if __name__ == "__main__":

    part1("day_12/day_12_input.txt")
    part2("day_12/day_12_input.txt")
