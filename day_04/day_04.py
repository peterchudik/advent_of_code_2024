def read_input(file_path):
    """
    """
    field = []

    with open(file_path, mode='rt', encoding='utf-8') as f:
        for line in f:
            line_items = list(line.strip("\n"))
            field.append(line_items)
        
    return field


def word_count_horizontal(field : list, word : str):
    """
    """
    word_count_left_to_right = sum(''.join(line).count(word) for line in field)
    word_count_right_to_left = sum(''.join(reversed(line)).count(word) for line in field)

    return word_count_left_to_right + word_count_right_to_left


def get_verticals(field):
    """
    transpose field -> columns become lines
    """
    number_of_lines = len(field)
    number_of_columns = len(field[0])

    result = []

    for column in range(0,number_of_columns):
        result_line = []
        for line in range(0, number_of_lines):
            result_line.append(field[line][column])
        result.append(list(reversed(result_line)))
    
    return result


def get_diagonals(field):
    """
    get diagonals from field -> diagonal become line
    assumption number of lines is the same as number of columns
    """
    number_of_lines = len(field)
    # print(number_of_lines)

    result = []

    for line_id in range(0, number_of_lines):

        result_diagonal_upper = []
        result_diagonal_lower = []
        index_line = line_id
        offset = number_of_lines - line_id - 1

        for index in range(0, line_id + 1):

            index_column = index

            result_diagonal_upper.append(field[index_line][index_column])
            if offset > 0:
                result_diagonal_lower.append(field[index_line + offset][index_column + offset])

            index_line -= 1
            index_column += 1

        result.append(result_diagonal_upper)
        result.append(result_diagonal_lower)

    return result


def check_x_mas(field_3x3):
    """
    """
    if (
        field_3x3[1][1] == 'A' and
        (
            (field_3x3[0][0] == 'M' and field_3x3[2][2] == 'S') or
            (field_3x3[0][0] == 'S' and field_3x3[2][2] == 'M')
        ) and
        (
            (field_3x3[0][2] == 'M' and field_3x3[2][0] == 'S') or
            (field_3x3[0][2] == 'S' and field_3x3[2][0] == 'M')
        )
       ):
        return True
    else:
        return False


def get_all_fields_3x3(field):
    """
    """
    number_of_lines = len(field)
    number_of_columns = len(field[0])

    result = []

    for line in range(0, number_of_lines-2):
        for column in range(0, number_of_columns-2):

            field_3x3 = []

            result_line = field[line][column:column+3]
            field_3x3.append(result_line)
            result_line = field[line+1][column:column+3]
            field_3x3.append(result_line)
            result_line = field[line+2][column:column+3]
            field_3x3.append(result_line)

            result.append(field_3x3)

    return result


def part1(file_path):
    """
    """
    field = read_input(file_path)

    search_word = 'XMAS'

    wc_horizontals = word_count_horizontal(field, search_word)

    field_verticals = get_verticals(field)
    wc_verticals = word_count_horizontal(field_verticals, search_word)

    field_diagonals = get_diagonals(field)
    wc_diagonals = word_count_horizontal(field_diagonals, search_word)

    field_diagonals_v = get_diagonals(field_verticals)
    wc_diagonals_v = word_count_horizontal(field_diagonals_v, search_word)

    print("Answer part 1:")
    print(f"Total count of word {search_word} is : {wc_horizontals + wc_verticals + wc_diagonals + wc_diagonals_v}")


def part2(file_path):
    """
    """
    field = read_input(file_path)

    all_fields_3x3 = get_all_fields_3x3(field)

    x_mas_count = sum(1 for field_3x3 in all_fields_3x3 if check_x_mas(field_3x3))

    print("Answer part 2:")
    print(f"Total X-MAS shapes id : {x_mas_count}")


if __name__ == "__main__":

    part1("day_04/day_04_input.txt")
    part2("day_04/day_04_input.txt")
