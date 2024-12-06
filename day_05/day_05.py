import itertools

def read_input(file_path):
    """
    """
    ordering_rules = set()
    updates = []

    with open(file_path, mode='rt', encoding='utf-8') as f:
        for line in f:
            if line.count('|') == 1:
                ordering_rules.add(line.strip('\n'))
            elif line.count(',') >= 1:
                updates.append(line.strip('\n').split(','))
        
    return ordering_rules, updates


def get_good_update(ordering_rules : set, updates : list):

    for update in updates:
        rules_for_update = set('|'.join([combination[0], combination[1]]) for combination in itertools.combinations(update,2))
        if ordering_rules.issuperset(rules_for_update):
            yield update


def check_update(ordering_rules : set, update : list):
    return ordering_rules.issuperset(set('|'.join([combination[0], combination[1]]) for combination in itertools.combinations(update,2)))


def make_bad_update_good(ordering_rules : set, bad_update : list):
    update_len = len(bad_update)

    for rule in ordering_rules:

        left = rule.split('|')[0]
        right = rule.split('|')[1]

        try:
            index_left = bad_update.index(left)
        except ValueError:
            index_left = -1

        try:
            index_right = bad_update.index(right)
        except ValueError:
            index_right = update_len
        
        if index_left > index_right:
            bad_update[index_left], bad_update[index_right] = bad_update[index_right], bad_update[index_left]

    if check_update(ordering_rules, bad_update):
        return bad_update
    else:
        return make_bad_update_good(ordering_rules, bad_update)


def part1(file_path):
    """
    """
    ordering_rules, updates = read_input(file_path)

    sum_middle = sum(int(update[len(update) // 2]) for update in get_good_update(ordering_rules, updates))
   
    print("Answer part 1:")
    print(f"Sum of all middle elements in correct updates is : {sum_middle}")


def part2(file_path):
    """
    """
    ordering_rules, updates = read_input(file_path)

    good_bad_updates = [make_bad_update_good(ordering_rules, update) for update in updates if not check_update(ordering_rules, update)]

    sum_middle = sum(int(update[len(update) // 2]) for update in good_bad_updates)

    print("Answer part 2:")
    print(f"Sum of all middle elements in bad updates made good is : {sum_middle}")


if __name__ == "__main__":

    part1("day_05/day_05_input.txt")
    part2("day_05/day_05_input.txt")
