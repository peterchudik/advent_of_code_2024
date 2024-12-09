def read_input(file_path):
    """
    """
    with open(file_path, mode='rt', encoding='utf-8') as f:
        for line in f:
            line_items = line.strip("\n")
            disk_map = tuple(int(i) for i in line_items)
    
    return disk_map


def get_disk_blocks_from_disk_map(disk_map):
    """
    """
    disk_blocks = []
    file_id = 0

    for i, item_size in enumerate(disk_map):
        # is file
        if i % 2 == 0:
            disk_blocks += [file_id] * item_size
            file_id += 1 
        # is empty block
        else:
            disk_blocks += [None] * item_size

    return disk_blocks


def compress_disk_blocks(disk_blocks : list):
    """
    """
    while True:

        first_none_index = disk_blocks.index(None)

        for i, item in enumerate(reversed(disk_blocks)):
            if item is not None:
                last_not_none_index = len(disk_blocks) - i - 1
                break

        if first_none_index > last_not_none_index:
            break
        else:
            disk_blocks[first_none_index], disk_blocks[last_not_none_index] = disk_blocks[last_not_none_index], disk_blocks[first_none_index]

    return disk_blocks


def compress_disk_blocks_filewise(disk_blocks : list):
    """
    """
    last_file_id = None
    for item in reversed(disk_blocks):
        if item is not None:
            last_file_id = item
            break
    
    for file_id in range(last_file_id, 0, -1):

        file_start_index = disk_blocks.index(file_id)
        file_len = disk_blocks.count(file_id)

        # search empty block which can fit the file
        search_from = 0
        found_block = False
        while True:
            empty_block_start_index = disk_blocks.index(None, search_from)

            # if start index would be after file tart index
            if empty_block_start_index >= file_start_index:
                break

            # search only until start of the file
            if search_from >= file_start_index:
                break

            # found block to fit the file
            if all(block == None for block in disk_blocks[empty_block_start_index : empty_block_start_index + file_len]):
                found_block = True
                break
            # continue block search
            else:
                search_from = empty_block_start_index + 1

        # found block to place the file into
        if found_block == True:
            for i in range(0, file_len):
                disk_blocks[empty_block_start_index + i], disk_blocks[file_start_index + i] = disk_blocks[file_start_index + i], disk_blocks[empty_block_start_index + i]
        # no block to fit the file, move to next file
        else:
            continue
    
    return disk_blocks


def calc_disk_check_sum(disk_blocks : list):
    """
    """
    return sum(i * item for i, item in enumerate(disk_blocks) if item is not None)


def part1(file_path):
    """
    """
    disk_map = read_input(file_path)

    disk_blocks = get_disk_blocks_from_disk_map(disk_map)

    disk_blocks = compress_disk_blocks(disk_blocks)

    check_sum = calc_disk_check_sum(disk_blocks)

    print("Answer part 1:")
    print(f"Disc checksum after compressing is : {check_sum}")


def part2(file_path):
    """
    """
    disk_map = read_input(file_path)

    disk_blocks = get_disk_blocks_from_disk_map(disk_map)

    disk_blocks = compress_disk_blocks_filewise(disk_blocks)

    check_sum = calc_disk_check_sum(disk_blocks)

    print("Answer part 2:")
    print(f"Disc checksum after compressing is : {check_sum}")


if __name__ == "__main__":

    part1("day_09/day_09_input.txt")
    part2("day_09/day_09_input.txt")

