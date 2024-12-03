import re


def read_input(file_path):
    """
    """

    with open(file_path, mode='rt', encoding='utf-8') as f:
        lines = f.readlines()
        text = "".join(lines)
        return text


def parse_input_re(input):
    """
    return list of tuples
    """
    # search_pattern = r'mul\([0-9]+,[0-9]+\)'
    search_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    hits = re.findall(search_pattern, input)
    return hits


def parse_hits(hits):
    """
    """
    # result = sum(int(item[item.find('(')+1:item.find(',')]) * int(item[item.find(',')+1:item.find(')')]) for item in hits)
    result = sum(int(item[0]) * int(item[1]) for item in hits)
    return result

def get_parsable_input(all_input : str):
    """
    """
    
    start_pos = 0
    end_pos = 0
    result = ''

    while True:

        end_pos = all_input.find("don't()", start_pos)

        if end_pos == -1:
            result += all_input[start_pos:]
            break
        else:
            result += all_input[start_pos:end_pos]
        
        start_pos = end_pos + 7 # len("don't()")
        end_pos = all_input.find('do()', start_pos)

        if end_pos == -1:
            break
        else:
            start_pos = end_pos + 4 # len('do()')

    return result


def part1():
    """
    """

    # read input data
    input = read_input("day_03/day_03_input.txt")
    # print(input)

    # parse input using regular expression
    hits = parse_input_re(input)
    # print(hits)

    # calculate result by parsing valid hits
    result = parse_hits(hits)

    print("Answer part 1:")
    print(f"Parsed result is : {result}")

    return None

def part2():
    """
    """

    # read input data
    input = read_input("day_03/day_03_input.txt")
    # print(input)

    # parse input using instructions
    parsable_input = get_parsable_input(input)
    # print(parsable_input)

    # parse input using regular expression
    hits = parse_input_re(parsable_input)
    # print(hits)

    # calculate result by parsing valid hits
    result = parse_hits(hits)

    print("Answer part 2:")
    print(f"Parsed result is : {result}")

    return None


if __name__ == "__main__":

    part1()
    part2()
