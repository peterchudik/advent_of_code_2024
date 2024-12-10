from pprint import pprint as pp

def read_input(file_path):
    """
    """
    input_map = []

    with open(file_path, mode='rt', encoding='utf-8') as f:
        for line in f:
            line_items = line.strip("\n")
            input_map.append(list(i for i in line_items))
    
    return input_map


def part1(file_path):
    """
    """
    input_map = read_input(file_path)
    pp(input_map)

    print("Answer part 1:")


def part2(file_path):
    """
    """
    input_map = read_input(file_path)
    pp(input_map)

    print("Answer part 2:")


if __name__ == "__main__":

    part1("day_10/day_10_input_test.txt")
    part2("day_10/day_10_input_test.txt")

