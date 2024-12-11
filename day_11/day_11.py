def read_input(file_path):
    """
    """
    stones_dict = {}
    with open(file_path, mode='rt', encoding='utf-8') as f:
        for line in f:
            line_items = line.strip("\n")
            for stone in list(int(i) for i in line_items.split()):
                stones_dict[stone] = 1
   
    return stones_dict


def blink_once(stones_dict : dict):
    """
    """
    stones_to_check = list(stone for stone in stones_dict.keys())
    stones_dict_out = {}

    for stone in stones_to_check:

        stone_number_of_digits = len(str(stone))
        # all 0 stones replace with 1 stones
        if stone == 0:
            stones_dict_out[1] = stones_dict_out.get(1, 0) + stones_dict[0]
        # for stone with even number of digits - split into 2 stones
        elif stone_number_of_digits % 2 == 0:
            split_at = int(stone_number_of_digits / 2)
            stone_1 = int(str(stone)[:split_at])
            stone_2 = int(str(stone)[split_at:])
            stones_dict_out[stone_1] = stones_dict_out.get(stone_1, 0) + stones_dict[stone]
            stones_dict_out[stone_2] = stones_dict_out.get(stone_2, 0) + stones_dict[stone]
        # replace all stones with stone * 2024
        else:
            stones_dict_out[stone*2024] = stones_dict_out.get(stone*2024, 0) + stones_dict[stone]
    
    return stones_dict_out


def blink_n_times(stones_dict, n_times):
    """
    """
    n = 1
    while n <= n_times:
        stones_dict = blink_once(stones_dict)
        n += 1
   
    return stones_dict


def part1(file_path):
    """
    """
    stones_dict = read_input(file_path)

    times_to_blink = 25
    stones_dict = blink_n_times(stones_dict, times_to_blink)

    print("Answer part 1:")
    print(f"Number of stones after blinking {times_to_blink} times is : {sum(stone_count for stone_count in stones_dict.values())}")


def part2(file_path):
    """
    """
    stones_dict = read_input(file_path)

    times_to_blink = 75
    stones_dict = blink_n_times(stones_dict, times_to_blink)

    print("Answer part 1:")
    print(f"Number of stones after blinking {times_to_blink} times is : {sum(stone_count for stone_count in stones_dict.values())}")


if __name__ == "__main__":

    part1("day_11/day_11_input.txt")
    part2("day_11/day_11_input.txt")
