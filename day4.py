import re


def line_parser(line):
    # Extract Card ID
    match_card_id = re.search(r"\bCard\s+(\d{1,3}):", line)
    card_id = int(match_card_id.group(1)) if match_card_id else None

    # Extract the rest of the string after the card ID
    rest_of_string = line[match_card_id.end():].strip()

    # Split the string into two lists using '|'
    entries_lists = [entry.strip().split() for entry in rest_of_string.split('|')]

    # Convert each entry to integers
    entries_lists = [[int(num) for num in entry] for entry in entries_lists]

    # Separate into two lists
    my_nums, winning_nums = entries_lists

    # Test for each entry and calculate points for part 1
    count = 0
    points = 0
    for num in my_nums:
        if num in winning_nums:
            count += 1
    if count == 0:
        return 0
    else:
        return pow(2, count - 1)


def extract_card_info(line):
    # Extract Card ID
    match_card_id = re.search(r"\bCard\s+(\d{1,3}):", line)
    card_id = int(match_card_id.group(1)) if match_card_id else None

    # Extract the rest of the string after the card ID
    rest_of_string = line[match_card_id.end():].strip()

    # Split the string into two lists using '|'
    entries_lists = [entry.strip().split() for entry in rest_of_string.split('|')]

    # Convert each entry to integers
    entries_lists = [[int(num) for num in entry] for entry in entries_lists]

    # Separate into two lists
    my_nums, winning_nums = entries_lists

    return card_id, my_nums, winning_nums


def get_card_string(card_id, file_path="test_input.txt"):
    card_strings = []
    # Read the content of the file
    with open(file_path, "r") as file:
        for line in file:
            current_card_id, my_nums, winning_nums = extract_card_info(line)
            if current_card_id == card_id:
                # Format the card string
                my_nums_str = " ".join(map(str, my_nums))
                winning_nums_str = " ".join(map(str, winning_nums))
                card_strings.append(f"Card {current_card_id}: {my_nums_str} | {winning_nums_str}")
    return card_strings

def get_winning_card_and_number(line):
    # Extract Card ID
    match_card_id = re.search(r"\bCard\s+(\d{1,3}):", line)
    card_id = int(match_card_id.group(1)) if match_card_id else None

    # Extract the rest of the string after the card ID
    rest_of_string = line[match_card_id.end():].strip()

    # Split the string into two lists using '|'
    entries_lists = [entry.strip().split() for entry in rest_of_string.split('|')]

    # Convert each entry to integers
    entries_lists = [[int(num) for num in entry] for entry in entries_lists]

    # Separate into two lists
    my_nums, winning_nums = entries_lists

    # Test for each entry and calculate points for part 1
    count = 0
    for num in my_nums:
        if num in winning_nums:
            count += 1

    return card_id, count


# generate a new list of winning cards, one copy each of the next winning number of cards
def card_gen(card_info):
    card_id, count2 = card_info
    new_list = []
    for card_id_copy in range(card_id+1, card_id+count2+1):
        new_list.append(card_id_copy)
    return new_list

lines = open('day4_input.txt', 'r').readlines()

def part1():
    total = 0
    for line in lines:
        x, y = map(str.split, line.split('|'))
        matches = set(x) & set(y)
        total += 2 ** (len(matches) - 1) if matches else 0
    return total

def part2():
    cards = [1] * len(lines)
    for i, line in enumerate(lines):
        x, y = map(str.split, line.split('|'))
        n = len(set(x) & set(y))
        for j in range(i + 1, min(i + 1 + n, len(lines))):
            cards[j] += cards[i]
    return sum(cards)




if __name__ == "__main__":

    # Add up the results for part 1
    count = 0
    with open("test_input.txt", "r") as f:
        for line in f:
            line = line.strip()
            count = count + (line_parser(line))

    # print(f"Answer part 1: {count}")

    card = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    #print(card_gen(get_winning_card_and_number(card)))
    card_list = []
    for card in card_gen(get_winning_card_and_number(card)):
        card_list += (get_card_string(card))
    print(card_list)

    with open("test_input.txt", "r") as f:
        for line in f:
            line = line.strip()
            print(card_gen(get_winning_card_and_number(line)))

    print(part2())
