import itertools

def read_input(file_path):
    """
    """
    input = {}

    with open(file_path, mode='rt', encoding='utf-8') as f:
        i = 1
        for line in f:
            line_items = line.strip("\n")
            result = int(line_items.split(':')[0])
            input_values = [int(v) for v in line_items.split(':')[1].split()]
            input[i] = {
                        'result': result,
                        'input_values': input_values,
                        'input_values_count' : len(input_values)
                        }
            i += 1
    
    return input


def calculate_calibration_result(input, operators):

    calibration_result = 0

    for line_items in input.values():

        input_values_count = line_items['input_values_count']
        input_values = line_items['input_values']
        input_result = line_items['result']

        for opeartor_combination in itertools.product(operators, repeat=input_values_count-1):

            result = input_values[0]
            for i in range(1, input_values_count):
                operator = opeartor_combination[i-1]

                if operator == '*':
                    result = result * input_values[i]
                elif operator == '+':
                    result = result + input_values[i]
                elif operator == '||':
                    result = int(str(result) + str(input_values[i]))
                else:
                    raise NotImplementedError
            
            if result == input_result:
                calibration_result += result
                break

    return calibration_result


def part1(file_path):
    """
    """
    input = read_input(file_path)

    calibration_result = calculate_calibration_result(input, ['*', '+'])

    print("Answer part 1:")
    print(f"Total sum of all good equations id : {calibration_result}")


def part2(file_path):
    """
    """
    input = read_input(file_path)

    calibration_result = calculate_calibration_result(input, ['*', '+', '||'])

    print("Answer part 2:")
    print(f"Total sum of all good equations id : {calibration_result}")


if __name__ == "__main__":

    part1("day_07/day_07_input.txt")
    part2("day_07/day_07_input.txt")

