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

def get_fence_count(farm, line_id, column_id):

    fence_count = 0
    # check left
    if column_id == 0 or farm[line_id][column_id] != farm[line_id][column_id - 1]:
        fence_count += 1
    # check right
    if column_id == len(farm[0]) - 1 or farm[line_id][column_id] != farm[line_id][column_id + 1]:
        fence_count += 1
    # check up
    if line_id == 0 or farm[line_id][column_id] != farm[line_id - 1][column_id]:
        fence_count += 1
    # check down
    if line_id == len(farm) - 1 or farm[line_id][column_id] != farm[line_id + 1][column_id]:
        fence_count += 1

    return fence_count 


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
        fence_count = get_fence_count(farm, line_id, column_id)
        gardens[garden_id].append(tuple([line_id, column_id, fence_count]))
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


def part1(file_path):
    """
    """
    farm = read_input(file_path)

    gardens = find_all_gardens(farm)

    total_price = 0
    for _, garden_info in gardens.items():
        number_of_garden_fields = len(garden_info)
        number_of_fences = sum(i[2] for i in garden_info)
        total_price = total_price + (number_of_garden_fields * number_of_fences)

    print("Answer part 1:")
    print(f"Total price of fencing all gardens on the farm is {total_price}")


def part2(file_path):
    """
    """
    pass

if __name__ == "__main__":

    part1("day_12/day_12_input.txt")
    part2("day_12/day_12_input_test.txt")
