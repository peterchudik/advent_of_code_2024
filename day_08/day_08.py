from pprint import pprint as pp
import copy
import itertools

def read_input(file_path):
    """
    """
    input_field = []

    with open(file_path, mode='rt', encoding='utf-8') as f:
        for line in f:
            line_items = line.strip("\n")
            input_field.append(list(i for i in line_items))
    
    return input_field


def get_antenas_coordinates(input_field):
    """
    """
    antenas_coordinates = {}

    for line_id, line_item in enumerate(input_field):
        for column_id, column_item in enumerate(line_item):
            if column_item == '.':
                continue
            elif column_item in antenas_coordinates:
                antenas_coordinates[column_item].append((line_id, column_id))
            else:
                antenas_coordinates[column_item] = [(line_id, column_id)]
    
    return antenas_coordinates


def get_antinodes_coordinates(coordinate_pair, max_line, max_column, only_first):
    """
    """
    antinode_coordinates = []

    c1, c2 = coordinate_pair
    c1_line, c1_column = c1[0], c1[1]
    c2_line, c2_column = c2[0], c2[1]

    if c1_line <= c2_line and c1_column <= c2_column:
        c1_line_offset = c1_line - c2_line # negative
        c1_column_offset = c1_column - c2_column # negative
        c2_line_offset = c2_line - c1_line # positive
        c2_column_offset = c2_column - c1_column # positive

    elif c1_line >= c2_line and c1_column >= c2_column:
        c1_line_offset = c1_line - c2_line # positive
        c1_column_offset = c1_column - c2_column # positive
        c2_line_offset = c2_line - c1_line # negative
        c2_column_offset = c2_column - c1_column # negative

    elif c1_line < c2_line and c1_column > c2_column:
        c1_line_offset = c1_line - c2_line # negative
        c1_column_offset = c1_column - c2_column # positive
        c2_line_offset = c2_line - c1_line # positive
        c2_column_offset = c2_column - c1_column # negative

    elif c1_line > c2_line and c1_column < c2_column:
        c1_line_offset = c1_line - c2_line # positive
        c1_column_offset = c1_column - c2_column # negative
        c2_line_offset = c2_line - c1_line # negative
        c2_column_offset = c2_column - c1_column # positive

    ac1_line = c1_line + c1_line_offset
    ac1_column = c1_column + c1_column_offset
    while (0 <= ac1_line <= max_line and 0 <= ac1_column <= max_column):
        antinode_coordinates.append((ac1_line, ac1_column))
        if only_first:
            break
        ac1_line += c1_line_offset
        ac1_column += c1_column_offset

    ac2_line = c2_line + c2_line_offset
    ac2_column = c2_column + c2_column_offset
    while (0 <= ac2_line <= max_line and 0 <= ac2_column <= max_column):
        antinode_coordinates.append((ac2_line, ac2_column))
        if only_first:
            break
        ac2_line += c2_line_offset
        ac2_column += c2_column_offset

    return antinode_coordinates


def place_antinode_into_field(field, coordinate):
    """
    """
    if min(coordinate[0], coordinate[1]) >= 0:
        try:
            field[coordinate[0]][coordinate[1]] = '#'
        except IndexError:
            pass
    return None


def count_antinodes_in_field(field, include_antenas):
    """
    """
    counter = 0

    for line_item in field:
        for column_item in line_item:
            if column_item == '.':
                continue
            elif include_antenas:
                counter +=1
            elif column_item == '#':
                counter += 1
    
    return counter


def place_antinodes(input_field, only_first):
    """
    """
    field_with_antinodes = copy.deepcopy(input_field)
    antenas_coordinates = get_antenas_coordinates(input_field)

    field_max_line_index = len(input_field) - 1
    field_max_column_index = len(input_field[0]) - 1

    for _, coordinates in antenas_coordinates.items():
        for coordinate_pair in itertools.combinations(coordinates,2):
            antinodes = get_antinodes_coordinates(coordinate_pair, field_max_line_index, field_max_column_index, only_first)
            for antinode in antinodes:
                place_antinode_into_field(field_with_antinodes, antinode)

    return field_with_antinodes


def part1(file_path):
    """
    """
    input_field = read_input(file_path)

    field_with_antinodes = place_antinodes(input_field, only_first = True)

    print("Answer part 1:")
    print(f"Number of antinodes in the field is :{count_antinodes_in_field(field_with_antinodes, include_antenas = False)}")


def part2(file_path):
    """
    """
    input_field = read_input(file_path)

    field_with_antinodes = place_antinodes(input_field, only_first = False)

    print("Answer part 2:")
    print(f"Number of antinodes in the field is :{count_antinodes_in_field(field_with_antinodes, include_antenas = True)}")


if __name__ == "__main__":

    part1("day_08/day_08_input.txt")
    part2("day_08/day_08_input.txt")

