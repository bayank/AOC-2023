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


if __name__ == "__main__":

    count = 0
    with open("day4_input.txt", "r") as f:
        for line in f:
            line = line.strip()
            count = count + (line_parser(line))

    print(f"Answer part 1: {count}")